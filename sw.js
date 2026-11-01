/**
 * LIVRET DU CITOYEN 2026 - Service Worker & Mode Hors-Ligne (PWA)
 * Cache-First with Stale-While-Revalidate for application assets and lessons
 */

const CACHE_NAME = 'citoyen-fr-v2026.1';

const STATIC_ASSETS = [
  './',
  './index.html',
  './css/style.css',
  './manifest.webmanifest',
  './js/app.js',
  './js/ai_reader.js',
  './js/course.js',
  './js/video_player.js',
  './js/quiz.js',
  './js/flashcards.js',
  './js/timeline.js',
  './js/geography.js',
  './js/interview.js',
  './js/progress.js',
  './data/course.json',
  './data/quizzes.json',
  './data/flashcards.json',
  './data/interview_prep.json',
  './data/timeline.json',
  './data/geography.json',
  './data/video_lessons.json',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './assets/icon.svg'
];

// Installation : Mise en cache des ressources critiques du socle
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Mise en cache initiale des fichiers essentiels...');
      return cache.addAll(STATIC_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// Activation : Nettoyage des anciens caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[ServiceWorker] Suppression ancien cache :', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Interception des requêtes
self.addEventListener('fetch', (event) => {
  const req = event.request;

  // Ignorer les requêtes non-GET et les requêtes Chrome extension
  if (req.method !== 'GET' || !req.url.startsWith('http')) {
    return;
  }

  // Navigation vers une page HTML -> servir index.html depuis le cache si hors-ligne
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req).catch(() => {
        return caches.match('./index.html') || caches.match('./');
      })
    );
    return;
  }

  // Ressources statiques locales ou externes (polices, CDN fontawesome, images)
  event.respondWith(
    caches.match(req).then((cachedResponse) => {
      if (cachedResponse) {
        // Stale-While-Revalidate : renvoyer le cache immédiatement, rafraîchir en tâche de fond
        fetch(req).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
            caches.open(CACHE_NAME).then((cache) => cache.put(req, networkResponse));
          }
        }).catch(() => {
          // Hors ligne : rien à faire, la réponse en cache a déjà été servie
        });
        return cachedResponse;
      }

      // Si pas en cache, chercher sur le réseau et sauvegarder en cache
      return fetch(req).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200) {
          return networkResponse;
        }

        // Mettre en cache dynamique les images ou polices CDN
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(req, responseToCache);
        });

        return networkResponse;
      }).catch((err) => {
        // En cas d'erreur réseau pour une image, on peut retourner un fallback ou null
        return cachedResponse;
      });
    })
  );
});
