/**
 * LIVRET DU CITOYEN 2026 - 3D Flashcards Engine
 * Features: 3D perspective flip, Spaced Repetition (Mastered vs Review), Category filtering, Audio speech.
 */

let activeFlashcardsList = [];
let currentCardIndex = 0;
let isCardFlipped = false;
let currentCategoryFilter = "all";

function initFlashcardsView() {
  if (!APP_STATE.flashcardsData) return;
  setupCategoryFilter();
  filterFlashcards(currentCategoryFilter);
  bindKeyboardShortcuts();
}

// Populate Category Filter Dropdown
function setupCategoryFilter() {
  const select = document.getElementById('flashcard-category-select');
  if (!select || !APP_STATE.flashcardsData) return;

  const cats = APP_STATE.flashcardsData.categories;
  select.innerHTML = `
    <option value="all">Toutes les thématiques (${APP_STATE.flashcardsData.totalCards} cartes)</option>
    <option value="needs-review">⚠️ Cartes à revoir uniquement</option>
    <option value="mastered">✓ Cartes maîtrisées</option>
    ${cats.map(c => `<option value="${c}">${c}</option>`).join('')}
  `;

  select.value = currentCategoryFilter;
  select.onchange = (e) => filterFlashcards(e.target.value);
}

// Filter cards based on selection
function filterFlashcards(category) {
  currentCategoryFilter = category;
  const allCards = APP_STATE.flashcardsData.cards;

  if (category === 'all') {
    activeFlashcardsList = [...allCards];
  } else if (category === 'needs-review') {
    activeFlashcardsList = allCards.filter(c => APP_STATE.userProgress.flashcardStats.needsReview.includes(c.id));
  } else if (category === 'mastered') {
    activeFlashcardsList = allCards.filter(c => APP_STATE.userProgress.flashcardStats.mastered.includes(c.id));
  } else {
    activeFlashcardsList = allCards.filter(c => c.category === category);
  }

  currentCardIndex = 0;
  isCardFlipped = false;
  renderFlashcard();
}

// Render active flashcard
function renderFlashcard() {
  const cardElement = document.getElementById('main-flashcard-3d');
  const counterElement = document.getElementById('flashcard-counter-badge');
  const emptyState = document.getElementById('flashcards-empty-state');
  const sceneWrapper = document.getElementById('flashcard-scene-wrapper');

  if (!cardElement) return;

  // If filtered list is empty
  if (activeFlashcardsList.length === 0) {
    if (sceneWrapper) sceneWrapper.style.display = 'none';
    if (emptyState) emptyState.style.display = 'block';
    if (counterElement) counterElement.textContent = "0 / 0";
    return;
  }

  if (sceneWrapper) sceneWrapper.style.display = 'block';
  if (emptyState) emptyState.style.display = 'none';

  const card = activeFlashcardsList[currentCardIndex];
  if (!card) return;

  // Unflip first
  cardElement.classList.remove('flipped');
  isCardFlipped = false;

  // Populate Front
  document.getElementById('fc-front-category').textContent = card.category;
  document.getElementById('fc-front-tag').textContent = card.tag || "";
  document.getElementById('fc-front-text').textContent = card.front;

  // Populate Back
  document.getElementById('fc-back-category').textContent = card.category;
  document.getElementById('fc-back-tag').textContent = card.tag || "";
  document.getElementById('fc-back-text').textContent = card.back;
  document.getElementById('fc-back-tip-text').textContent = card.tip || "Point clé attendu lors de l'entretien.";

  // Update Status Badge
  const isMastered = APP_STATE.userProgress.flashcardStats.mastered.includes(card.id);
  const isNeedsReview = APP_STATE.userProgress.flashcardStats.needsReview.includes(card.id);

  const statusPill = document.getElementById('fc-mastery-status');
  if (statusPill) {
    if (isMastered) {
      statusPill.innerHTML = '<span style="color:var(--success); font-weight:700;"><i class="fa-solid fa-circle-check"></i> Maîtrisée</span>';
    } else if (isNeedsReview) {
      statusPill.innerHTML = '<span style="color:var(--danger); font-weight:700;"><i class="fa-solid fa-triangle-exclamation"></i> À revoir</span>';
    } else {
      statusPill.innerHTML = '<span style="color:var(--text-muted);"><i class="fa-regular fa-circle"></i> En cours</span>';
    }
  }

  // Counter
  if (counterElement) {
    counterElement.textContent = `${currentCardIndex + 1} / ${activeFlashcardsList.length}`;
  }
}

