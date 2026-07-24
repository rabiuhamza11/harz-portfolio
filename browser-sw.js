// HARZ Browser Service Worker v2
const CACHE_NAME = 'harz-browser-v2';
const CACHE_URLS = [
  './harz-browser.html',
  './browser-manifest.json',
  './browser-icon-192.png',
  './browser-icon-512.png',
  './browser-favicon.png'
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
  const url = new URL(e.request.url);
  
  // Network first for API calls
  if (url.hostname.includes('base44.app') || url.pathname.includes('/functions/')) {
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
    return;
  }
  
  // Cache first for static assets, network fallback
  if (e.request.method === 'GET') {
    e.respondWith(
      caches.match(e.request).then((cached) => {
        const fetchPromise = fetch(e.request).then((response) => {
          // Cache same-origin responses
          if (response && response.status === 200 && url.origin === location.origin) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(e.request, clone));
          }
          return response;
        }).catch(() => cached);
        return cached || fetchPromise;
      })
    );
  }
});