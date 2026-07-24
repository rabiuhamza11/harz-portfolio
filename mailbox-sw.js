const CACHE_NAME = 'harz-mailbox-v1';
const ASSETS = [
  'https://rabiuhamza11.github.io/harz-portfolio/harz-mailbox.html',
  'https://rabiuhamza11.github.io/harz-portfolio/mailbox-manifest.json',
  'https://rabiuhamza11.github.io/harz-portfolio/mailbox-icon-192.png',
  'https://rabiuhamza11.github.io/harz-portfolio/mailbox-icon-512.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.map(k => k !== CACHE_NAME ? caches.delete(k) : null))));
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  if (e.request.url.includes('superagent-2286fb2f.base44.app')) {
    // Never cache API calls
    return;
  }
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});