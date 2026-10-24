/**
 * LIVRET DU CITOYEN 2026 - AnkiDroid Spaced Repetition Flashcards Engine
 * 
 * Features:
 * - Full HTML & Rich Text support on Front and Back
 * - AnkiDroid 4-button Feedback Mechanism:
 *     - Again (À revoir) : Snooze 1 min (60,000 ms)
 *     - Hard (Difficile)  : Snooze 6 min (360,000 ms)
 *     - Good (Correct)    : Snooze 10 min (600,000 ms)
 *     - Easy (Facile)     : Snooze 3 days (259,200,000 ms)
 * - Persistent Schedule & Feedback History in LocalStorage
 * - Queue Management: Due Cards first, Live Countdown for snoozed cards
 * - Early Review mode & Free Navigation mode
 * - Natural French TTS Audio pronunciation (clean HTML stripping)
 * - AnkiDroid Queue Counters: 🔵 Nouveau, 🔴 À revoir, 🟢 Révision, ⏳ En attente
 * - Comprehensive Retention & Feedback Statistics Modal
 */

// AnkiDroid Intervals Configuration
const ANKI_INTERVALS = {
  again: {
    key: 'again',
    ms: 1 * 60 * 1000,
    label: '1 min',
    title: 'À revoir',
    description: 'À revoir dans 1 minute',
    icon: 'fa-rotate-left',
    type: 'danger'
  },
  hard: {
    key: 'hard',
    ms: 6 * 60 * 1000,
    label: '6 min',
    title: 'Difficile',
    description: 'À revoir dans 6 minutes',
    icon: 'fa-triangle-exclamation',
    type: 'warning'
  },
  good: {
    key: 'good',
    ms: 10 * 60 * 1000,
    label: '10 min',
    title: 'Correct',
    description: 'À revoir dans 10 minutes',
    icon: 'fa-thumbs-up',
    type: 'primary'
  },
  easy: {
    key: 'easy',
    ms: 3 * 24 * 60 * 60 * 1000,
    label: '3 j',
    title: 'Facile',
    description: 'Snooze pour 3 jours',
    icon: 'fa-circle-check',
    type: 'success'
  }
};

let activeFlashcardsList = [];
let currentCardIndex = 0;
let isCardFlipped = false;
let currentCategoryFilter = "all-due";
let studyMode = "spaced"; // "spaced" (AnkiDroid Queue) or "browse" (Free Navigation)
let countdownIntervalId = null;

/**
 * Initialize the Flashcards view
 */
function initFlashcardsView() {
  if (!APP_STATE.flashcardsData) return;

  // Ensure schedule and feedback containers exist in userProgress
  if (!APP_STATE.userProgress.flashcardSchedule) {
    APP_STATE.userProgress.flashcardSchedule = {};
  }
  if (!APP_STATE.userProgress.flashcardFeedback) {
    APP_STATE.userProgress.flashcardFeedback = {
      again: 0,
      hard: 0,
      good: 0,
      easy: 0,
      totalReviews: 0,
      history: []
    };
  }

  setupCategoryFilter();
  updateAnkiHeaderBadges();
  filterFlashcards(currentCategoryFilter);
  bindKeyboardShortcuts();
}

/**
 * Helper to strip HTML tags for clean Text-to-Speech
 */
function stripHtmlTags(html) {
  if (!html) return "";
  const tmp = document.createElement("div");
  tmp.innerHTML = html;
  return tmp.textContent || tmp.innerText || "";
}

/**
 * Helper to check if a card is currently due
 */
function isCardDue(cardId) {
  const schedule = APP_STATE.userProgress.flashcardSchedule[cardId];
  if (!schedule) return true; // Never reviewed -> due immediately
  return Date.now() >= schedule.due;
}

/**
 * Helper to get card schedule state
 */
function getCardScheduleState(cardId) {
  const schedule = APP_STATE.userProgress.flashcardSchedule[cardId];
  if (!schedule) return 'new';
  if (Date.now() < schedule.due) return 'snoozed';
  if (schedule.lastRating === 'again' || schedule.lastRating === 'hard') return 'learning';
  return 'review';
}

