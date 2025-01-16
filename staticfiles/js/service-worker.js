const CACHE_NAME = 'alquran-pwa-cache-v1';
const urlsToCache = [
    '/',
    '/offline/', // Halaman offline yang disiapkan
    '/static/img/icon.png',
];

// Install Service Worker
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                return cache.addAll(urlsToCache);
            })
    );
});

// Fetch Requests
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Kembalikan dari cache jika ada
                if (response) {
                    return response;
                }

                // Jika tidak ada di cache, coba ambil dari jaringan
                return fetch(event.request).catch(() => {
                    // Fallback ke halaman offline
                    return caches.match('/offline/');
                });
            })
    );
});

// Activate Service Worker
self.addEventListener('activate', (event) => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (!cacheWhitelist.includes(cacheName)) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
