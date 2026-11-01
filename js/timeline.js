/**
 * LIVRET DU CITOYEN 2026 - Frise Chronologique Interactive des Dates Clés
 * 
 * Permet de réviser les 20 repères historiques et républicains majeurs
 * exigés lors de l'Examen Civique et de l'Entretien de Naturalisation.
 */

(function () {
  'use strict';

  let timelineMilestones = [];
  let timelineCategories = ['Tous'];
  let activeTimelineCategory = 'Tous';
  let timelineSearchQuery = '';
  let currentlyPlayingId = null;

  /**
   * Charger les données de la frise chronologique
   */
  async function loadTimelineData() {
    if (timelineMilestones.length > 0) return true;
    try {
      const response = await fetch('data/timeline.json');
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      timelineMilestones = data.milestones || [];
      if (data.categories && data.categories.length > 0) {
        timelineCategories = data.categories;
      }
      return true;
    } catch (err) {
      console.error('Erreur chargement timeline.json:', err);
      return false;
    }
  }

  /**
   * Normaliser le texte pour la recherche
   */
  function normalizeText(str) {
    if (!str) return '';
    return str
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .trim();
  }

  /**
   * Filtrer les repères selon catégorie active et recherche
   */
  function getFilteredMilestones() {
    let list = timelineMilestones;

    if (activeTimelineCategory !== 'Tous') {
      list = list.filter(m => m.category === activeTimelineCategory);
    }

    if (timelineSearchQuery.trim()) {
      const q = normalizeText(timelineSearchQuery);
      list = list.filter(m => {
        const year = normalizeText(m.year);
        const date = normalizeText(m.date);
        const title = normalizeText(m.title);
        const desc = normalizeText(m.description);
        const fig = normalizeText(m.figures);
        const tip = normalizeText(m.interviewTip);
        return year.includes(q) || date.includes(q) || title.includes(q) || desc.includes(q) || fig.includes(q) || tip.includes(q);
      });
    }

    return list;
  }

  /**
   * Ouvrir le modal de la frise
   */
  async function openTimelineModal() {
    const modal = document.getElementById('timeline-modal');
    if (!modal) return;

    await loadTimelineData();

    renderTimelineCategories();
    renderTimelineItems();

    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    // Focus sur la recherche pour faciliter la saisie
    const searchInput = document.getElementById('timeline-search-input');
    if (searchInput) {
      setTimeout(() => searchInput.focus(), 150);
    }
  }

  /**
   * Fermer le modal de la frise
   */
  function closeTimelineModal() {
    const modal = document.getElementById('timeline-modal');
    if (!modal) return;

    stopTimelineSpeech();

    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  /**
   * Rendu des onglets / filtres par catégorie
   */
  function renderTimelineCategories() {
    const container = document.getElementById('timeline-categories-bar');
    if (!container) return;

    container.innerHTML = timelineCategories.map(cat => {
      const isActive = cat === activeTimelineCategory;
      const count = cat === 'Tous' 
        ? timelineMilestones.length 
        : timelineMilestones.filter(m => m.category === cat).length;
      return `
        <button type="button" 
                class="timeline-cat-pill ${isActive ? 'active' : ''}" 
                onclick="window.setTimelineCategory('${cat.replace(/'/g, "\\'")}')">
          <span>${cat}</span>
          <span class="timeline-pill-count">${count}</span>
        </button>
      `;
    }).join('');
  }

  /**
   * Changer la catégorie active
   */
  function setTimelineCategory(category) {
    activeTimelineCategory = category;
    renderTimelineCategories();
    renderTimelineItems();
  }

  /**
   * Gérer la recherche
   */
  function handleTimelineSearch(val) {
    timelineSearchQuery = val || '';
    const clearBtn = document.getElementById('timeline-search-clear');
    if (clearBtn) {
      clearBtn.style.display = timelineSearchQuery ? 'inline-flex' : 'none';
    }
    renderTimelineItems();
  }

  function clearTimelineSearch() {
    const input = document.getElementById('timeline-search-input');
    if (input) {
      input.value = '';
    }
    timelineSearchQuery = '';
    const clearBtn = document.getElementById('timeline-search-clear');
    if (clearBtn) {
      clearBtn.style.display = 'none';
    }
    renderTimelineItems();
    if (input) input.focus();
  }

  /**
   * Rendu des jalons de la frise chronologique
   */
  function renderTimelineItems() {
    const container = document.getElementById('timeline-stream-container');
    const countBadge = document.getElementById('timeline-results-count');
    if (!container) return;

    const filtered = getFilteredMilestones();

    if (countBadge) {
      countBadge.textContent = `${filtered.length} repère${filtered.length > 1 ? 's' : ''}`;
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="timeline-empty-state">
          <i class="fa-solid fa-calendar-xmark"></i>
          <h4>Aucun repère chronologique trouvé</h4>
          <p>Essayez avec d'autres mots-clés ou sélectionnez une autre catégorie.</p>
          <button type="button" class="btn btn-secondary btn-sm" onclick="window.clearTimelineSearch(); window.setTimelineCategory('Tous');">
            Réinitialiser les filtres
          </button>
        </div>
      `;
      return;
    }

    container.innerHTML = `
      <div class="timeline-spine"></div>
      <div class="timeline-milestones-list">
        ${filtered.map((item, index) => {
          const isLeft = index % 2 === 0;
          const isPlaying = currentlyPlayingId === item.id;
          return `
            <article class="timeline-milestone-row ${isLeft ? 'row-left' : 'row-right'}" id="milestone-${item.id}">
              <div class="timeline-center-node">
                <div class="timeline-node-pin">
                  <i class="fa-solid ${item.icon || 'fa-calendar-check'}"></i>
                </div>
                <div class="timeline-year-callout">${item.year}</div>
              </div>
              <div class="timeline-card-wrapper">
                <div class="timeline-card">
                  <div class="timeline-card-header">
                    <span class="timeline-badge-cat"><i class="fa-solid fa-tag"></i> ${item.category}</span>
                    <span class="timeline-badge-sub">${item.badge || item.year}</span>
                  </div>

                  <h3 class="timeline-card-title">${item.title}</h3>
                  <div class="timeline-card-date"><i class="fa-regular fa-calendar"></i> ${item.date}</div>

                  <p class="timeline-card-desc">${item.description}</p>

                  ${item.figures ? `
                    <div class="timeline-card-figures">
                      <strong><i class="fa-solid fa-users"></i> Personnalités clés :</strong>
                      <span>${item.figures}</span>
                    </div>
                  ` : ''}

                  ${item.interviewTip ? `
                    <div class="timeline-card-tip">
                      <div class="timeline-tip-header">
                        <i class="fa-solid fa-lightbulb"></i>
                        <span>Clé Examen & Entretien</span>
                      </div>
                      <p>${item.interviewTip}</p>
                    </div>
                  ` : ''}

                  <div class="timeline-card-actions">
                    <button type="button" 
                            class="timeline-action-btn ${isPlaying ? 'active-speaking' : ''}" 
                            onclick="window.toggleTimelineSpeech('${item.id}')"
                            title="Écouter le repère avec la synthèse vocale">
                      <i class="fa-solid ${isPlaying ? 'fa-stop' : 'fa-volume-high'}"></i>
                      <span>${isPlaying ? 'Arrêter' : 'Écouter'}</span>
                    </button>

                    ${item.flashcardId ? `
                      <button type="button" 
                              class="timeline-action-btn btn-link-fc" 
                              onclick="window.jumpToFlashcardFromTimeline('${item.flashcardId}')"
                              title="Réviser la Flashcard correspondante">
                        <i class="fa-solid fa-clone"></i>
                        <span>Flashcard ${item.flashcardId.replace('fc-', '#')}</span>
                      </button>
                    ` : ''}
                  </div>
                </div>
              </div>
            </article>
          `;
        }).join('')}
      </div>
    `;
  }

  /**
   * Synthèse vocale pour un repère
   */
  function toggleTimelineSpeech(milestoneId) {
    if (currentlyPlayingId === milestoneId) {
      stopTimelineSpeech();
      return;
    }

    const item = timelineMilestones.find(m => m.id === milestoneId);
    if (!item) return;

    stopTimelineSpeech();
    currentlyPlayingId = milestoneId;
    renderTimelineItems();

    const textToRead = `${item.date}. ${item.title}. ${item.description}. Personnalités : ${item.figures || 'Non spécifiées'}. Conseil pour l'entretien : ${item.interviewTip || ''}`;

    if (window.FrenchAIReader) {
      window.FrenchAIReader.speak(textToRead, {
        onEnd: () => {
          currentlyPlayingId = null;
          renderTimelineItems();
        },
        onError: () => {
          currentlyPlayingId = null;
          renderTimelineItems();
        }
      });
    } else if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(textToRead);
      utter.lang = 'fr-FR';
      utter.rate = 1.0;
      utter.onend = () => {
        currentlyPlayingId = null;
        renderTimelineItems();
      };
      utter.onerror = () => {
        currentlyPlayingId = null;
        renderTimelineItems();
      };
      window.speechSynthesis.speak(utter);
    }
  }

  function stopTimelineSpeech() {
    if (window.FrenchAIReader) {
      window.FrenchAIReader.stop();
    }
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    currentlyPlayingId = null;
  }

  /**
   * Sauter directement sur la flashcard depuis la frise
   */
  function jumpToFlashcardFromTimeline(flashcardId) {
    closeTimelineModal();
    if (typeof window.switchView === 'function') {
      window.switchView('flashcards');
    }
    setTimeout(() => {
      if (typeof window.jumpToCard === 'function') {
        window.jumpToCard(flashcardId);
      }
    }, 250);
  }

  // Écouteur pour la touche Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      const modal = document.getElementById('timeline-modal');
      if (modal && modal.classList.contains('active')) {
        closeTimelineModal();
      }
    }
  });

  // Exposer les méthodes globalement
  window.openTimelineModal = openTimelineModal;
  window.closeTimelineModal = closeTimelineModal;
  window.setTimelineCategory = setTimelineCategory;
  window.handleTimelineSearch = handleTimelineSearch;
  window.clearTimelineSearch = clearTimelineSearch;
  window.toggleTimelineSpeech = toggleTimelineSpeech;
  window.jumpToFlashcardFromTimeline = jumpToFlashcardFromTimeline;

})();