/**
 * Update the AnkiDroid queue status badges
 */
function updateAnkiHeaderBadges() {
  if (!APP_STATE.flashcardsData) return;

  const cards = APP_STATE.flashcardsData.cards;
  let countNew = 0;
  let countLearning = 0;
  let countReview = 0;
  let countSnoozed = 0;

  cards.forEach(card => {
    const state = getCardScheduleState(card.id);
    if (state === 'new') countNew++;
    else if (state === 'snoozed') countSnoozed++;
    else if (state === 'learning') countLearning++;
    else if (state === 'review') countReview++;
  });

  const elNew = document.getElementById('fc-count-new');
  const elLearning = document.getElementById('fc-count-learning');
  const elReview = document.getElementById('fc-count-review');
  const elSnoozed = document.getElementById('fc-count-snoozed');

  if (elNew) elNew.textContent = countNew;
  if (elLearning) elLearning.textContent = countLearning;
  if (elReview) elReview.textContent = countReview;
  if (elSnoozed) elSnoozed.textContent = countSnoozed;

  // Counter badge on toolbar
  const counterElement = document.getElementById('flashcard-counter-badge');
  if (counterElement && activeFlashcardsList.length > 0) {
    counterElement.textContent = `${currentCardIndex + 1} / ${activeFlashcardsList.length}`;
  }
}

/**
 * Populate Category and Filter Dropdown
 */
function setupCategoryFilter() {
  const select = document.getElementById('flashcard-category-select');
  if (!select || !APP_STATE.flashcardsData) return;

  const total = APP_STATE.flashcardsData.totalCards || APP_STATE.flashcardsData.cards.length;
  const cats = APP_STATE.flashcardsData.categories;

  // Calculate current due count
  const dueCount = APP_STATE.flashcardsData.cards.filter(c => isCardDue(c.id)).length;
  const snoozedCount = APP_STATE.flashcardsData.cards.filter(c => !isCardDue(c.id)).length;

  select.innerHTML = `
    <optgroup label="Files AnkiDroid">
      <option value="all-due">⚡ Cartes à réviser maintenant (${dueCount})</option>
      <option value="all">📚 Toutes les cartes (${total})</option>
      <option value="snoozed">⏳ Cartes en attente / Snoozed (${snoozedCount})</option>
      <option value="needs-review">⚠️ Cartes difficiles (À revoir / Again)</option>
      <option value="mastered">✓ Cartes maîtrisées (Good / Easy)</option>
    </optgroup>
    <optgroup label="Par Thématique">
      ${cats.map(c => {
        const catTotal = APP_STATE.flashcardsData.cards.filter(card => card.category === c).length;
        return `<option value="${c}">${c} (${catTotal})</option>`;
      }).join('')}
    </optgroup>
  `;

  select.value = currentCategoryFilter;
  select.onchange = (e) => filterFlashcards(e.target.value);
}

/**
 * Filter flashcards according to chosen criteria
 */
function filterFlashcards(filterKey) {
  currentCategoryFilter = filterKey;
  const allCards = APP_STATE.flashcardsData.cards;

  if (filterKey === 'all-due') {
    activeFlashcardsList = allCards.filter(c => isCardDue(c.id));
  } else if (filterKey === 'all') {
    activeFlashcardsList = [...allCards];
  } else if (filterKey === 'snoozed') {
    activeFlashcardsList = allCards.filter(c => !isCardDue(c.id));
  } else if (filterKey === 'needs-review') {
    activeFlashcardsList = allCards.filter(c => APP_STATE.userProgress.flashcardStats.needsReview.includes(c.id));
  } else if (filterKey === 'mastered') {
    activeFlashcardsList = allCards.filter(c => APP_STATE.userProgress.flashcardStats.mastered.includes(c.id));
  } else {
    // Specific category
    if (studyMode === 'spaced') {
      const catDue = allCards.filter(c => c.category === filterKey && isCardDue(c.id));
      activeFlashcardsList = catDue.length > 0 ? catDue : allCards.filter(c => c.category === filterKey);
    } else {
      activeFlashcardsList = allCards.filter(c => c.category === filterKey);
    }
  }

  currentCardIndex = 0;
  isCardFlipped = false;
  renderFlashcard();
  updateAnkiHeaderBadges();
}

