/**
 * LIVRET DU CITOYEN 2026 - Interactive E-Learning Video Player
 * Features:
 * - 16:9 Cinematic Video Stage with dynamic visual scenes & animations
 * - Voiceover French Audio Narration (Web Speech API) with natural pacing
 * - Live Synchronized Subtitles (Sous-titres en temps réel)
 * - Video Controls: Play/Pause, Scrubber bar, Speed (0.75x, 1x, 1.25x), Volume, Fullscreen
 * - Scene navigator bookmarks
 * - Interactive End-of-Video Knowledge Checkpoint
 */

const VIDEO_STATE = {
  currentChapterId: "m1-c1",
  lessonData: null,
  currentSceneIndex: 0,
  isPlaying: false,
  playbackSpeed: 1.0,
  isMuted: false,
  showSubtitles: true,
  elapsedSeconds: 0,
  totalDurationSeconds: 110,
  timerInterval: null,
  currentAudio: null,
  currentUtterance: null
};

// Open Video Player Modal for a given chapter
async function openVideoLesson(chapterId = "m1-c1") {
  VIDEO_STATE.currentChapterId = chapterId;

  // Load video lessons data if not cached
  if (!APP_STATE.videoLessonsData) {
    try {
      const res = await fetch('data/video_lessons.json');
      APP_STATE.videoLessonsData = await res.json();
    } catch (e) {
      console.error('Error loading video lessons:', e);
      showToast("Impossible de charger la vidéo e-learning", "info");
      return;
    }
  }

  const lesson = APP_STATE.videoLessonsData.lessons[chapterId];
  if (!lesson) {
    showToast("La vidéo de ce chapitre sera bientôt disponible !", "info");
    return;
  }

  VIDEO_STATE.lessonData = lesson;
  VIDEO_STATE.currentSceneIndex = 0;
  VIDEO_STATE.elapsedSeconds = 0;
  VIDEO_STATE.isPlaying = false;

  // Compute total duration
  let totalSec = 0;
  lesson.scenes.forEach(s => totalSec += (s.durationSeconds || 18));
  VIDEO_STATE.totalDurationSeconds = totalSec;

  const modal = document.getElementById('video-player-modal');
  if (modal) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  renderVideoPlayerUI();
  loadScene(0);

  // Auto-play after 400ms
  setTimeout(() => {
    playVideo();
  }, 400);
}

