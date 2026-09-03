// KPSS 2026 Service Worker - v3 (cache busting)
const CACHE_NAME = 'kpss-v5';
const ASSETS = [
  '/',
  '/index.html',
  '/app.js',
  '/style.css',
  '/data.js',
  '/manifest.json'
];

self.addEventListener('install', (e) => {
  // Hemen aktif ol, eski SW'yi bekletme
  self.skipWaiting();
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
});

self.addEventListener('activate', (e) => {
  // Eski cache'leri temizle
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  // Network önce, cache fallback
  e.respondWith(
    fetch(e.request)
      .then(res => {
        // Başarılı ise cache'e de yaz
        const clone = res.clone();
        caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
        return res;
      })
      .catch(() => caches.match(e.request))
  );
});