/**
 * Jump directly to a specific flashcard by ID
 */
function jumpToCard(cardId) {
  if (!APP_STATE.flashcardsData || !APP_STATE.flashcardsData.cards) return;
  const allCards = APP_STATE.flashcardsData.cards;
  const idx = allCards.findIndex(c => c.id === cardId);
  if (idx !== -1) {
    currentCategoryFilter = 'all';
    const select = document.getElementById('flashcard-category-select');
    if (select) select.value = 'all';
    activeFlashcardsList = [...allCards];
    currentCardIndex = idx;
    isCardFlipped = false;
    renderFlashcard();
  }
}
window.jumpToCard = jumpToCard;

/**
 * Render the active card
 */
function renderFlashcard() {
  const cardElement = document.getElementById('main-flashcard-3d');
  const counterElement = document.getElementById('flashcard-counter-badge');
  const emptyState = document.getElementById('flashcards-empty-state');
  const sessionComplete = document.getElementById('flashcards-session-complete');
  const sceneWrapper = document.getElementById('flashcard-scene-wrapper');
  const controlsFront = document.getElementById('fc-controls-front');
  const controlsBack = document.getElementById('fc-controls-back');

  if (countdownIntervalId) {
    clearInterval(countdownIntervalId);
    countdownIntervalId = null;
  }

  if (!cardElement) return;

  // Handle case when no cards match filter
  if (activeFlashcardsList.length === 0) {
    if (sceneWrapper) sceneWrapper.style.display = 'none';
    if (controlsFront) controlsFront.style.display = 'none';
    if (controlsBack) controlsBack.style.display = 'none';
    if (counterElement) counterElement.textContent = "0 / 0";

    // If we were on 'all-due', show the session completion screen with snooze countdown
    if (currentCategoryFilter === 'all-due') {
      if (emptyState) emptyState.style.display = 'none';
      if (sessionComplete) {
        sessionComplete.style.display = 'block';
        startNextDueCountdown();
      }
    } else {
      if (sessionComplete) sessionComplete.style.display = 'none';
      if (emptyState) emptyState.style.display = 'block';
    }
    return;
  }

  if (sceneWrapper) sceneWrapper.style.display = 'block';
  if (emptyState) emptyState.style.display = 'none';
  if (sessionComplete) sessionComplete.style.display = 'none';

  const card = activeFlashcardsList[currentCardIndex];
  if (!card) return;

  // Reset 3D flip state
  cardElement.classList.remove('flipped');
  isCardFlipped = false;

  // Show front controls, hide rating controls
  if (controlsFront) controlsFront.style.display = 'flex';
  if (controlsBack) controlsBack.style.display = 'none';

  // Populate Front (supports HTML)
  const frontCat = document.getElementById('fc-front-category');
  const frontTag = document.getElementById('fc-front-tag');
  const frontText = document.getElementById('fc-front-text');
  if (frontCat) frontCat.textContent = card.category;
  if (frontTag) frontTag.textContent = card.tag || "";
  if (frontText) frontText.innerHTML = card.front;

  // Populate Back (supports HTML)
  const backCat = document.getElementById('fc-back-category');
  const backTag = document.getElementById('fc-back-tag');
  const backText = document.getElementById('fc-back-text');
  const backTip = document.getElementById('fc-back-tip-text');
  if (backCat) backCat.textContent = card.category;
  if (backTag) backTag.textContent = card.tag || "";
  if (backText) backText.innerHTML = card.back;
  if (backTip) backTip.textContent = card.tip || "Point clé attendu lors de l'entretien.";

  // Reset scroll positions so the new card always starts cleanly at the top
  const frontContent = document.querySelector('.flashcard-face.front .fc-content-center');
  const backContent = document.querySelector('.flashcard-face.back .fc-content-center');
  if (frontContent) frontContent.scrollTop = 0;
  if (backContent) backContent.scrollTop = 0;

  // Update schedule status pill on card
  renderScheduleBadge(card.id);

  // Update Counter
  if (counterElement) {
    counterElement.textContent = `${currentCardIndex + 1} / ${activeFlashcardsList.length}`;
  }
}

