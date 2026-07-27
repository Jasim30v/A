// اسم الكاش - تقدر تغيره لأي اسم
const CACHE_NAME = 'my-site-cache-v1';

// الملفات اللي تتخزن أوفلاين - ضيف صفحاتك المهمة هنا
const urlsToCache = [
    '/',
    '/index.html',
    '/style.css',
    '/script.js'
];

// تثبيت الـ Service Worker
self.addEventListener('install', function(event) {
    console.log('✅ Service Worker: تم التثبيت');
    event.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            console.log('📦 Service Worker: جاري تخزين الملفات');
            return cache.addAll(urlsToCache).catch(function(error) {
                console.log('⚠️ فشل تخزين بعض الملفات:', error);
            });
        })
    );
});

// تفعيل الـ Service Worker
self.addEventListener('activate', function(event) {
    console.log('🚀 Service Worker: تم التفعيل');
    var cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        console.log('🗑️ حذف الكاش القديم:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// استراتيجية التحميل: نجرب النت أولاً، لو فشل نرجع للكاش
self.addEventListener('fetch', function(event) {
    event.respondWith(
        fetch(event.request).then(function(response) {
            // لو النت شغال، نخزن النسخة الجديدة في الكاش
            if (response && response.status === 200) {
                var responseClone = response.clone();
                caches.open(CACHE_NAME).then(function(cache) {
                    cache.put(event.request, responseClone);
                });
            }
            return response;
        }).catch(function() {
            // لو النت مقطوع، نرجع النسخة المخزنة
            return caches.match(event.request).then(function(response) {
                return response || new Response('أنت غير متصل بالإنترنت');
            });
        })
    );
});

// إشعارات Push (اختياري)
self.addEventListener('push', function(event) {
    var options = {
        body: event.data ? event.data.text() : 'إشعار جديد',
        icon: '/icon-192.png',
        badge: '/icon-192.png',
        vibrate: [200, 100, 200],
        dir: 'rtl',
        lang: 'ar'
    };
    event.waitUntil(
        self.registration.showNotification('اسم موقعك', options)
    );
});

// الضغط على الإشعار
self.addEventListener('notificationclick', function(event) {
    event.notification.close();
    event.waitUntil(
        clients.openWindow('/')
    );
});
