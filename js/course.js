/**
 * LIVRET DU CITOYEN 2026 - Modular Course Viewer & Reader
 * Handles sidebar hierarchy, chapter rendering, audio text-to-speech, and progress toggling.
 */

let currentModuleId = "module-1";
let currentChapterId = "m1-c1";
let isSpeaking = false;
let speechUtterance = null;

function initCourseView() {
  if (!APP_STATE.courseData) return;
  renderCourseSidebar();
  renderChapter(currentModuleId, currentChapterId);
  setupCourseSearch();
}

// Render Accordion Sidebar
function renderCourseSidebar(filterQuery = "") {
  const container = document.getElementById('course-modules-accordion');
  if (!container || !APP_STATE.courseData) return;

  const query = filterQuery.toLowerCase().trim();

  container.innerHTML = APP_STATE.courseData.modules.map(mod => {
    // Filter chapters if search query
    const filteredChapters = mod.chapters.filter(ch => {
      if (!query) return true;
      return ch.title.toLowerCase().includes(query) || 
             ch.highlights.some(h => h.toLowerCase().includes(query));
    });

    if (query && filteredChapters.length === 0) return "";

    const isOpen = mod.id === currentModuleId || query.length > 0;

    return `
      <div class="module-accordion-item" data-mod-id="${mod.id}">
        <button class="module-accordion-header ${isOpen ? 'open' : ''} ${mod.id === currentModuleId ? 'active' : ''}" onclick="toggleModuleAccordion('${mod.id}')">
          <div class="accordion-title-wrap">
            <i class="fa-solid ${mod.icon}"></i>
            <span>Module ${mod.number}: ${mod.title}</span>
          </div>
          <i class="fa-solid fa-chevron-right accordion-chevron"></i>
        </button>
        <div class="module-chapters-list ${isOpen ? 'open' : ''}" id="chapters-list-${mod.id}">
          ${filteredChapters.map(chap => {
            const isRead = APP_STATE.userProgress.completedChapters.includes(chap.id);
            const isCurrent = chap.id === currentChapterId;

            return `
              <button class="chapter-nav-item ${isCurrent ? 'active' : ''}" onclick="selectChapter('${mod.id}', '${chap.id}')">
                <span style="display:flex; align-items:center; gap:0.4rem;">
                  ${chap.id === 'm1-c1' ? '<i class="fa-solid fa-circle-play" style="color:var(--fr-gold); font-size:0.75rem;" title="Capsule Vidéo E-Learning Disponible"></i>' : ''}
                  ${chap.title}
                </span>
                <span class="chapter-status-dot ${isRead ? 'completed' : ''}" title="${isRead ? 'Chapitre lu' : 'Non lu'}"></span>
              </button>
            `;
          }).join('')}
        </div>
      </div>
    `;
  }).join('');
}

function toggleModuleAccordion(modId) {
  const list = document.getElementById(`chapters-list-${modId}`);
  const header = list ? list.previousElementSibling : null;
  if (list && header) {
    list.classList.toggle('open');
    header.classList.toggle('open');
  }
}

function selectChapter(modId, chapId) {
  currentModuleId = modId;
  currentChapterId = chapId;
  renderCourseSidebar();
  renderChapter(modId, chapId);
  window.scrollTo({ top: 120, behavior: 'smooth' });
}

function openModuleChapter(modId, chapId) {
  switchTab('course');
  selectChapter(modId, chapId);
}