/**
 * Display schedule status pill on the card
 */
function renderScheduleBadge(cardId) {
  const schedule = APP_STATE.userProgress.flashcardSchedule[cardId];
  const frontPill = document.getElementById('fc-front-schedule-pill');
  const backPill = document.getElementById('fc-back-schedule-pill');
  const statusPill = document.getElementById('fc-mastery-status');

  let pillHtml = '';
  let statusHtml = '';

  if (!schedule) {
    pillHtml = `<span class="fc-schedule-tag tag-new"><i class="fa-solid fa-sparkles"></i> Nouveau</span>`;
    statusHtml = `<span style="color:var(--info); font-weight:600;"><i class="fa-regular fa-circle"></i> Non vue</span>`;
  } else {
    const isDue = Date.now() >= schedule.due;
    const intervalTxt = schedule.intervalLabel || '';
    const ratingLabels = {
      again: 'À revoir',
      hard: 'Difficile',
      good: 'Correct',
      easy: 'Facile'
    };
    const lastRatingText = ratingLabels[schedule.lastRating] || schedule.lastRating;

    if (isDue) {
      pillHtml = `<span class="fc-schedule-tag tag-due"><i class="fa-solid fa-bell"></i> À réviser (${intervalTxt})</span>`;
    } else {
      const remainingSec = Math.max(0, Math.round((schedule.due - Date.now()) / 1000));
      const remainingMin = Math.ceil(remainingSec / 60);
      const remainingHours = (remainingSec / 3600).toFixed(1);
      let timeTxt = `${remainingMin} min`;
      if (remainingSec > 86400) timeTxt = `${Math.ceil(remainingSec / 86400)} j`;
      else if (remainingSec > 3600) timeTxt = `${remainingHours} h`;

      pillHtml = `<span class="fc-schedule-tag tag-snoozed"><i class="fa-solid fa-clock"></i> Snooze (${timeTxt})</span>`;
    }

    if (schedule.lastRating === 'easy' || schedule.lastRating === 'good') {
      statusHtml = `<span style="color:var(--success); font-weight:700;"><i class="fa-solid fa-circle-check"></i> Maîtrisée (${lastRatingText})</span>`;
    } else {
      statusHtml = `<span style="color:var(--danger); font-weight:700;"><i class="fa-solid fa-triangle-exclamation"></i> À revoir (${lastRatingText})</span>`;
    }
  }

  if (frontPill) frontPill.innerHTML = pillHtml;
  if (backPill) backPill.innerHTML = pillHtml;
  if (statusPill) statusPill.innerHTML = statusHtml;
}

/**
 * 3D Flip Card Action
 */
function flipCard(event) {
  // If user clicked inside an image, button, link, or was selecting text, ignore flip
  if (event) {
    if (event.target && event.target.closest('button, a, input, select, .flashcard-img')) {
      return;
    }
    const selection = window.getSelection();
    if (selection && selection.toString().length > 0) {
      return;
    }
  }

  const cardElement = document.getElementById('main-flashcard-3d');
  const controlsFront = document.getElementById('fc-controls-front');
  const controlsBack = document.getElementById('fc-controls-back');

  if (!cardElement) return;

  isCardFlipped = !isCardFlipped;
  cardElement.classList.toggle('flipped', isCardFlipped);

  if (isCardFlipped) {
    if (controlsFront) controlsFront.style.display = 'none';
    if (controlsBack) controlsBack.style.display = 'flex';
    const backContent = document.querySelector('.flashcard-face.back .fc-content-center');
    if (backContent) backContent.scrollTop = 0;
  } else {
    if (controlsFront) controlsFront.style.display = 'flex';
    if (controlsBack) controlsBack.style.display = 'none';
    const frontContent = document.querySelector('.flashcard-face.front .fc-content-center');
    if (frontContent) frontContent.scrollTop = 0;
  }
}

