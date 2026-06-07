const CACHE = 'mexvisapro-v20';
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
  '/blog/mexico-citizenship-naturalization/',
  '/blog/visa-buying-property-mexico/',
  '/blog/retire-in-mexico-2026/',
  '/blog/mexico-visa-requirements-2026/',
  '/blog/mexico-tourist-visa-fmm/',
  '/es/blog/',
  '/es/blog/mexico-temporary-residency-guide/',
  '/es/blog/permanent-residency-mexico-requirements/',
  '/es/blog/work-permit-mexico-2026/',
  '/es/blog/digital-nomad-visa-mexico/',
  '/es/blog/mexico-citizenship-naturalization/',
  '/es/blog/visa-buying-property-mexico/',
  '/es/blog/retire-in-mexico-2026/',
  '/es/blog/mexico-visa-requirements-2026/',
  '/es/blog/mexico-tourist-visa-fmm/',
  '/ru/blog/',
  '/ru/blog/mexico-temporary-residency-guide/',
  '/ru/blog/permanent-residency-mexico-requirements/',
  '/ru/blog/work-permit-mexico-2026/',
  '/ru/blog/digital-nomad-visa-mexico/',
  '/ru/blog/mexico-citizenship-naturalization/',
  '/ru/blog/visa-buying-property-mexico/',
  '/ru/blog/retire-in-mexico-2026/',
  '/ru/blog/mexico-visa-requirements-2026/',
  '/ru/blog/mexico-tourist-visa-fmm/',
  '/zh/blog/',
  '/zh/blog/mexico-temporary-residency-guide/',
  '/zh/blog/permanent-residency-mexico-requirements/',
  '/zh/blog/work-permit-mexico-2026/',
  '/zh/blog/digital-nomad-visa-mexico/',
  '/zh/blog/mexico-citizenship-naturalization/',
  '/zh/blog/visa-buying-property-mexico/',
  '/zh/blog/retire-in-mexico-2026/',
  '/zh/blog/mexico-visa-requirements-2026/',
  '/zh/blog/mexico-tourist-visa-fmm/',
  '/partners/',
  '/sitemap/'
];

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.map(k => caches.delete(k)))
    ).then(() => caches.open(CACHE).then(c => c.addAll(ASSETS)))
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
    .then(() => self.clients.matchAll()).then(clients =>
      clients.forEach(c => c.postMessage({ type: 'SW_UPDATED' }))
    )
  );
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
