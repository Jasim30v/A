// ⚡ SERVICE WORKER PRO - ULTIMATE 2026 ⚡
const CACHE_VERSION = 'v1';
const CACHE_NAME = `static-${CACHE_VERSION}`;
const DYNAMIC_CACHE = `dynamic-${CACHE_VERSION}`;
const IMAGE_CACHE = `images-${CACHE_VERSION}`;
const FONT_CACHE = `fonts-${CACHE_VERSION}`;

// ========== INSTALL ==========
self.addEventListener('install', (event) => {
    event.waitUntil(
        Promise.all([
            caches.open(CACHE_NAME),
            caches.open(DYNAMIC_CACHE),
            caches.open(IMAGE_CACHE),
            caches.open(FONT_CACHE)
        ]).then(() => self.skipWaiting())
    );
});

// ========== ACTIVATE ==========
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames
                    .filter((cache) => {
                        return ![CACHE_NAME, DYNAMIC_CACHE, IMAGE_CACHE, FONT_CACHE].includes(cache);
                    })
                    .map((cache) => caches.delete(cache))
            );
        }).then(() => self.clients.claim())
    );
});

// ========== FETCH - ذكي مع استراتيجيات متعددة ==========
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);
    
    if (request.method !== 'GET') return;

    // صور - Cache First
    if (request.destination === 'image') {
        event.respondWith(cacheFirst(request, IMAGE_CACHE));
        return;
    }

    // خطوط - Cache First
    if (request.destination === 'font' || url.pathname.match(/\.(woff|woff2|ttf|eot)$/)) {
        event.respondWith(cacheFirst(request, FONT_CACHE));
        return;
    }

    // CSS/JS - Cache First مع تحديث خلفي
    if (request.destination === 'style' || request.destination === 'script') {
        event.respondWith(staleWhileRevalidate(request, CACHE_NAME));
        return;
    }

    // HTML - Network First
    if (request.destination === 'document') {
        event.respondWith(networkFirst(request, DYNAMIC_CACHE));
        return;
    }

    // الباقي - Network First
    event.respondWith(networkFirst(request, DYNAMIC_CACHE));
});

// ========== استراتيجية Cache First ==========
async function cacheFirst(request, cacheName) {
    const cached = await caches.match(request);
    if (cached) return cached;
    
    try {
        const response = await fetch(request);
        if (response && response.status === 200) {
            const cache = await caches.open(cacheName);
            cache.put(request, response.clone());
        }
        return response;
    } catch {
        return new Response('', { status: 408 });
    }
}

// ========== استراتيجية Network First ==========
async function networkFirst(request, cacheName) {
    try {
        const response = await fetch(request);
        if (response && response.status === 200) {
            const cache = await caches.open(cacheName);
            cache.put(request, response.clone());
        }
        return response;
    } catch {
        const cached = await caches.match(request);
        if (cached) return cached;
        
        if (request.destination === 'document') {
            const offlinePage = await caches.match('/');
            if (offlinePage) return offlinePage;
        }
        
        return new Response('غير متصل', { status: 503 });
    }
}

// ========== استراتيجية Stale While Revalidate ==========
async function staleWhileRevalidate(request, cacheName) {
    const cached = await caches.match(request);
    
    const fetchPromise = fetch(request).then((response) => {
        if (response && response.status === 200) {
            caches.open(cacheName).then((cache) => {
                cache.put(request, response.clone());
            });
        }
        return response;
    }).catch(() => cached);

    return cached || fetchPromise;
}

// ========== PUSH ==========
self.addEventListener('push', (event) => {
    if (!event.data) return;
    
    let data;
    try {
        data = event.data.json();
    } catch {
        data = { title: 'إشعار جديد', body: event.data.text() };
    }

    const options = {
        body: data.body || '',
        icon: data.icon || '/icon-192.png',
        badge: '/icon-192.png',
        image: data.image || '',
        vibrate: [200, 100, 200, 100, 200],
        dir: 'rtl',
        lang: 'ar',
        tag: data.tag || Date.now().toString(),
        data: data.url || '/',
        requireInteraction: data.requireInteraction || false,
        actions: data.actions || [
            { action: 'open', title: '🔓 فتح' },
            { action: 'close', title: '❌ إغلاق' }
        ]
    };

    event.waitUntil(
        self.registration.showNotification(data.title, options)
    );
});

// ========== NOTIFICATION CLICK ==========
self.addEventListener('notificationclick', (event) => {
    event.notification.close();

    if (event.action === 'close') return;

    const urlToOpen = event.notification.data || '/';

    event.waitUntil(
        clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
            for (const client of clientList) {
                if (client.url.includes(urlToOpen) && 'focus' in client) {
                    return client.focus();
                }
            }
            return clients.openWindow(urlToOpen);
        })
    );
});

// ========== BACKGROUND SYNC ==========
self.addEventListener('sync', (event) => {
    event.waitUntil(handleSync(event.tag));
});

async function handleSync(tag) {
    const cache = await caches.open(DYNAMIC_CACHE);
    const requests = await cache.keys();
    
    for (const request of requests) {
        try {
            await fetch(request);
        } catch {
            // إعادة المحاولة لاحقاً
        }
    }
}

// ========== PERIODIC SYNC ==========
self.addEventListener('periodicsync', (event) => {
    if (event.tag === 'content-sync') {
        event.waitUntil(updateContent());
    }
});

async function updateContent() {
    try {
        const response = await fetch('/');
        if (response.ok) {
            const cache = await caches.open(DYNAMIC_CACHE);
            await cache.put('/', response);
        }
    } catch {
        // فشل التحديث
    }
}

// ========== MESSAGE ==========
self.addEventListener('message', (event) => {
    const { type, payload } = event.data || {};

    switch (type) {
        case 'SKIP_WAITING':
            self.skipWaiting();
            break;
        case 'CLEAR_ALL_CACHE':
            event.waitUntil(
                caches.keys().then((names) => {
                    return Promise.all(names.map((name) => caches.delete(name)));
                })
            );
            break;
        case 'CLEAR_OLD_CACHE':
            event.waitUntil(
                caches.keys().then((cacheNames) => {
                    return Promise.all(
                        cacheNames
                            .filter((cache) => {
                                return ![CACHE_NAME, DYNAMIC_CACHE, IMAGE_CACHE, FONT_CACHE].includes(cache);
                            })
                            .map((cache) => caches.delete(cache))
                    );
                })
            );
            break;
        case 'GET_CACHE_SIZE':
            event.waitUntil(
                getCacheSize().then((size) => {
                    event.ports[0]?.postMessage({ size });
                })
            );
            break;
        default:
            break;
    }
});

// ========== حساب حجم الكاش ==========
async function getCacheSize() {
    const cacheNames = await caches.keys();
    let totalSize = 0;
    
    for (const name of cacheNames) {
        const cache = await caches.open(name);
        const requests = await cache.keys();
        
        for (const request of requests) {
            const response = await cache.match(request);
            if (response) {
                const blob = await response.blob();
                totalSize += blob.size;
            }
        }
    }
    
    return (totalSize / 1024 / 1024).toFixed(2) + ' MB';
}