/**
 * Open high-resolution lightbox for flashcard illustration
 */
function openImageLightbox(src, alt) {
  const modal = document.getElementById('fc-image-modal');
  const img = document.getElementById('fc-lightbox-img');
  const caption = document.getElementById('fc-lightbox-caption');
  if (modal && img) {
    img.src = src;
    img.alt = alt || "Illustration officielle";
    if (caption) caption.textContent = alt || "Illustration officielle – Livret du Citoyen 2026";
    modal.style.display = 'flex';
  }
}

/**
 * Close high-resolution lightbox
 */
function closeImageLightbox() {
  const modal = document.getElementById('fc-image-modal');
  if (modal) modal.style.display = 'none';
}
window.openImageLightbox = openImageLightbox;
window.closeImageLightbox = closeImageLightbox;

/**
 * Collect User Feedback and Snooze Card (AnkiDroid Spaced Repetition)
 * @param {'again'|'hard'|'good'|'easy'} rating 
 */
function rateFlashcard(rating) {
  const card = activeFlashcardsList[currentCardIndex];
  if (!card) return;

  const intervalConfig = ANKI_INTERVALS[rating];
  if (!intervalConfig) return;

  const now = Date.now();
  const prevSchedule = APP_STATE.userProgress.flashcardSchedule[card.id] || {};

  // 1. Update card schedule
  APP_STATE.userProgress.flashcardSchedule[card.id] = {
    due: now + intervalConfig.ms,
    intervalMs: intervalConfig.ms,
    intervalLabel: intervalConfig.label,
    lastRating: rating,
    lastReviewed: now,
    reps: (prevSchedule.reps || 0) + 1,
    lapses: rating === 'again' ? (prevSchedule.lapses || 0) + 1 : (prevSchedule.lapses || 0)
  };

  // 2. Update feedback statistics
  const fb = APP_STATE.userProgress.flashcardFeedback;
  fb[rating] = (fb[rating] || 0) + 1;
  fb.totalReviews = (fb.totalReviews || 0) + 1;
  fb.history = fb.history || [];
  fb.history.unshift({
    cardId: card.id,
    rating: rating,
    timestamp: now,
    intervalLabel: intervalConfig.label
  });
  if (fb.history.length > 100) fb.history.pop();

  // 3. Keep compatibility with existing mastered / needsReview stats
  if (rating === 'easy' || rating === 'good') {
    if (!APP_STATE.userProgress.flashcardStats.mastered.includes(card.id)) {
      APP_STATE.userProgress.flashcardStats.mastered.push(card.id);
    }
    const idx = APP_STATE.userProgress.flashcardStats.needsReview.indexOf(card.id);
    if (idx >= 0) APP_STATE.userProgress.flashcardStats.needsReview.splice(idx, 1);
  } else {
    if (!APP_STATE.userProgress.flashcardStats.needsReview.includes(card.id)) {
      APP_STATE.userProgress.flashcardStats.needsReview.push(card.id);
    }
    const idx = APP_STATE.userProgress.flashcardStats.mastered.indexOf(card.id);
    if (idx >= 0) APP_STATE.userProgress.flashcardStats.mastered.splice(idx, 1);
  }

  // 4. Save state
  saveUserProgress();

  // 5. Toast feedback
  const toastType = rating === 'again' ? 'info' : (rating === 'easy' || rating === 'good' ? 'success' : 'info');
  showToast(`${intervalConfig.title} : snooze pour ${intervalConfig.label}`, toastType);

  // 6. Advance Queue
  if (studyMode === 'spaced' && currentCategoryFilter === 'all-due') {
    // Card is now snoozed, remove from active due list
    activeFlashcardsList.splice(currentCardIndex, 1);
    if (currentCardIndex >= activeFlashcardsList.length) {
      currentCardIndex = 0;
    }
    renderFlashcard();
  } else {
    navigateFlashcards(1);
  }

  updateAnkiHeaderBadges();
}

/**
 * Navigate to Next or Previous Card
 */
function navigateFlashcards(delta) {
  if (activeFlashcardsList.length === 0) return;
  currentCardIndex = (currentCardIndex + delta + activeFlashcardsList.length) % activeFlashcardsList.length;
  renderFlashcard();
}

