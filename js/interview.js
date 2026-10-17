/**
 * LIVRET DU CITOYEN 2026 - Interview Simulator & Preparation Checklist
 * Simulates prefecture naturalization interview with examiner guidance and model answers.
 */

let currentInterviewIndex = 0;
let isAnswerRevealed = false;

function initInterviewView() {
  if (!APP_STATE.interviewData) return;
  renderInterviewQuestion();
  renderChecklist();
  renderAdviceList();
}

function renderInterviewQuestion() {
  const container = document.getElementById('interview-qa-container');
  if (!container || !APP_STATE.interviewData) return;

  const questions = APP_STATE.interviewData.questions;
  if (!questions || questions.length === 0) return;

  const q = questions[currentInterviewIndex];
  isAnswerRevealed = false;

  document.getElementById('sim-category-badge').textContent = q.category;
  document.getElementById('sim-counter-text').textContent = `Question ${currentInterviewIndex + 1} / ${questions.length}`;
  document.getElementById('sim-question-text').textContent = q.question;
  document.getElementById('sim-intent-text').textContent = `Intention de l'agent : ${q.intent}`;

  // Reset practice text
  const noteKey = `interview_note_${q.id}`;
  const savedNote = localStorage.getItem(noteKey) || '';
  const textarea = document.getElementById('sim-user-notes');
  if (textarea) textarea.value = savedNote;

  // Reveal box
  const revealBox = document.getElementById('sim-answer-reveal-box');
  if (revealBox) {
    revealBox.classList.remove('show');
    document.getElementById('sim-model-answer-text').textContent = q.modelAnswer;

    // Dos & Don'ts
    const dosList = document.getElementById('sim-dos-list');
    const dontsList = document.getElementById('sim-donts-list');
    if (dosList) dosList.innerHTML = q.dos.map(d => `<li>✓ ${d}</li>`).join('');
    if (dontsList) dontsList.innerHTML = q.donts.map(d => `<li>✗ ${d}</li>`).join('');
  }

  const revealBtnLabel = document.getElementById('sim-reveal-btn-label');
  if (revealBtnLabel) revealBtnLabel.textContent = "Révéler la réponse type & conseils";
}

function toggleRevealAnswer() {
  const revealBox = document.getElementById('sim-answer-reveal-box');
  const revealBtnLabel = document.getElementById('sim-reveal-btn-label');
  if (!revealBox) return;

  isAnswerRevealed = !isAnswerRevealed;
  revealBox.classList.toggle('show', isAnswerRevealed);
  if (revealBtnLabel) {
    revealBtnLabel.textContent = isAnswerRevealed ? "Masquer la réponse type" : "Révéler la réponse type & conseils";
  }
}

function navigateInterview(delta) {
  const questions = APP_STATE.interviewData.questions;
  if (!questions || questions.length === 0) return;

  // Save current note
  saveInterviewNote();

  currentInterviewIndex = (currentInterviewIndex + delta + questions.length) % questions.length;
  renderInterviewQuestion();
  window.scrollTo({ top: 120, behavior: 'smooth' });
}

function saveInterviewNote() {
  const q = APP_STATE.interviewData.questions[currentInterviewIndex];
  const textarea = document.getElementById('sim-user-notes');
  if (q && textarea) {
    localStorage.setItem(`interview_note_${q.id}`, textarea.value);
  }
}

// Pronounce the interview question
function pronounceInterviewQuestion() {
  const q = APP_STATE.interviewData.questions[currentInterviewIndex];
  if (!q || !('speechSynthesis' in window)) return;

  const utter = new SpeechSynthesisUtterance(q.question);
  utter.lang = 'fr-FR';
  utter.rate = 0.95;
  window.speechSynthesis.speak(utter);
}

// Render personal checklist for the interview
const DEFAULT_CHECKLIST = [
  { id: "chk-1", text: "Je connais le nom du maire de ma commune" },
  { id: "chk-2", text: "Je connais le nom du préfet de mon département" },
  { id: "chk-3", text: "Je sais expliquer clairement pourquoi je veux être français(e)" },
  { id: "chk-4", text: "Je connais la devise et ses 3 valeurs dans ma vie" },
  { id: "chk-5", text: "Je maîtrise les 4 principes (Indivisible, Laïque, Démocratique, Sociale)" },
  { id: "chk-6", text: "Je connais le nom du Président et du Premier ministre actuels" },
  { id: "chk-7", text: "Je peux citer 3 rois, 3 présidents et 3 fleuves de France" },
  { id: "chk-8", text: "Je connais les numéros d'urgence (15, 17, 18, 112)" },
  { id: "chk-9", text: "Tous mes documents originaux sont classés et prêts" },
  { id: "chk-10", text: "Je me suis entraîné(e) à parler posément en français niveau B2" }
];

function renderChecklist() {
  const container = document.getElementById('interview-checklist-container');
  if (!container) return;

  container.innerHTML = DEFAULT_CHECKLIST.map(item => {
    const isChecked = Boolean(APP_STATE.userProgress.checklist[item.id]);

    return `
      <label class="checklist-item">
        <input type="checkbox" id="${item.id}" ${isChecked ? 'checked' : ''} onchange="toggleChecklistItem('${item.id}')">
        <span style="${isChecked ? 'text-decoration: line-through; opacity: 0.7;' : ''}">${item.text}</span>
      </label>
    `;
  }).join('');
}

function toggleChecklistItem(itemId) {
  APP_STATE.userProgress.checklist[itemId] = !APP_STATE.userProgress.checklist[itemId];
  saveUserProgress();
  renderChecklist();
}

function renderAdviceList() {
  const container = document.getElementById('interview-advice-container');
  if (!container || !APP_STATE.interviewData) return;

  container.innerHTML = APP_STATE.interviewData.advice.map(adv => `
    <div style="background:var(--bg-tertiary); border-radius:10px; padding:1rem; margin-bottom:0.75rem;">
      <h6 style="font-weight:700; color:var(--fr-blue); font-size:0.9rem; margin-bottom:0.25rem;">
        <i class="fa-solid fa-circle-check"></i> ${adv.title}
      </h6>
      <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.4;">${adv.text}</p>
    </div>
  `).join('');
}

window.initInterviewView = initInterviewView;
window.toggleRevealAnswer = toggleRevealAnswer;
window.navigateInterview = navigateInterview;
window.saveInterviewNote = saveInterviewNote;
window.pronounceInterviewQuestion = pronounceInterviewQuestion;
window.toggleChecklistItem = toggleChecklistItem;
