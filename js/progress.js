/**
 * LIVRET DU CITOYEN 2026 - Analytics & Progress Dashboard
 * Displays in-depth tracking metrics, exam history, data export/import and reset tools.
 */

function renderProgressDashboard() {
  if (!APP_STATE.courseData) return;

  const score = calculateReadinessScore();

  // Progress gauge
  const progressText = document.getElementById('prog-readiness-percent');
  const progressBar = document.getElementById('prog-readiness-bar');
  const verdictBadge = document.getElementById('prog-verdict-badge');

  if (progressText) progressText.textContent = `${score}%`;
  if (progressBar) progressBar.style.width = `${score}%`;

  if (verdictBadge) {
    if (score >= 80) {
      verdictBadge.innerHTML = '<span class="module-card-status completed"><i class="fa-solid fa-circle-check"></i> Prêt pour l\'entretien officiel</span>';
    } else if (score >= 50) {
      verdictBadge.innerHTML = '<span class="module-card-status in-progress"><i class="fa-solid fa-spinner"></i> Bon niveau en progression</span>';
    } else {
      verdictBadge.innerHTML = '<span class="module-card-status not-started"><i class="fa-solid fa-circle"></i> Début de parcours</span>';
    }
  }

  // Summary Metrics
  let totalChapters = 0;
  APP_STATE.courseData.modules.forEach(m => totalChapters += m.chapters.length);
  const chaptersRead = APP_STATE.userProgress.completedChapters.length;
  document.getElementById('prog-stat-chapters').textContent = `${chaptersRead} / ${totalChapters}`;

  let passedQuizzes = 0;
  for (const qid in APP_STATE.userProgress.quizScores) {
    if (APP_STATE.userProgress.quizScores[qid].passed) passedQuizzes++;
  }
  const totalQuizzes = APP_STATE.quizzesData ? APP_STATE.quizzesData.modules.length : 5;
  document.getElementById('prog-stat-quizzes').textContent = `${passedQuizzes} / ${totalQuizzes}`;

  const masteredCards = APP_STATE.userProgress.flashcardStats.mastered.length;
  const totalCards = APP_STATE.flashcardsData ? APP_STATE.flashcardsData.cards.length : 52;
  document.getElementById('prog-stat-flashcards').textContent = `${masteredCards} / ${totalCards}`;

  const examPassed = APP_STATE.userProgress.examAttempts.filter(e => e.passed).length;
  document.getElementById('prog-stat-exams').textContent = `${examPassed} réussi(s)`;

  // Render Detailed Module Table
  const tableBody = document.getElementById('prog-modules-table-body');
  if (tableBody) {
    tableBody.innerHTML = APP_STATE.courseData.modules.map(mod => {
      const modChapterIds = mod.chapters.map(c => c.id);
      const doneCount = modChapterIds.filter(id => APP_STATE.userProgress.completedChapters.includes(id)).length;
      const pct = Math.round((doneCount / mod.chapters.length) * 100);

      // Corresponding quiz
      const quizId = `quiz-m${mod.number}`;
      const qScore = APP_STATE.userProgress.quizScores[quizId];

      return `
        <tr>
          <td><strong>Module ${mod.number}</strong> : ${mod.title}</td>
          <td>
            <div style="display:flex; align-items:center; gap:0.5rem;">
              <span>${doneCount} / ${mod.chapters.length} (${pct}%)</span>
              <div class="progress-bar-container" style="width:70px; height:6px;">
                <div class="progress-bar-fill" style="width:${pct}%;"></div>
              </div>
            </div>
          </td>
          <td>
            ${qScore ? `
              <span style="font-weight:700; color:${qScore.passed ? 'var(--success)' : 'var(--danger)'};">
                ${qScore.bestScore} / ${qScore.total} (${qScore.percentage}%)
              </span>
            ` : '<span style="color:var(--text-muted);">Non passé</span>'}
          </td>
          <td>
            ${doneCount === mod.chapters.length ? 
              '<span class="badge-pill" style="background:var(--success-bg); color:var(--success);"><i class="fa-solid fa-check"></i> Complété</span>' : 
              (doneCount > 0 ? '<span class="badge-pill" style="background:var(--warning-bg); color:var(--warning);">En cours</span>' : '<span class="badge-pill">À faire</span>')
            }
          </td>
        </tr>
      `;
    }).join('');
  }

  // Render Exam History Table
  const examTableBody = document.getElementById('prog-exams-table-body');
  if (examTableBody) {
    if (APP_STATE.userProgress.examAttempts.length === 0) {
      examTableBody.innerHTML = `
        <tr>
          <td colspan="5" style="text-align:center; color:var(--text-muted); padding:1.5rem;">
            Aucun examen blanc officiel passé pour le moment.
          </td>
        </tr>
      `;
    } else {
      examTableBody.innerHTML = APP_STATE.userProgress.examAttempts.map((att, idx) => `
        <tr>
          <td>Tentative #${idx + 1}</td>
          <td>${att.date}</td>
          <td><strong>${att.score} / ${att.total}</strong></td>
          <td>${att.percentage}%</td>
          <td>
            ${att.passed ? 
              '<span style="color:var(--success); font-weight:700;"><i class="fa-solid fa-circle-check"></i> Admis (≥ 80%)</span>' : 
              '<span style="color:var(--danger); font-weight:700;"><i class="fa-solid fa-circle-xmark"></i> Non admis (< 80%)</span>'}
          </td>
        </tr>
      `).join('');
    }
  }
}

// Export progress as JSON file
function exportProgress() {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(APP_STATE.userProgress, null, 2));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", `citoyen_2026_sauvegarde_${new Date().toISOString().slice(0, 10)}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
  showToast("Progression exportée avec succès !", "success");
}

// Import progress from JSON file
function triggerImportFile() {
  const input = document.getElementById('prog-import-input');
  if (input) input.click();
}

function handleImportFile(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = (e) => {
    try {
      const parsed = JSON.parse(e.target.result);
      if (parsed && typeof parsed === 'object') {
        APP_STATE.userProgress = Object.assign(APP_STATE.userProgress, parsed);
        saveUserProgress();
        renderProgressDashboard();
        showToast("Progression importée avec succès !", "success");
      }
    } catch (err) {
      console.error(err);
      showToast("Format de fichier JSON invalide", "info");
    }
  };
  reader.readAsText(file);
}

// Reset all progress
function resetAllProgress() {
  if (confirm("Êtes-vous certain de vouloir réinitialiser l'ensemble de votre progression ? Cette action est irréversible.")) {
    APP_STATE.userProgress = {
      completedChapters: [],
      quizScores: {},
      examAttempts: [],
      flashcardStats: { mastered: [], needsReview: [] },
      checklist: {}
    };
    saveUserProgress();
    renderProgressDashboard();
    showToast("Progression réinitialisée à zéro.", "info");
  }
}

window.renderProgressDashboard = renderProgressDashboard;
window.exportProgress = exportProgress;
window.triggerImportFile = triggerImportFile;
window.handleImportFile = handleImportFile;
window.resetAllProgress = resetAllProgress;