/**
 * Shuffle cards in current view
 */
function shuffleFlashcards() {
  activeFlashcardsList.sort(() => 0.5 - Math.random());
  currentCardIndex = 0;
  renderFlashcard();
  showToast("Cartes mélangées !", "info");
}

/**
 * Legacy wrappers for backward compatibility with existing tests/links
 */
function markCardMastered() {
  rateFlashcard('good');
}

function markCardNeedsReview() {
  rateFlashcard('again');
}

/**
 * Live Countdown to the next card due
 */
function startNextDueCountdown() {
  const cdEl = document.getElementById('fc-next-due-countdown');
  if (!cdEl || !APP_STATE.flashcardsData) return;

  function update() {
    const schedules = Object.values(APP_STATE.userProgress.flashcardSchedule || {});
    const futureDue = schedules
      .map(s => s.due)
      .filter(d => d > Date.now())
      .sort((a, b) => a - b);

    if (futureDue.length === 0) {
      cdEl.textContent = "Toutes les cartes révisées !";
      return;
    }

    const diffMs = futureDue[0] - Date.now();
    if (diffMs <= 0) {
      cdEl.textContent = "Une carte est prête !";
      filterFlashcards('all-due');
      return;
    }

    const sec = Math.floor(diffMs / 1000) % 60;
    const min = Math.floor(diffMs / (1000 * 60)) % 60;
    const hours = Math.floor(diffMs / (1000 * 60 * 60));

    let str = "";
    if (hours > 0) str += `${hours}h `;
    str += `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
    cdEl.textContent = `Prochaine carte disponible dans : ${str}`;
  }

  update();
  countdownIntervalId = setInterval(update, 1000);
}

/**
 * Review ahead: bypass snooze to review all cards early
 */
function reviewAhead() {
  studyMode = 'browse';
  updateStudyModeButton();
  filterFlashcards('all');
  showToast("Mode révision anticipée activé", "info");
}

/**
 * Switch back to Free Mode
 */
function switchToFreeMode() {
  studyMode = 'browse';
  updateStudyModeButton();
  filterFlashcards('all');
}

/**
 * Toggle between Spaced Repetition Mode and Free Navigation Mode
 */
function toggleStudyMode() {
  studyMode = (studyMode === 'spaced') ? 'browse' : 'spaced';
  updateStudyModeButton();
  if (studyMode === 'spaced') {
    filterFlashcards('all-due');
    showToast("Mode Répétition Espacée activé (Anki)", "info");
  } else {
    filterFlashcards('all');
    showToast("Mode Consultation Libre activé (Toutes les cartes)", "info");
  }
}

function updateStudyModeButton() {
  const btn = document.getElementById('fc-mode-toggle');
  const txt = document.getElementById('fc-mode-text');
  if (!btn || !txt) return;

  if (studyMode === 'spaced') {
    btn.classList.add('active');
    txt.textContent = "Mode Espacé (Anki)";
    btn.title = "Mode Répétition Espacée actif : révision prioritaire des cartes dues";
  } else {
    btn.classList.remove('active');
    txt.textContent = "Mode Consultation Libre";
    btn.title = "Mode Consultation Libre actif : toutes les cartes sont affichées";
  }
}

/**
 * Text-to-Speech audio pronunciation
 */
function pronounceCard() {
  const card = activeFlashcardsList[currentCardIndex];
  if (!card || !('speechSynthesis' in window)) return;

  const rawHtml = isCardFlipped ? card.back : card.front;
  const cleanText = stripHtmlTags(rawHtml);

  window.speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(cleanText);
  utter.lang = 'fr-FR';
  utter.rate = 0.95;

  const btn = isCardFlipped ? document.getElementById('fc-speak-back-btn') : document.getElementById('fc-speak-front-btn');
  if (btn) btn.classList.add('speaking');
  utter.onend = () => { if (btn) btn.classList.remove('speaking'); };
  utter.onerror = () => { if (btn) btn.classList.remove('speaking'); };

  window.speechSynthesis.speak(utter);
}

/**
 * Open AnkiDroid Retention & Statistics Modal
 */
function openFlashcardStatsModal() {
  const modal = document.getElementById('fc-stats-modal');
  if (!modal) return;

  const fb = APP_STATE.userProgress.flashcardFeedback || { again: 0, hard: 0, good: 0, easy: 0, totalReviews: 0 };
  const total = fb.totalReviews || 0;

  const pctAgain = total > 0 ? Math.round((fb.again / total) * 100) : 0;
  const pctHard = total > 0 ? Math.round((fb.hard / total) * 100) : 0;
  const pctGood = total > 0 ? Math.round((fb.good / total) * 100) : 0;
  const pctEasy = total > 0 ? Math.round((fb.easy / total) * 100) : 0;
  const retention = total > 0 ? Math.round(((fb.good + fb.easy) / total) * 100) : 0;

  document.getElementById('stat-total-reviews').textContent = total;
  document.getElementById('stat-retention-rate').textContent = `${retention}%`;

  document.getElementById('stat-count-again').textContent = `${fb.again} (${pctAgain}%)`;
  document.getElementById('stat-bar-again').style.width = `${pctAgain}%`;

  document.getElementById('stat-count-hard').textContent = `${fb.hard} (${pctHard}%)`;
  document.getElementById('stat-bar-hard').style.width = `${pctHard}%`;

  document.getElementById('stat-count-good').textContent = `${fb.good} (${pctGood}%)`;
  document.getElementById('stat-bar-good').style.width = `${pctGood}%`;

  document.getElementById('stat-count-easy').textContent = `${fb.easy} (${pctEasy}%)`;
  document.getElementById('stat-bar-easy').style.width = `${pctEasy}%`;

  modal.classList.add('active');
}

function closeFlashcardStatsModal() {
  const modal = document.getElementById('fc-stats-modal');
  if (modal) modal.classList.remove('active');
}

/**
 * Keyboard shortcuts (Space: Flip / Good, 1: Again, 2: Hard, 3: Good, 4: Easy)
 */
function bindKeyboardShortcuts() {
  if (window._flashcardsKeyboardBound) return;
  window._flashcardsKeyboardBound = true;

  document.addEventListener('keydown', (e) => {
    if (APP_STATE.currentTab !== 'flashcards') return;
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;

    if (e.code === 'Space' || e.code === 'Enter') {
      e.preventDefault();
      if (!isCardFlipped) {
        flipCard();
      } else {
        rateFlashcard('good');
      }
    } else if (e.key === '1') {
      e.preventDefault();
      if (isCardFlipped) rateFlashcard('again');
      else flipCard();
    } else if (e.key === '2') {
      e.preventDefault();
      if (isCardFlipped) rateFlashcard('hard');
    } else if (e.key === '3') {
      e.preventDefault();
      if (isCardFlipped) rateFlashcard('good');
    } else if (e.key === '4') {
      e.preventDefault();
      if (isCardFlipped) rateFlashcard('easy');
    } else if (e.code === 'ArrowRight') {
      e.preventDefault();
      navigateFlashcards(1);
    } else if (e.code === 'ArrowLeft') {
      e.preventDefault();
      navigateFlashcards(-1);
    } else if (e.key === 'r' || e.key === 'R') {
      e.preventDefault();
      pronounceCard();
    }
  });
}

// Global Exports
window.initFlashcardsView = initFlashcardsView;
window.flipCard = flipCard;
window.rateFlashcard = rateFlashcard;
window.navigateFlashcards = navigateFlashcards;
window.shuffleFlashcards = shuffleFlashcards;
window.markCardMastered = markCardMastered;
window.markCardNeedsReview = markCardNeedsReview;
window.pronounceCard = pronounceCard;
window.filterFlashcards = filterFlashcards;
window.toggleStudyMode = toggleStudyMode;
window.reviewAhead = reviewAhead;
window.switchToFreeMode = switchToFreeMode;
window.openFlashcardStatsModal = openFlashcardStatsModal;
window.closeFlashcardStatsModal = closeFlashcardStatsModal;
