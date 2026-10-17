/**
 * LIVRET DU CITOYEN 2026 - Quiz & Examen Civique Engine
 * Supports Examen Blanc 2026 (40 questions, 45 min timer), Module Quizzes, and Instant Practice.
 */

let activeQuizSession = {
  isExamMode: false,
  title: "",
  questions: [],
  currentIndex: 0,
  userAnswers: {}, // { questionIndex: selectedOptionIndex }
  timerSecondsLeft: 0,
  timerInterval: null
};

function initQuizHub() {
  if (!APP_STATE.quizzesData) return;
  renderQuizzesList();
}

// Render available quizzes cards in the hub
function renderQuizzesList() {
  const container = document.getElementById('quizzes-cards-grid');
  if (!container || !APP_STATE.quizzesData) return;

  container.innerHTML = APP_STATE.quizzesData.modules.map(quiz => {
    const savedScore = APP_STATE.userProgress.quizScores[quiz.id];

    return `
      <div class="quiz-card">
        <div>
          <div class="quiz-card-header">
            <span class="quiz-category-tag">Module ${quiz.category.replace('module-', '')}</span>
            <span class="quiz-score-badge">
              ${savedScore ? `Meilleur score : <strong style="color:var(--success);">${savedScore.bestScore}/${quiz.questionCount}</strong>` : 'Non tenté'}
            </span>
          </div>
          <h4>${quiz.title}</h4>
          <p>${quiz.description}</p>
        </div>
        <div class="quiz-card-footer">
          <span style="font-size:0.85rem; color:var(--text-secondary);">
            <i class="fa-regular fa-circle-question"></i> ${quiz.questionCount} questions
          </span>
          <button class="btn-sm-primary" onclick="startModuleQuiz('${quiz.id}')">
            ${savedScore ? 'Recommencer' : 'Commencer'} <i class="fa-solid fa-play"></i>
          </button>
        </div>
      </div>
    `;
  }).join('');
}

// Start a Module Quiz
function startModuleQuiz(quizId) {
  const quiz = APP_STATE.quizzesData.modules.find(q => q.id === quizId);
  if (!quiz) return;

  // Retrieve questions from pool
  const qList = quiz.questionIds
    .map(qid => APP_STATE.quizzesData.questions.find(q => q.id === qid))
    .filter(Boolean);

  startQuizSession({
    isExamMode: false,
    title: quiz.title,
    quizId: quiz.id,
    questions: qList,
    timeLimitSeconds: 0 // No strict timer for training quiz
  });
}

// Start Official Examen Blanc 2026 (40 questions, 45 minutes)
function startMockExam2026() {
  if (!APP_STATE.quizzesData) return;

  // Shuffle and pick 40 questions from all questions pool
  const allPool = [...APP_STATE.quizzesData.questions];
  const shuffled = allPool.sort(() => 0.5 - Math.random());
  const examQuestions = shuffled.slice(0, 40);

  startQuizSession({
    isExamMode: true,
    title: "Examen Blanc Civique Officiel 2026",
    quizId: "examen-blanc-2026",
    questions: examQuestions,
    timeLimitSeconds: 45 * 60 // 45 minutes
  });
}

// Quick 10-Question Random Practice
function startQuickPractice() {
  if (!APP_STATE.quizzesData) return;

  const allPool = [...APP_STATE.quizzesData.questions];
  const shuffled = allPool.sort(() => 0.5 - Math.random());
  const practiceQuestions = shuffled.slice(0, 10);

  startQuizSession({
    isExamMode: false,
    title: "Entraînement Rapide (10 Questions)",
    quizId: "quick-practice",
    questions: practiceQuestions,
    timeLimitSeconds: 0
  });
}