// Close Video Player Modal
function closeVideoLesson() {
  pauseVideo();
  stopAudioPlayback();
  const modal = document.getElementById('video-player-modal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

// Render the main Video Player Shell
function renderVideoPlayerUI() {
  const container = document.getElementById('video-player-content');
  if (!container || !VIDEO_STATE.lessonData) return;

  const lesson = VIDEO_STATE.lessonData;

  container.innerHTML = `
    <!-- Republican Top Ribbon on Video -->
    <div class="video-ribbon"></div>

    <!-- Video Stage Header -->
    <div class="video-stage-header">
      <div class="video-title-wrap">
        <div style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap;">
          <span class="video-badge"><i class="fa-solid fa-play"></i> Capsule Vidéo E-Learning</span>
          <span class="video-badge" style="background:rgba(16,185,129,0.15); color:#10B981; border-color:rgba(16,185,129,0.3);"><i class="fa-solid fa-wand-magic-sparkles"></i> Voix IA Studio HD</span>
        </div>
        <h3 class="video-lesson-title">${lesson.title}</h3>
      </div>
      <button class="video-close-btn" onclick="closeVideoLesson()" title="Fermer la vidéo" aria-label="Fermer">
        <i class="fa-solid fa-xmark"></i>
      </button>
    </div>

    <!-- 16:9 Cinematic Video Display Stage -->
    <div class="video-stage-screen" id="video-stage-screen">
      <!-- Dynamic Scene Content inserted here -->
      <div id="video-scene-canvas" class="video-scene-canvas"></div>

      <!-- Live Synchronized Subtitles (CC) -->
      <div class="video-subtitles-bar" id="video-subtitles-bar" style="${VIDEO_STATE.showSubtitles ? '' : 'display:none;'}">
        <span id="video-subtitles-text">Chargement de la leçon...</span>
      </div>
    </div>

    <!-- Video Timeline & Controls Toolbar -->
    <div class="video-controls-bar">
      
      <!-- Scrubber Track with Scene Markers -->
      <div class="video-scrubber-track" id="video-scrubber-track" onclick="handleScrubberClick(event)">
        <div class="video-scrubber-fill" id="video-scrubber-fill" style="width: 0%;"></div>
        ${lesson.scenes.map((s, idx) => {
          let sceneStartSec = 0;
          for (let i = 0; i < idx; i++) sceneStartSec += (lesson.scenes[i].durationSeconds || 18);
          const posPct = (sceneStartSec / VIDEO_STATE.totalDurationSeconds) * 100;
          return `
            <div class="video-scene-marker" style="left: ${posPct}%;" title="Partie ${idx + 1} : ${s.title}" onclick="event.stopPropagation(); loadScene(${idx});"></div>
          `;
        }).join('')}
      </div>

      <!-- Playback Buttons & Utilities -->
      <div class="video-buttons-row">
        
        <div class="video-ctrl-left">
          <!-- Play / Pause -->
          <button class="video-ctrl-btn play-btn" id="btn-video-play-pause" onclick="togglePlayPause()" title="Lecture / Pause (Espace)">
            <i class="fa-solid fa-play" id="video-play-icon"></i>
          </button>

          <!-- Prev Scene -->
          <button class="video-ctrl-btn" onclick="prevScene()" title="Scène précédente">
            <i class="fa-solid fa-backward-step"></i>
          </button>

          <!-- Next Scene -->
          <button class="video-ctrl-btn" onclick="nextScene()" title="Scène suivante">
            <i class="fa-solid fa-forward-step"></i>
          </button>

          <!-- Time Display -->
          <span class="video-time-indicator" id="video-time-indicator">00:00 / 01:50</span>
        </div>

        <div class="video-ctrl-right">
          <!-- Subtitles Toggle -->
          <button class="video-ctrl-btn ${VIDEO_STATE.showSubtitles ? 'active-tool' : ''}" id="btn-video-cc" onclick="toggleSubtitles()" title="Activer / Désactiver les sous-titres">
            <i class="fa-solid fa-closed-captioning"></i>
          </button>

          <!-- Playback Speed -->
          <button class="video-speed-btn" id="btn-video-speed" onclick="cyclePlaybackSpeed()" title="Vitesse de lecture">
            ${VIDEO_STATE.playbackSpeed}x
          </button>

          <!-- Mute / Audio Toggle -->
          <button class="video-ctrl-btn" id="btn-video-mute" onclick="toggleMute()" title="Son activé / Couper le son">
            <i class="fa-solid ${VIDEO_STATE.isMuted ? 'fa-volume-xmark' : 'fa-volume-high'}" id="video-sound-icon"></i>
          </button>

          <!-- Fullscreen -->
          <button class="video-ctrl-btn" onclick="toggleFullscreen()" title="Plein écran">
            <i class="fa-solid fa-expand"></i>
          </button>
        </div>

      </div>

      <!-- Quick Scene Tabs Navigator -->
      <div class="video-scene-tabs">
        ${lesson.scenes.map((s, idx) => `
          <button class="video-scene-tab ${idx === 0 ? 'active' : ''}" id="v-tab-${idx}" onclick="loadScene(${idx})">
            <span>${idx + 1}. ${s.title.substring(0, 22)}${s.title.length > 22 ? '...' : ''}</span>
          </button>
        `).join('')}
      </div>

    </div>
  `;
}

// Load and Display a specific Scene
function loadScene(index) {
  const lesson = VIDEO_STATE.lessonData;
  if (!lesson || index < 0 || index >= lesson.scenes.length) return;

  VIDEO_STATE.currentSceneIndex = index;
  const scene = lesson.scenes[index];

  // Calculate elapsed time from previous scenes
  let startSec = 0;
  for (let i = 0; i < index; i++) startSec += (lesson.scenes[i].durationSeconds || 18);
  VIDEO_STATE.elapsedSeconds = startSec;

  // Update Scene Tabs
  document.querySelectorAll('.video-scene-tab').forEach((tab, i) => {
    tab.classList.toggle('active', i === index);
  });

  // Render Scene Canvas
  const canvas = document.getElementById('video-scene-canvas');
  if (!canvas) return;

  // Visual Theme classes
  canvas.className = `video-scene-canvas theme-${scene.visualTheme || 'tricolore'}`;

  let sceneHTML = `
    <div class="video-scene-badge-row">
      <span class="scene-badge"><i class="fa-solid ${scene.icon || 'fa-landmark'}"></i> ${scene.badge}</span>
      <span class="scene-counter">Partie ${scene.number} sur ${lesson.totalScenes}</span>
    </div>

    <div class="video-scene-main">
      <h2 class="scene-heading animate-pop">${scene.heading}</h2>
      <h4 class="scene-subheading animate-fade-delay">${scene.subheading}</h4>

      <!-- Key Visual Cards -->
      ${scene.keyPoints ? `
        <div class="scene-cards-grid">
          ${scene.keyPoints.map((pt, pIdx) => `
            <div class="scene-point-card animate-stagger" style="animation-delay: ${0.2 + pIdx * 0.15}s;">
              <i class="fa-solid fa-circle-check" style="color:var(--success); font-size:1.1rem; flex-shrink:0;"></i>
              <span>${pt}</span>
            </div>
          `).join('')}
        </div>
      ` : ''}

      <!-- Interactive Checkpoint Quiz if End Scene -->
      ${scene.quiz ? `
        <div class="scene-checkpoint-box animate-pop">
          <div class="checkpoint-q"><i class="fa-solid fa-question-circle"></i> ${scene.quiz.question}</div>
          <div class="checkpoint-options">
            ${scene.quiz.options.map((opt, oIdx) => `
              <button class="checkpoint-opt-btn" onclick="answerVideoCheckpoint(${oIdx}, ${scene.quiz.correctIndex}, '${scene.quiz.explanation.replace(/'/g, "\\'")}')">
                <span class="checkpoint-opt-letter">${['A', 'B', 'C'][oIdx]}</span>
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>
          <div id="checkpoint-feedback-box" class="checkpoint-feedback"></div>
        </div>
      ` : ''}

      <!-- Takeaway Banner -->
      ${scene.takeaway && !scene.quiz ? `
        <div class="scene-takeaway-card animate-stagger" style="animation-delay: 0.8s;">
          <i class="fa-solid fa-lightbulb" style="color:var(--fr-gold); font-size:1.2rem;"></i>
          <span><strong>À retenir :</strong> ${scene.takeaway}</span>
        </div>
      ` : ''}
    </div>
  `;

  canvas.innerHTML = sceneHTML;

  // Update Subtitles
  const subEl = document.getElementById('video-subtitles-text');
  if (subEl) subEl.textContent = scene.narrationText;

  updateScrubberUI();

  // Speak Narration using Neural AI Audio or fallback
  if (VIDEO_STATE.isPlaying) {
    playSceneAudio(scene);
  }
}

// Play Scene Audio using Studio Neural AI MP3
function playSceneAudio(scene) {
  stopAudioPlayback();
  if (VIDEO_STATE.isMuted || !scene) return;

  if (scene.audioSrc) {
    const audio = new Audio(scene.audioSrc);
    audio.playbackRate = VIDEO_STATE.playbackSpeed;
    audio.muted = VIDEO_STATE.isMuted;
    VIDEO_STATE.currentAudio = audio;

    audio.onended = () => {
      // Auto-advance to next scene after 600ms if playing
      if (VIDEO_STATE.isPlaying && VIDEO_STATE.currentSceneIndex < VIDEO_STATE.lessonData.scenes.length - 1) {
        setTimeout(() => {
          if (VIDEO_STATE.isPlaying) nextScene();
        }, 600);
      }
    };

    audio.play().catch(err => {
      console.warn("AI Audio autoplay issue, using fallback:", err);
      speakFallbackNarration(scene.narrationText);
    });
  } else {
    speakFallbackNarration(scene.narrationText);
  }
}

// Stop current audio playback
function stopAudioPlayback() {
  if (VIDEO_STATE.currentAudio) {
    VIDEO_STATE.currentAudio.pause();
    VIDEO_STATE.currentAudio.currentTime = 0;
    VIDEO_STATE.currentAudio = null;
  }
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
}

// Fallback Speech Synthesis if audio file unavailable
function speakFallbackNarration(text) {
  if (!('speechSynthesis' in window) || VIDEO_STATE.isMuted) return;
  window.speechSynthesis.cancel();
  VIDEO_STATE.currentUtterance = new SpeechSynthesisUtterance(text);
  VIDEO_STATE.currentUtterance.lang = 'fr-FR';
  VIDEO_STATE.currentUtterance.rate = VIDEO_STATE.playbackSpeed * 0.95;
  VIDEO_STATE.currentUtterance.onend = () => {
    if (VIDEO_STATE.isPlaying && VIDEO_STATE.currentSceneIndex < VIDEO_STATE.lessonData.scenes.length - 1) {
      setTimeout(() => {
        if (VIDEO_STATE.isPlaying) nextScene();
      }, 800);
    }
  };
  window.speechSynthesis.speak(VIDEO_STATE.currentUtterance);
}

// Play / Pause Video
function playVideo() {
  VIDEO_STATE.isPlaying = true;
  const icon = document.getElementById('video-play-icon');
  if (icon) icon.className = "fa-solid fa-pause";

  clearInterval(VIDEO_STATE.timerInterval);
  VIDEO_STATE.timerInterval = setInterval(() => {
    VIDEO_STATE.elapsedSeconds++;
    updateScrubberUI();

    // Check if we reached end of all scenes
    if (VIDEO_STATE.elapsedSeconds >= VIDEO_STATE.totalDurationSeconds) {
      pauseVideo();
    }
  }, 1000 / VIDEO_STATE.playbackSpeed);

  const scene = VIDEO_STATE.lessonData.scenes[VIDEO_STATE.currentSceneIndex];
  if (scene) {
    if (VIDEO_STATE.currentAudio && VIDEO_STATE.currentAudio.paused) {
      VIDEO_STATE.currentAudio.playbackRate = VIDEO_STATE.playbackSpeed;
      VIDEO_STATE.currentAudio.play().catch(() => playSceneAudio(scene));
    } else {
      playSceneAudio(scene);
    }
  }
}

function pauseVideo() {
  VIDEO_STATE.isPlaying = false;
  const icon = document.getElementById('video-play-icon');
  if (icon) icon.className = "fa-solid fa-play";

  clearInterval(VIDEO_STATE.timerInterval);
  if (VIDEO_STATE.currentAudio) {
    VIDEO_STATE.currentAudio.pause();
  }
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
}

function togglePlayPause() {
  if (VIDEO_STATE.isPlaying) pauseVideo();
  else playVideo();
}

// Next & Previous Scene
function nextScene() {
  if (!VIDEO_STATE.lessonData) return;
  if (VIDEO_STATE.currentSceneIndex < VIDEO_STATE.lessonData.scenes.length - 1) {
    loadScene(VIDEO_STATE.currentSceneIndex + 1);
  } else {
    pauseVideo();
  }
}

function prevScene() {
  if (VIDEO_STATE.currentSceneIndex > 0) {
    loadScene(VIDEO_STATE.currentSceneIndex - 1);
  }
}

// Update Scrubber bar & Time indicator
function updateScrubberUI() {
  const fill = document.getElementById('video-scrubber-fill');
  const timeEl = document.getElementById('video-time-indicator');

  const cur = Math.min(VIDEO_STATE.elapsedSeconds, VIDEO_STATE.totalDurationSeconds);
  const total = VIDEO_STATE.totalDurationSeconds;
  const pct = (cur / total) * 100;

  if (fill) fill.style.width = `${pct}%`;

  if (timeEl) {
    const curM = Math.floor(cur / 60).toString().padStart(2, '0');
    const curS = (cur % 60).toString().padStart(2, '0');
    const totM = Math.floor(total / 60).toString().padStart(2, '0');
    const totS = (total % 60).toString().padStart(2, '0');
    timeEl.textContent = `${curM}:${curS} / ${totM}:${totS}`;
  }
}

// Handle Click on Timeline Scrubber
function handleScrubberClick(e) {
  const track = document.getElementById('video-scrubber-track');
  if (!track || !VIDEO_STATE.lessonData) return;

  const rect = track.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const pct = Math.max(0, Math.min(1, clickX / rect.width));
  const targetSec = Math.round(pct * VIDEO_STATE.totalDurationSeconds);

  // Find which scene corresponds to targetSec
  let accumulated = 0;
  for (let i = 0; i < VIDEO_STATE.lessonData.scenes.length; i++) {
    const dur = VIDEO_STATE.lessonData.scenes[i].durationSeconds || 18;
    if (targetSec <= accumulated + dur || i === VIDEO_STATE.lessonData.scenes.length - 1) {
      loadScene(i);
      VIDEO_STATE.elapsedSeconds = targetSec;
      updateScrubberUI();
      break;
    }
    accumulated += dur;
  }
}

// Toggle Live Subtitles
function toggleSubtitles() {
  VIDEO_STATE.showSubtitles = !VIDEO_STATE.showSubtitles;
  const bar = document.getElementById('video-subtitles-bar');
  const btn = document.getElementById('btn-video-cc');
  if (bar) bar.style.display = VIDEO_STATE.showSubtitles ? 'block' : 'none';
  if (btn) btn.classList.toggle('active-tool', VIDEO_STATE.showSubtitles);
}

// Cycle Playback Speed (0.75x -> 1x -> 1.25x -> 1.5x)
function cyclePlaybackSpeed() {
  const speeds = [0.75, 1.0, 1.25, 1.5];
  const idx = speeds.indexOf(VIDEO_STATE.playbackSpeed);
  VIDEO_STATE.playbackSpeed = speeds[(idx + 1) % speeds.length];

  const btn = document.getElementById('btn-video-speed');
  if (btn) btn.textContent = `${VIDEO_STATE.playbackSpeed}x`;

  if (VIDEO_STATE.currentAudio) {
    VIDEO_STATE.currentAudio.playbackRate = VIDEO_STATE.playbackSpeed;
  }

  if (VIDEO_STATE.isPlaying) {
    clearInterval(VIDEO_STATE.timerInterval);
    VIDEO_STATE.timerInterval = setInterval(() => {
      VIDEO_STATE.elapsedSeconds++;
      updateScrubberUI();
      if (VIDEO_STATE.elapsedSeconds >= VIDEO_STATE.totalDurationSeconds) {
        pauseVideo();
      }
    }, 1000 / VIDEO_STATE.playbackSpeed);
  }
}

// Mute / Unmute
function toggleMute() {
  VIDEO_STATE.isMuted = !VIDEO_STATE.isMuted;
  const icon = document.getElementById('video-sound-icon');
  if (icon) {
    icon.className = `fa-solid ${VIDEO_STATE.isMuted ? 'fa-volume-xmark' : 'fa-volume-high'}`;
  }
  if (VIDEO_STATE.currentAudio) {
    VIDEO_STATE.currentAudio.muted = VIDEO_STATE.isMuted;
  }
  if (VIDEO_STATE.isMuted) {
    stopAudioPlayback();
  } else if (VIDEO_STATE.isPlaying) {
    const scene = VIDEO_STATE.lessonData.scenes[VIDEO_STATE.currentSceneIndex];
    if (scene) playSceneAudio(scene);
  }
}

// Fullscreen
function toggleFullscreen() {
  const screen = document.getElementById('video-player-modal');
  if (!screen) return;

  if (!document.fullscreenElement) {
    screen.requestFullscreen().catch(err => console.log(err));
  } else {
    document.exitFullscreen();
  }
}

// Answer Checkpoint Quiz
function answerVideoCheckpoint(optionIdx, correctIdx, explanation) {
  const feedbackBox = document.getElementById('checkpoint-feedback-box');
  const buttons = document.querySelectorAll('.checkpoint-opt-btn');
  if (!feedbackBox) return;

  buttons.forEach((b, i) => {
    b.disabled = true;
    if (i === correctIdx) b.classList.add('correct');
    else if (i === optionIdx) b.classList.add('wrong');
  });

  const isCorrect = optionIdx === correctIdx;
  feedbackBox.className = `checkpoint-feedback show ${isCorrect ? 'pass' : 'fail'}`;
  feedbackBox.innerHTML = `
    <strong>${isCorrect ? '✓ Excellent ! Bonne réponse.' : '✗ Incorrect.'}</strong><br>
    <span>${explanation}</span>
  `;

  if (isCorrect) {
    // Automatically mark chapter as completed in user progress
    if (!APP_STATE.userProgress.completedChapters.includes(VIDEO_STATE.currentChapterId)) {
      APP_STATE.userProgress.completedChapters.push(VIDEO_STATE.currentChapterId);
      saveUserProgress();
      renderCourseSidebar();
    }
    showToast("Félicitations ! Vidéo validée et chapitre marqué comme complété 🎓", "success");
  }
}

// Keyboard navigation inside Video
document.addEventListener('keydown', (e) => {
  const modal = document.getElementById('video-player-modal');
  if (!modal || !modal.classList.contains('active')) return;

  if (e.code === 'Space') {
    e.preventDefault();
    togglePlayPause();
  } else if (e.code === 'ArrowRight') {
    e.preventDefault();
    nextScene();
  } else if (e.code === 'ArrowLeft') {
    e.preventDefault();
    prevScene();
  } else if (e.code === 'Escape') {
    closeVideoLesson();
  }
});

window.openVideoLesson = openVideoLesson;
window.closeVideoLesson = closeVideoLesson;
window.togglePlayPause = togglePlayPause;
window.nextScene = nextScene;
window.prevScene = prevScene;
window.toggleSubtitles = toggleSubtitles;
window.cyclePlaybackSpeed = cyclePlaybackSpeed;
window.toggleMute = toggleMute;
window.toggleFullscreen = toggleFullscreen;
window.handleScrubberClick = handleScrubberClick;
window.loadScene = loadScene;
window.answerVideoCheckpoint = answerVideoCheckpoint;
