/**
 * LIVRET DU CITOYEN 2026 - Main Application Controller
 * Handles State, Persistence (LocalStorage), Theme, Routing, and Global Events.
 */

const APP_STATE = {
  theme: localStorage.getItem('citoyen_theme') || 'light',
  currentTab: 'dashboard',
  courseData: null,
  quizzesData: null,
  flashcardsData: null,
  interviewData: null,
  userProgress: {
    completedChapters: [],
    quizScores: {}, // { quizId: { bestScore, total, date, passed } }
    examAttempts: [], // [ { score, total, percentage, passed, date } ]
    flashcardStats: {
      mastered: [],
      needsReview: []
    },
    flashcardSchedule: {}, // { cardId: { due, intervalMs, intervalLabel, lastRating, lastReviewed, reps } }
    flashcardFeedback: { again: 0, hard: 0, good: 0, easy: 0, totalReviews: 0, history: [] },
    checklist: {}
  }
};

// Initialize State from LocalStorage
function loadUserProgress() {
  const saved = localStorage.getItem('citoyen_progress_2026');
  if (saved) {
    try {
      const parsed = JSON.parse(saved);
      APP_STATE.userProgress = Object.assign(APP_STATE.userProgress, parsed);
      if (!APP_STATE.userProgress.flashcardStats) {
        APP_STATE.userProgress.flashcardStats = { mastered: [], needsReview: [] };
      }
      if (!APP_STATE.userProgress.flashcardSchedule) {
        APP_STATE.userProgress.flashcardSchedule = {};
      }
      if (!APP_STATE.userProgress.flashcardFeedback) {
        APP_STATE.userProgress.flashcardFeedback = { again: 0, hard: 0, good: 0, easy: 0, totalReviews: 0, history: [] };
      }
    } catch (e) {
      console.error('Error loading progress:', e);
    }
  }
}

function saveUserProgress() {
  localStorage.setItem('citoyen_progress_2026', JSON.stringify(APP_STATE.userProgress));
  updateDashboardKPIs();
  updateReadinessRing();
}

