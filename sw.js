const CACHE = 'mexvisapro-v7';
const ASSETS = [
  '/',
  '/assets/css/style.min.css',
  '/assets/js/main.min.js',
  '/assets/img/hero-illustration.svg',
  '/assets/img/why-us.svg',
  '/assets/img/icon-192.png',
  '/manifest.json',
  '/favicon.ico',
  '/assets/img/apple-touch-icon.png',
  '/blog/',
  '/blog/mexico-temporary-residency-guide/',
  '/blog/permanent-residency-mexico-requirements/',
  '/blog/work-permit-mexico-2026/',
  '/blog/digital-nomad-visa-mexico/',
  '/blog/mexico-citizenship-naturalization/'
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
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;
  e.respondWith(
    fetch(e.request)
      .then(r => {
        if (r.ok) {
          const clone = r.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
        }
        return r;
      })
      .catch(() => caches.match(e.request))
  );
});
