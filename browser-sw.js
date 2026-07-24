// HARZ Browser Service Worker
const CACHE_NAME = 'harz-browser-v1';
const CACHE_URLS = [
  'https://rabiuhamza11.github.io/harz-portfolio/harz-browser.html',
  'https://rabiuhamza11.github.io/harz-portfolio/browser-manifest.json'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(CACHE_URLS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(
      keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  // Network first for API calls, cache first for pages
  if (e.request.url.includes('/functions/')) {
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
  } else {
    e.respondWith(
      caches.match(e.request).then((cached) => {
        return cached || fetch(e.request).then((response) => {
          return caches.open(CACHE_NAME).then((cache) => {
            if (e.request.url.includes('github.io')) cache.put(e.request, response.clone());
            return response;
          });
        }).catch(() => cached);
      })
    );
  }
});