// Show Toast Notification
function showToast(message, type = 'info') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <i class="fa-solid ${type === 'success' ? 'fa-circle-check' : 'fa-circle-info'}"></i>
    <span>${message}</span>
  `;

  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// Switch Active View Tab
function switchTab(tabId) {
  APP_STATE.currentTab = tabId;

  // Update nav buttons
  document.querySelectorAll('.nav-tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === tabId);
  });

  // Update view sections
  document.querySelectorAll('.view-section').forEach(sec => {
    sec.classList.toggle('active', sec.id === `view-${tabId}`);
  });

  // Stop lesson audio or French AI Reader when switching views
  if (window.FrenchAIReader) {
    window.FrenchAIReader.stop();
  }
  if (tabId !== 'course' && window.stopAudioReading) {
    window.stopAudioReading();
  }

  // Scroll to top
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // Hook tab-specific renderers
  if (tabId === 'dashboard') {
    updateDashboardKPIs();
    updateReadinessRing();
  } else if (tabId === 'progress') {
    renderProgressDashboard();
  } else if (tabId === 'flashcards' && window.initFlashcardsView) {
    window.initFlashcardsView();
  } else if (tabId === 'interview' && window.initInterviewView) {
    window.initInterviewView();
  }
}

// Calculate Global Naturalization Readiness Score (0 to 100%)
function calculateReadinessScore() {
  if (!APP_STATE.courseData) return 0;

  // Total chapters count
  let totalChapters = 0;
  APP_STATE.courseData.modules.forEach(m => totalChapters += m.chapters.length);
  const chaptersRead = APP_STATE.userProgress.completedChapters.length;
  const courseWeight = totalChapters > 0 ? (chaptersRead / totalChapters) * 35 : 0; // 35% weight

  // Quizzes count
  const quizzesCount = APP_STATE.quizzesData ? APP_STATE.quizzesData.modules.length : 5;
  let passedQuizzes = 0;
  for (const qid in APP_STATE.userProgress.quizScores) {
    if (APP_STATE.userProgress.quizScores[qid].passed) passedQuizzes++;
  }
  const quizWeight = (passedQuizzes / quizzesCount) * 25; // 25% weight

  // Mock Exam
  const hasPassedExam = APP_STATE.userProgress.examAttempts.some(att => att.passed);
  const examWeight = hasPassedExam ? 20 : (APP_STATE.userProgress.examAttempts.length > 0 ? 10 : 0); // 20% weight

  // Flashcards Mastered
  const totalCards = APP_STATE.flashcardsData ? APP_STATE.flashcardsData.cards.length : 52;
  const masteredCards = APP_STATE.userProgress.flashcardStats.mastered.length;
  const cardWeight = totalCards > 0 ? (masteredCards / totalCards) * 15 : 0; // 15% weight

  // Checklist
  const checklistItems = Object.values(APP_STATE.userProgress.checklist);
  const checklistChecked = checklistItems.filter(Boolean).length;
  const checklistWeight = checklistItems.length > 0 ? (checklistChecked / checklistItems.length) * 5 : 0; // 5% weight

  const totalScore = Math.min(100, Math.round(courseWeight + quizWeight + examWeight + cardWeight + checklistWeight));
  return totalScore;
}

// Update Hero Progress Ring & Label
function updateReadinessRing() {
  const score = calculateReadinessScore();
  const circle = document.getElementById('hero-readiness-circle');
  const text = document.getElementById('hero-readiness-text');
  const label = document.getElementById('hero-readiness-status');

  if (circle) {
    // Circumference = 2 * PI * 50 = 314
    const offset = 314 - (314 * score) / 100;
    circle.style.strokeDashoffset = offset;
  }

  if (text) {
    text.textContent = `${score}%`;
  }

  if (label) {
    if (score >= 80) {
      label.textContent = "Prêt pour l'entretien ! 🎉";
      label.style.color = "#10B981";
    } else if (score >= 50) {
      label.textContent = "En bonne voie d'assimilation 👍";
      label.style.color = "#38BDF8";
    } else {
      label.textContent = "Préparation à approfondir 📖";
      label.style.color = "#E2E8F0";
    }
  }
}

// Update Dashboard KPI numbers & Module overview cards
function updateDashboardKPIs() {
  if (!APP_STATE.courseData) return;

  let totalChapters = 0;
  APP_STATE.courseData.modules.forEach(m => totalChapters += m.chapters.length);
  const chaptersRead = APP_STATE.userProgress.completedChapters.length;

  const chaptersKpi = document.getElementById('kpi-chapters-count');
  if (chaptersKpi) chaptersKpi.textContent = `${chaptersRead} / ${totalChapters}`;

  let passedQuizzes = 0;
  for (const qid in APP_STATE.userProgress.quizScores) {
    if (APP_STATE.userProgress.quizScores[qid].passed) passedQuizzes++;
  }
  const quizzesKpi = document.getElementById('kpi-quizzes-count');
  if (quizzesKpi) {
    const totalQ = APP_STATE.quizzesData ? APP_STATE.quizzesData.modules.length : 5;
    quizzesKpi.textContent = `${passedQuizzes} / ${totalQ}`;
  }

  const cardsKpi = document.getElementById('kpi-cards-count');
  if (cardsKpi) {
    const mastered = APP_STATE.userProgress.flashcardStats.mastered.length;
    const total = APP_STATE.flashcardsData ? APP_STATE.flashcardsData.cards.length : 52;
    cardsKpi.textContent = `${mastered} / ${total}`;
  }

  // Render Module Progress Cards in Dashboard
  const container = document.getElementById('dashboard-modules-grid');
  if (container && APP_STATE.courseData) {
    container.innerHTML = APP_STATE.courseData.modules.map(mod => {
      const modChapterIds = mod.chapters.map(c => c.id);
      const doneCount = modChapterIds.filter(id => APP_STATE.userProgress.completedChapters.includes(id)).length;
      const pct = Math.round((doneCount / mod.chapters.length) * 100);
      const isComplete = doneCount === mod.chapters.length;

      return `
        <div class="module-progress-card">
          <div class="module-card-header">
            <span class="module-card-number">Module ${mod.number}</span>
            <span class="module-card-status ${isComplete ? 'completed' : (doneCount > 0 ? 'in-progress' : 'not-started')}">
              <i class="fa-solid ${isComplete ? 'fa-circle-check' : (doneCount > 0 ? 'fa-spinner' : 'fa-circle')}"></i>
              ${isComplete ? 'Validé' : (doneCount > 0 ? 'En cours' : 'Non débuté')}
            </span>
          </div>
          <h4 class="module-card-title">${mod.title}</h4>
          <div class="progress-bar-container">
            <div class="progress-bar-fill" style="width: ${pct}%"></div>
          </div>
          <div class="module-card-footer">
            <span>${doneCount} sur ${mod.chapters.length} chapitres</span>
            <button class="btn-sm-primary" onclick="openModuleChapter('${mod.id}', '${mod.chapters[0].id}')">
              ${doneCount > 0 ? 'Continuer' : 'Débuter'} <i class="fa-solid fa-arrow-right"></i>
            </button>
          </div>
        </div>
      `;
    }).join('');
  }
}

// Toggle Light / Dark Theme
function toggleTheme() {
  APP_STATE.theme = APP_STATE.theme === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', APP_STATE.theme);
  localStorage.setItem('citoyen_theme', APP_STATE.theme);

  const icon = document.getElementById('theme-icon');
  if (icon) {
    icon.className = APP_STATE.theme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
  }
}

// App Initialization
async function initApp() {
  // Apply saved theme
  document.documentElement.setAttribute('data-theme', APP_STATE.theme);
  const icon = document.getElementById('theme-icon');
  if (icon) {
    icon.className = APP_STATE.theme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
  }

  loadUserProgress();

  // Load all JSON datasets
  try {
    const [courseRes, quizzesRes, flashcardsRes, interviewRes] = await Promise.all([
      fetch('data/course.json'),
      fetch('data/quizzes.json'),
      fetch('data/flashcards.json'),
      fetch('data/interview_prep.json')
    ]);

    APP_STATE.courseData = await courseRes.json();
    APP_STATE.quizzesData = await quizzesRes.json();
    APP_STATE.flashcardsData = await flashcardsRes.json();
    APP_STATE.interviewData = await interviewRes.json();

    // Initialize View Controllers
    if (window.initCourseView) window.initCourseView();
    if (window.initQuizHub) window.initQuizHub();
    if (window.initFlashcardsView) window.initFlashcardsView();
    if (window.initInterviewView) window.initInterviewView();

    updateDashboardKPIs();
    updateReadinessRing();

  } catch (error) {
    console.error('Error loading application datasets:', error);
    showToast('Erreur de chargement des données du cours', 'info');
  }

  // Bind Navigation Tabs
  document.querySelectorAll('.nav-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => switchTab(btn.dataset.tab));
  });

  // Global Quick Action shortcuts
  document.querySelectorAll('[data-goto]').forEach(el => {
    el.addEventListener('click', () => switchTab(el.dataset.goto));
  });
}

document.addEventListener('DOMContentLoaded', initApp);
