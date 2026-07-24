// HARZ Super App Service Worker
const CACHE = 'harz-super-app-v3';
const ASSETS = [
  './harz-super-app.html',
  './super-app-manifest.json',
  './super-app-icon-192.png',
  './super-app-icon-512.png'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  // Only handle GET requests
  if (e.request.method !== 'GET') return;

  const url = new URL(e.request.url);

  // Only intercept requests for the Super App itself — let everything else pass through
  if (url.pathname.endsWith('harz-super-app.html') ||
      url.pathname.endsWith('super-app-manifest.json') ||
      url.pathname.endsWith('super-app-icon-192.png') ||
      url.pathname.endsWith('super-app-icon-512.png')) {
    e.respondWith(
      caches.match(e.request).then(cached => {
        const fetchPromise = fetch(e.request).then(network => {
          if (network && network.status === 200) {
            const clone = network.clone();
            caches.open(CACHE).then(c => c.put(e.request, clone));
          }
          return network;
        }).catch(() => cached);
        return cached || fetchPromise;
      })
    );
  }
  // All other requests (including navigations to other pages) pass through normally
});