// Launch Quiz Session & show runner interface
function startQuizSession(config) {
  activeQuizSession = {
    isExamMode: config.isExamMode,
    title: config.title,
    quizId: config.quizId,
    questions: config.questions,
    currentIndex: 0,
    userAnswers: {},
    timerSecondsLeft: config.timeLimitSeconds,
    timerInterval: null
  };

  // Hide Hub & Results, Show Active Quiz Container
  document.getElementById('quiz-hub-view').style.display = 'none';
  document.getElementById('quiz-results-container').classList.remove('active');
  const runner = document.getElementById('quiz-active-container');
  runner.classList.add('active');

  // Setup Timer if exam
  clearInterval(activeQuizSession.timerInterval);
  const timerBadge = document.getElementById('quiz-timer-display');
  if (config.timeLimitSeconds > 0) {
    timerBadge.style.display = 'inline-flex';
    updateTimerDisplay();
    activeQuizSession.timerInterval = setInterval(() => {
      activeQuizSession.timerSecondsLeft--;
      updateTimerDisplay();
      if (activeQuizSession.timerSecondsLeft <= 0) {
        clearInterval(activeQuizSession.timerInterval);
        submitQuizSession();
        showToast("Temps écoulé ! Votre examen a été soumis.", "info");
      }
    }, 1000);
  } else {
    timerBadge.style.display = 'none';
  }

  renderCurrentQuestion();
  window.scrollTo({ top: 100, behavior: 'smooth' });
}