// Flip Card Action
function flipCard() {
  const cardElement = document.getElementById('main-flashcard-3d');
  if (cardElement) {
    isCardFlipped = !isCardFlipped;
    cardElement.classList.toggle('flipped', isCardFlipped);
  }
}

// Next / Previous Navigation
function navigateFlashcards(delta) {
  if (activeFlashcardsList.length === 0) return;
  currentCardIndex = (currentCardIndex + delta + activeFlashcardsList.length) % activeFlashcardsList.length;
  renderFlashcard();
}

// Shuffle Cards
function shuffleFlashcards() {
  activeFlashcardsList.sort(() => 0.5 - Math.random());
  currentCardIndex = 0;
  renderFlashcard();
  showToast("Cartes mélangées !", "info");
}

// Mark as Mastered
function markCardMastered() {
  const card = activeFlashcardsList[currentCardIndex];
  if (!card) return;

  // Add to mastered, remove from needsReview
  if (!APP_STATE.userProgress.flashcardStats.mastered.includes(card.id)) {
    APP_STATE.userProgress.flashcardStats.mastered.push(card.id);
  }
  const reviewIdx = APP_STATE.userProgress.flashcardStats.needsReview.indexOf(card.id);
  if (reviewIdx >= 0) APP_STATE.userProgress.flashcardStats.needsReview.splice(reviewIdx, 1);

  saveUserProgress();
  showToast("Carte validée comme maîtrisée ✓", "success");
  navigateFlashcards(1);
}

// Mark as Needs Review
function markCardNeedsReview() {
  const card = activeFlashcardsList[currentCardIndex];
  if (!card) return;

  // Add to needsReview, remove from mastered
  if (!APP_STATE.userProgress.flashcardStats.needsReview.includes(card.id)) {
    APP_STATE.userProgress.flashcardStats.needsReview.push(card.id);
  }
  const masteredIdx = APP_STATE.userProgress.flashcardStats.mastered.indexOf(card.id);
  if (masteredIdx >= 0) APP_STATE.userProgress.flashcardStats.mastered.splice(masteredIdx, 1);

  saveUserProgress();
  showToast("Carte marquée à revoir ⚠️", "info");
  navigateFlashcards(1);
}

// Voice Pronunciation of Flashcard
function pronounceCard() {
  const card = activeFlashcardsList[currentCardIndex];
  if (!card || !('speechSynthesis' in window)) return;

  const text = isCardFlipped ? card.back : card.front;
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = 'fr-FR';
  utter.rate = 0.95;
  window.speechSynthesis.speak(utter);
}

// Keyboard shortcuts (Space: Flip, Arrows: Navigate)
function bindKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    if (APP_STATE.currentTab !== 'flashcards') return;
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    if (e.code === 'Space') {
      e.preventDefault();
      flipCard();
    } else if (e.code === 'ArrowRight') {
      e.preventDefault();
      navigateFlashcards(1);
    } else if (e.code === 'ArrowLeft') {
      e.preventDefault();
      navigateFlashcards(-1);
    }
  });
}

window.initFlashcardsView = initFlashcardsView;
window.flipCard = flipCard;
window.navigateFlashcards = navigateFlashcards;
window.shuffleFlashcards = shuffleFlashcards;
window.markCardMastered = markCardMastered;
window.markCardNeedsReview = markCardNeedsReview;
window.pronounceCard = pronounceCard;