// Render Selected Chapter Content
function renderChapter(modId, chapId) {
  const container = document.getElementById('chapter-content-display');
  if (!container || !APP_STATE.courseData) return;

  stopAudioReading();

  const mod = APP_STATE.courseData.modules.find(m => m.id === modId);
  if (!mod) return;
  const chap = mod.chapters.find(c => c.id === chapId);
  if (!chap) return;

  const isCompleted = APP_STATE.userProgress.completedChapters.includes(chap.id);

  // Find previous & next chapter
  let allChaps = [];
  APP_STATE.courseData.modules.forEach(m => {
    m.chapters.forEach(c => allChaps.push({ modId: m.id, chap: c }));
  });
  const currentIndex = allChaps.findIndex(item => item.chap.id === chap.id);
  const prevItem = currentIndex > 0 ? allChaps[currentIndex - 1] : null;
  const nextItem = currentIndex < allChaps.length - 1 ? allChaps[currentIndex + 1] : null;

  // Build HTML Content
  let html = `
    <div class="reader-header">
      <div class="reader-breadcrumb">
        <span>Module ${mod.number}</span> <i class="fa-solid fa-chevron-right"></i> ${mod.title}
      </div>
      <h2 class="reader-title">${chap.title}</h2>
      <div class="reader-meta-bar">
        <div class="reader-tags">
          <span class="reader-pill"><i class="fa-regular fa-clock"></i> ${chap.readTime}</span>
          ${chap.badge ? `<span class="reader-pill badge-pill"><i class="fa-solid fa-certificate"></i> ${chap.badge}</span>` : ''}
          ${chap.id === 'm1-c1' ? `<span class="reader-pill" style="background:rgba(212,175,55,0.15); color:var(--fr-gold); border:1px solid rgba(212,175,55,0.3); font-weight:600;"><i class="fa-solid fa-circle-play"></i> Vidéo E-Learning B2</span>` : ''}
        </div>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <button class="reader-video-btn" onclick="openVideoLesson('${chap.id}')" title="Regarder la capsule vidéo animée avec voix et sous-titres">
            <i class="fa-solid fa-play"></i>
            <span>Vidéo E-Learning</span>
          </button>
          <button id="btn-audio-listen" class="reader-audio-btn" onclick="toggleAudioReading()">
            <i class="fa-solid fa-volume-high"></i>
            <span id="audio-btn-label">Écouter la leçon (B2)</span>
          </button>
        </div>
      </div>
    </div>
  `;

  // Video E-Learning Capsule Banner Callout for Chapter 1
  if (chap.id === 'm1-c1') {
    html += `
      <div class="chapter-video-callout" onclick="openVideoLesson('${chap.id}')">
        <div class="video-callout-left">
          <div class="video-play-pulse-btn">
            <i class="fa-solid fa-play"></i>
          </div>
          <div>
            <div class="video-callout-badge"><i class="fa-solid fa-sparkles"></i> Capsule E-Learning & Checkpoint Civique</div>
            <h4 class="video-callout-title">Regarder la Vidéo du Cours : ${chap.title}</h4>
            <p class="video-callout-desc">Animation 16:9 interactive avec voix off en français, repères visuels clés, sous-titres synchronisés et validation par mini-quiz.</p>
          </div>
        </div>
        <button class="btn-watch-video">
          <span>Lancer la vidéo</span>
          <i class="fa-solid fa-arrow-right"></i>
        </button>
      </div>
    `;
  }

  // Highlights ("À Retenir pour l'Entretien")
  if (chap.highlights && chap.highlights.length > 0) {
    html += `
      <div class="highlights-card">
        <h4 class="highlights-title"><i class="fa-solid fa-star"></i> À Retenir Absolument pour l'Entretien</h4>
        <ul class="highlights-list">
          ${chap.highlights.map(h => `<li>${h}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  // Illustration image if present
  if (chap.image) {
    html += `
      <div class="chapter-illustration-wrap">
        <img src="${chap.image}" alt="${chap.title}" class="chapter-illustration-img">
        ${chap.imageCaption ? `<div class="chapter-illustration-caption">${chap.imageCaption}</div>` : ''}
      </div>
    `;
  }

  // Main Content Blocks
  if (chap.content) {
    chap.content.forEach(block => {
      if (block.type === 'intro' || block.type === 'paragraph') {
        html += `<p class="reader-paragraph">${block.text}</p>`;
      } else if (block.type === 'section') {
        html += `
          <div class="reader-body-section">
            ${block.title ? `<h3 class="reader-section-title">${block.title}</h3>` : ''}
            ${block.text ? `<p class="reader-paragraph">${block.text}</p>` : ''}
            ${block.points ? `
              <ul class="reader-bullets-list">
                ${block.points.map(pt => `<li>${pt}</li>`).join('')}
              </ul>
            ` : ''}
          </div>
        `;
      } else if (block.type === 'callout') {
        html += `
          <div class="reader-callout ${block.variant || 'info'}">
            <div class="callout-header">
              <i class="fa-solid ${block.variant === 'warning' ? 'fa-triangle-exclamation' : (block.variant === 'danger' ? 'fa-ban' : 'fa-circle-info')}"></i>
              <span>${block.title}</span>
            </div>
            <div class="callout-text">${block.text}</div>
          </div>
        `;
      } else if (block.type === 'grid') {
        html += `
          <div class="reader-cards-grid">
            ${block.items.map(item => `
              <div class="reader-feature-card">
                ${item.image ? `<img src="${item.image}" alt="${item.title}" style="max-height:160px; object-fit:contain; margin-bottom:0.75rem; border-radius:8px;">` : ''}
                ${item.icon ? `<i class="fa-solid ${item.icon}" style="font-size:1.5rem; color:var(--fr-blue); margin-bottom:0.4rem;"></i>` : ''}
                <h5>${item.title}</h5>
                <p>${item.text}</p>
              </div>
            `).join('')}
          </div>
        `;
      } else if (block.type === 'table') {
        html += `
          <div class="reader-table-wrap">
            <table class="reader-table">
              <thead>
                <tr>
                  ${block.headers.map(h => `<th>${h}</th>`).join('')}
                </tr>
              </thead>
              <tbody>
                ${block.rows.map(row => `
                  <tr>
                    ${row.map(cell => `<td>${cell}</td>`).join('')}
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        `;
      } else if (block.type === 'timeline') {
        html += `
          <div class="reader-timeline" style="margin: 1.5rem 0; border-left: 3px solid var(--fr-blue); padding-left: 1.25rem;">
            ${block.events.map(ev => `
              <div style="margin-bottom: 1.25rem; position: relative;">
                <span style="display:inline-block; font-weight:800; color:var(--fr-blue); background:var(--fr-blue-light); padding:2px 8px; border-radius:4px; font-size:0.85rem; margin-bottom:0.25rem;">${ev.date}</span>
                <h5 style="font-size:1rem; font-weight:700; color:var(--text-primary);">${ev.title}</h5>
                <p style="font-size:0.9rem; color:var(--text-secondary);">${ev.desc}</p>
              </div>
            `).join('')}
          </div>
        `;
      }
    });
  }

  // Interview Questions specific to this lesson
  if (chap.interviewQuestions && chap.interviewQuestions.length > 0) {
    html += `
      <div class="lesson-interview-box">
        <h4 class="lesson-interview-title"><i class="fa-solid fa-comments"></i> Questions Possibles à l'Entretien Préfectoral</h4>
        ${chap.interviewQuestions.map(qa => `
          <div class="interview-qa-item">
            <div class="interview-qa-q"><i class="fa-regular fa-circle-question" style="color:var(--fr-blue);"></i> ${qa.question}</div>
            <div class="interview-qa-a"><strong>Réponse attendue :</strong> ${qa.answer}</div>
            ${qa.tip ? `<div class="interview-qa-tip"><i class="fa-solid fa-lightbulb"></i> <em>Conseil : ${qa.tip}</em></div>` : ''}
          </div>
        `).join('')}
      </div>
    `;
  }

  // Footer Navigation
  html += `
    <div class="reader-footer-nav">
      ${prevItem ? `
        <button class="reader-nav-btn btn-secondary" onclick="selectChapter('${prevItem.modId}', '${prevItem.chap.id}')">
          <i class="fa-solid fa-arrow-left"></i> ${prevItem.chap.title.substring(0, 24)}...
        </button>
      ` : `<div></div>`}

      <button id="btn-toggle-complete" class="reader-nav-btn ${isCompleted ? 'btn-success' : 'btn-primary'}" onclick="toggleChapterComplete('${chap.id}')">
        <i class="fa-solid ${isCompleted ? 'fa-check-circle' : 'fa-circle-check'}"></i>
        <span>${isCompleted ? 'Chapitre Validé (Marquer non lu)' : 'Marquer comme lu et compris'}</span>
      </button>

      ${nextItem ? `
        <button class="reader-nav-btn btn-primary" onclick="selectChapter('${nextItem.modId}', '${nextItem.chap.id}')">
          ${nextItem.chap.title.substring(0, 24)}... <i class="fa-solid fa-arrow-right"></i>
        </button>
      ` : `<div></div>`}
    </div>
  `;

  container.innerHTML = html;
}

// Toggle Complete Status for Current Chapter
function toggleChapterComplete(chapId) {
  const index = APP_STATE.userProgress.completedChapters.indexOf(chapId);
  if (index >= 0) {
    APP_STATE.userProgress.completedChapters.splice(index, 1);
    showToast('Chapitre marqué comme non lu', 'info');
  } else {
    APP_STATE.userProgress.completedChapters.push(chapId);
    showToast('Félicitations ! Chapitre validé 🎉', 'success');
  }

  saveUserProgress();
  renderCourseSidebar();
  renderChapter(currentModuleId, currentChapterId);
}

// Text-to-Speech (Web Speech API) in French
function toggleAudioReading() {
  if (!('speechSynthesis' in window)) {
    showToast("La synthèse vocale n'est pas supportée par votre navigateur", 'info');
    return;
  }

  const btn = document.getElementById('btn-audio-listen');
  const label = document.getElementById('audio-btn-label');

  if (isSpeaking) {
    stopAudioReading();
  } else {
    // Collect text from chapter reader
    const readerElement = document.getElementById('chapter-content-display');
    if (!readerElement) return;

    // Extract text ignoring buttons
    const textToRead = readerElement.innerText
      .replace(/Écouter la leçon/g, '')
      .replace(/Arrêter la lecture/g, '')
      .replace(/Marquer comme lu/g, '');

    speechUtterance = new SpeechSynthesisUtterance(textToRead);
    speechUtterance.lang = 'fr-FR';
    speechUtterance.rate = 0.95; // Clear natural French reading pace

    speechUtterance.onend = () => stopAudioReading();
    speechUtterance.onerror = () => stopAudioReading();

    window.speechSynthesis.speak(speechUtterance);
    isSpeaking = true;

    if (btn) btn.classList.add('speaking');
    if (label) label.textContent = 'Arrêter la lecture';
  }
}

function stopAudioReading() {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
  isSpeaking = false;
  const btn = document.getElementById('btn-audio-listen');
  const label = document.getElementById('audio-btn-label');
  if (btn) btn.classList.remove('speaking');
  if (label) label.textContent = 'Écouter la leçon (B2)';
}

// Search filter in sidebar
function setupCourseSearch() {
  const searchInput = document.getElementById('course-search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      renderCourseSidebar(e.target.value);
    });
  }
}

window.initCourseView = initCourseView;
window.selectChapter = selectChapter;
window.openModuleChapter = openModuleChapter;
window.toggleModuleAccordion = toggleModuleAccordion;
window.toggleChapterComplete = toggleChapterComplete;
window.toggleAudioReading = toggleAudioReading;