function updateTimerDisplay() {
  const timerEl = document.getElementById('quiz-timer-text');
  if (!timerEl) return;
  const m = Math.floor(activeQuizSession.timerSecondsLeft / 60);
  const s = activeQuizSession.timerSecondsLeft % 60;
  timerEl.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

// Render the active question in runner
function renderCurrentQuestion() {
  const q = activeQuizSession.questions[activeQuizSession.currentIndex];
  if (!q) return;

  // Header Title & Counter
  document.getElementById('quiz-session-title').textContent = activeQuizSession.title;
  document.getElementById('quiz-question-counter').textContent = 
    `Question ${activeQuizSession.currentIndex + 1} sur ${activeQuizSession.questions.length}`;

  // Question Text
  document.getElementById('quiz-question-text').textContent = q.question;

  // Options
  const letters = ['A', 'B', 'C', 'D'];
  const optionsContainer = document.getElementById('quiz-options-container');
  const selectedIdx = activeQuizSession.userAnswers[activeQuizSession.currentIndex];
  const hasAnswered = selectedIdx !== undefined;

  optionsContainer.innerHTML = q.options.map((opt, i) => {
    let classes = "quiz-option-btn";
    if (hasAnswered) {
      if (i === selectedIdx) classes += " selected";
      // In training mode, reveal immediate feedback
      if (!activeQuizSession.isExamMode) {
        if (i === q.answerIndex) classes += " correct";
        else if (i === selectedIdx) classes += " wrong";
      }
    }

    return `
      <button class="${classes}" onclick="selectQuizOption(${i})" ${hasAnswered && !activeQuizSession.isExamMode ? 'disabled' : ''}>
        <span class="option-letter">${letters[i]}</span>
        <span>${opt}</span>
      </button>
    `;
  }).join('');

  // Explanation box (Training mode only)
  const explanationBox = document.getElementById('quiz-explanation-display');
  if (!activeQuizSession.isExamMode && hasAnswered) {
    explanationBox.innerHTML = `
      <strong><i class="fa-solid fa-book-open"></i> Explication officielle :</strong><br>
      ${q.explanation}
    `;
    explanationBox.classList.add('show');
  } else {
    explanationBox.classList.remove('show');
  }

  // Footer Navigation Buttons
  const prevBtn = document.getElementById('btn-quiz-prev');
  const nextBtn = document.getElementById('btn-quiz-next');
  const submitBtn = document.getElementById('btn-quiz-submit');

  prevBtn.style.display = activeQuizSession.currentIndex > 0 ? 'inline-flex' : 'none';

  const isLast = activeQuizSession.currentIndex === activeQuizSession.questions.length - 1;
  nextBtn.style.display = isLast ? 'none' : 'inline-flex';
  submitBtn.style.display = isLast ? 'inline-flex' : 'none';
}

function selectQuizOption(index) {
  activeQuizSession.userAnswers[activeQuizSession.currentIndex] = index;
  renderCurrentQuestion();
}

function navigateQuiz(delta) {
  const newIndex = activeQuizSession.currentIndex + delta;
  if (newIndex >= 0 && newIndex < activeQuizSession.questions.length) {
    activeQuizSession.currentIndex = newIndex;
    renderCurrentQuestion();
  }
}

// Submit and compute results
function submitQuizSession() {
  clearInterval(activeQuizSession.timerInterval);

  let correctCount = 0;
  activeQuizSession.questions.forEach((q, idx) => {
    if (activeQuizSession.userAnswers[idx] === q.answerIndex) {
      correctCount++;
    }
  });

  const total = activeQuizSession.questions.length;
  const percentage = Math.round((correctCount / total) * 100);
  const isPassed = percentage >= 80;

  // Record in LocalStorage Progress
  if (activeQuizSession.quizId === 'examen-blanc-2026') {
    APP_STATE.userProgress.examAttempts.push({
      score: correctCount,
      total: total,
      percentage: percentage,
      passed: isPassed,
      date: new Date().toLocaleDateString('fr-FR')
    });
  } else if (activeQuizSession.quizId.startsWith('quiz-')) {
    const existing = APP_STATE.userProgress.quizScores[activeQuizSession.quizId] || { bestScore: 0 };
    APP_STATE.userProgress.quizScores[activeQuizSession.quizId] = {
      bestScore: Math.max(existing.bestScore, correctCount),
      total: total,
      percentage: percentage,
      passed: isPassed,
      date: new Date().toLocaleDateString('fr-FR')
    };
  }

  saveUserProgress();

  // Hide Runner, Show Results View
  document.getElementById('quiz-active-container').classList.remove('active');
  const resultsContainer = document.getElementById('quiz-results-container');
  resultsContainer.classList.add('active');

  // Populate Results View
  document.getElementById('results-score-text').textContent = correctCount;
  document.getElementById('results-total-text').textContent = `/ ${total} (${percentage}%)`;

  const verdictEl = document.getElementById('results-verdict-text');
  const descEl = document.getElementById('results-desc-text');

  if (isPassed) {
    verdictEl.textContent = "FÉLICITATIONS ! EXAMEN RÉUSSI 🇫🇷";
    verdictEl.className = "results-verdict pass";
    descEl.textContent = `Vous avez obtenu un score de ${percentage}%, supérieur au seuil d'exigence de 80%. Vos connaissances des principes, de l'histoire et de la société françaises sont solides pour l'entretien !`;
  } else {
    verdictEl.textContent = "SCORE INSUFFISANT (À RETRAVAILLER)";
    verdictEl.className = "results-verdict fail";
    descEl.textContent = `Vous avez obtenu ${percentage}%. Le seuil requis pour l'examen civique est de 80% (32/40). Prenez le temps de revoir les chapitres correspondants dans le cours et retentez votre chance !`;
  }

  // Render question review breakdown
  const reviewContainer = document.getElementById('results-questions-review');
  if (reviewContainer) {
    reviewContainer.innerHTML = activeQuizSession.questions.map((q, idx) => {
      const userChoice = activeQuizSession.userAnswers[idx];
      const isRight = userChoice === q.answerIndex;

      return `
        <div style="text-align:left; background:var(--bg-tertiary); border-radius:12px; padding:1.25rem; margin-bottom:1rem; border-left:4px solid ${isRight ? 'var(--success)' : 'var(--danger)'};">
          <div style="font-weight:700; margin-bottom:0.5rem; color:var(--text-primary);">
            Question ${idx + 1} : ${q.question}
          </div>
          <div style="font-size:0.9rem; margin-bottom:0.25rem;">
            Votre réponse : <strong style="color:${isRight ? 'var(--success)' : 'var(--danger)'};">
              ${userChoice !== undefined ? q.options[userChoice] : 'Non répondue'}
            </strong>
          </div>
          ${!isRight ? `
            <div style="font-size:0.9rem; color:var(--success); margin-bottom:0.5rem;">
              Bonne réponse : <strong>${q.options[q.answerIndex]}</strong>
            </div>
          ` : ''}
          <div style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5; font-style:italic; margin-top:0.4rem;">
            ${q.explanation}
          </div>
        </div>
      `;
    }).join('');
  }

  window.scrollTo({ top: 100, behavior: 'smooth' });
}

// Exit quiz results back to Hub
function exitQuizToHub() {
  document.getElementById('quiz-results-container').classList.remove('active');
  document.getElementById('quiz-active-container').classList.remove('active');
  document.getElementById('quiz-hub-view').style.display = 'flex';
  renderQuizzesList();
  window.scrollTo({ top: 100, behavior: 'smooth' });
}

window.initQuizHub = initQuizHub;
window.startModuleQuiz = startModuleQuiz;
window.startMockExam2026 = startMockExam2026;
window.startQuickPractice = startQuickPractice;
window.selectQuizOption = selectQuizOption;
window.navigateQuiz = navigateQuiz;
window.submitQuizSession = submitQuizSession;
window.exitQuizToHub = exitQuizToHub;
