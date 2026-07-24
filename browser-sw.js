// HARZ Browser Service Worker v3
const CACHE_NAME = 'harz-browser-v3';

self.addEventListener('install', (e) => {
  self.skipWaiting();
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => 
      cache.addAll([
        './harz-browser.html',
        './browser-manifest.json',
        './browser-icon-192.png',
        './browser-icon-512.png',
        './browser-favicon.png'
      ]).catch(err => console.log('Cache error:', err))
    )
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    Promise.all([
      caches.keys().then((keys) => 
        Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
      ),
      self.clients.claim()
    ])
  );
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  
  const url = new URL(e.request.url);
  
  // Skip cross-origin requests (iframes etc)
  if (url.origin !== location.origin) return;
  
  // Network first for API, cache fallback
  if (url.hostname.includes('base44.app')) {
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
    return;
  }
  
  // Cache first for same-origin static files
  e.respondWith(
    caches.match(e.request).then((cached) => {
      if (cached) return cached;
      return fetch(e.request).then((response) => {
        if (response && response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(e.request, clone));
        }
        return response;
      }).catch(() => cached);
    })
  );
});