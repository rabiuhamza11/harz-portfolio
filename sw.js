// Magani AI Service Worker
const CACHE_NAME = 'magani-ai-v1';
const CACHE_URLS = [
  'chat.html',
  'manifest.json',
  'magani-icon-192.png',
  'magani-icon-512.png'
];

// Install - cache core files
self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(CACHE_URLS).catch(function() {
        // Ignore individual cache failures
      });
    })
  );
  self.skipWaiting();
});

// Activate - clean old caches
self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(names) {
      return Promise.all(
        names.filter(function(n) { return n !== CACHE_NAME; })
          .map(function(n) { return caches.delete(n); })
      );
    })
  );
  self.clients.claim();
});

// Fetch - network first, fallback to cache
self.addEventListener('fetch', function(e) {
  e.respondWith(
    fetch(e.request).then(function(response) {
      // Clone and cache successful responses
      if (response.ok) {
        const clone = response.clone();
        caches.open(CACHE_NAME).then(function(cache) {
          cache.put(e.request, clone);
        });
      }
      return response;
    }).catch(function() {
      // Fallback to cache when offline
      return caches.match(e.request).then(function(cached) {
        return cached || caches.match('chat.html');
      });
    })
  );
});
