/**
 * LIVRET DU CITOYEN 2026 - Carte Interactive de France & Géographie Républicaine
 * 
 * Permet aux candidats de maîtriser les 13 Régions, les 5 Fleuves,
 * les 5 Massifs, les DROM-COM et les pays frontaliers pour l'entretien en préfecture.
 */

(function () {
  'use strict';

  let geoData = null;
  let activeGeoTab = 'exploration'; // 'exploration' | 'quiz' | 'reperes'
  let activeGeoLayer = 'all'; // 'all' | 'regions' | 'rivers' | 'mountains' | 'outremer'
  let selectedEntity = null;
  let currentSpeakingId = null;

  // Quiz Carte State
  let quizCurrentIndex = 0;
  let quizScore = 0;
  let quizAnswered = false;
  let quizActiveQuestion = null;

  /**
   * Charger les données géographiques
   */
  async function loadGeographyData() {
    if (geoData) return true;
    try {
      const response = await fetch('data/geography.json');
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      geoData = await response.json();
      return true;
    } catch (err) {
      console.error('Erreur chargement geography.json:', err);
      return false;
    }
  }

  /**
   * Ouvrir la modale de la carte interactive
   */
  async function openGeographyModal() {
    const modal = document.getElementById('geography-modal');
    if (!modal) return;

    await loadGeographyData();

    // Sélectionner par défaut la première région (Île-de-France)
    if (geoData && geoData.regions && geoData.regions.length > 0 && !selectedEntity) {
      selectedEntity = { type: 'region', data: geoData.regions[0] };
    }

    renderGeographyUI();

    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  /**
   * Fermer la modale
   */
  function closeGeographyModal() {
    const modal = document.getElementById('geography-modal');
    if (!modal) return;

    stopGeoSpeech();

    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  /**
   * Changer d'onglet principal (Exploration vs Quiz vs Repères)
   */
  function switchGeoTab(tab) {
    activeGeoTab = tab;
    stopGeoSpeech();

    // Mettre à jour les boutons d'onglets
    document.querySelectorAll('.geo-tab-pill').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tab);
    });

    if (tab === 'quiz') {
      startGeoQuiz();
    } else {
      renderGeographyUI();
    }
  }

  /**
   * Filtrer par couche (Toutes, Régions, Fleuves, Montagnes, Outre-mer)
   */
  function setGeoLayer(layer) {
    activeGeoLayer = layer;
    document.querySelectorAll('.geo-layer-pill').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.layer === layer);
    });
    updateMapLayersVisibility();
  }

  /**
   * Rendu complet de l'interface géographique
   */
  function renderGeographyUI() {
    const body = document.getElementById('geo-modal-body');
    if (!body || !geoData) return;

    if (activeGeoTab === 'reperes') {
      body.innerHTML = renderReperesView();
      return;
    }

    if (activeGeoTab === 'quiz') {
      body.innerHTML = renderQuizView();
      return;
    }

    // Mode Exploration (Carte SVG + Inspecteur + Vignettes DROM)
    body.innerHTML = `
      <div class="geo-workspace">
        <!-- Colonne Gauche : Carte Interactive SVG & Vignettes DROM -->
        <div class="geo-map-pane">
          <!-- Barre de filtres de couches -->
          <div class="geo-layer-bar">
            <button type="button" class="geo-layer-pill ${activeGeoLayer === 'all' ? 'active' : ''}" data-layer="all" onclick="window.setGeoLayer('all')">
              <i class="fa-solid fa-layer-group"></i> Tous les repères
            </button>
            <button type="button" class="geo-layer-pill ${activeGeoLayer === 'regions' ? 'active' : ''}" data-layer="regions" onclick="window.setGeoLayer('regions')">
              <i class="fa-solid fa-draw-polygon"></i> 13 Régions
            </button>
            <button type="button" class="geo-layer-pill ${activeGeoLayer === 'rivers' ? 'active' : ''}" data-layer="rivers" onclick="window.setGeoLayer('rivers')">
              <i class="fa-solid fa-water"></i> 5 Fleuves
            </button>
            <button type="button" class="geo-layer-pill ${activeGeoLayer === 'mountains' ? 'active' : ''}" data-layer="mountains" onclick="window.setGeoLayer('mountains')">
              <i class="fa-solid fa-mountain"></i> 5 Massifs
            </button>
            <button type="button" class="geo-layer-pill ${activeGeoLayer === 'outremer' ? 'active' : ''}" data-layer="outremer" onclick="window.setGeoLayer('outremer')">
              <i class="fa-solid fa-earth-americas"></i> Outre-Mer
            </button>
          </div>

          <!-- Conteneur Carte SVG -->
          <div class="geo-svg-wrapper" id="geo-svg-wrapper">
            ${renderFranceSvgMap()}
          </div>

          <!-- Vignettes Outre-Mer (DROM-COM) -->
          <div class="geo-outremer-ribbon" id="geo-outremer-ribbon">
            <div class="geo-ribbon-title">
              <i class="fa-solid fa-earth-americas"></i>
              <span>Territoires d'Outre-Mer (DROM-COM) :</span>
            </div>
            <div class="geo-outremer-chips">
              ${geoData.outremer.map(om => {
                const isSelected = selectedEntity && selectedEntity.type === 'outremer' && selectedEntity.data.id === om.id;
                return `
                  <button type="button" 
                          class="geo-om-chip ${isSelected ? 'active' : ''}" 
                          id="chip-${om.id}" 
                          onclick="window.selectGeoEntity('outremer', '${om.id}')">
                    <span class="om-chip-code">${om.code || 'DOM'}</span>
                    <span class="om-chip-name">${om.name}</span>
                  </button>
                `;
              }).join('')}
            </div>
          </div>
        </div>

        <!-- Colonne Droite : Fiche Inspecteur Détaillée -->
        <aside class="geo-inspector-pane" id="geo-inspector-pane">
          ${renderInspectorCard()}
        </aside>
      </div>
    `;

    updateMapLayersVisibility();
  }

  /**
   * Rendu de la carte vectorielle SVG de France
   */
  function renderFranceSvgMap() {
    return `
      <svg viewBox="0 0 920 780" class="france-interactive-map" id="france-svg" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter id="map-shadow" x="-5%" y="-5%" width="110%" height="110%">
            <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#001428" flood-opacity="0.18" />
          </filter>
          <linearGradient id="sea-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0055A5" />
            <stop offset="100%" stop-color="#0284c7" />
          </linearGradient>
          <linearGradient id="river-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#38bdf8" />
            <stop offset="100%" stop-color="#0284c7" />
          </linearGradient>
        </defs>

        <!-- Façades Maritimes & Mers Environnantes -->
        <g class="geo-seas-layer" opacity="0.6">
          <text x="280" y="70" class="geo-sea-label">LA MANCHE</text>
          <text x="590" y="50" class="geo-sea-label">MER DU NORD</text>
          <text x="80" y="440" class="geo-sea-label" transform="rotate(-90 80,440)">OCÉAN ATLANTIQUE</text>
          <text x="550" y="720" class="geo-sea-label">MER MÉDITERRANÉE</text>
        </g>

        <!-- Pays Frontaliers Extérieurs -->
        <g class="geo-border-countries" opacity="0.75">
          <!-- Belgique -->
          <path d="M 520,30 L 610,60 L 630,110 L 580,100 Z" class="geo-neighbor-country" />
          <text x="560" y="70" class="geo-neighbor-label">BELGIQUE</text>

          <!-- Allemagne -->
          <path d="M 680,110 L 780,110 L 770,220 L 710,190 Z" class="geo-neighbor-country" />
          <text x="735" y="160" class="geo-neighbor-label">ALLEMAGNE</text>

          <!-- Suisse -->
          <path d="M 700,280 L 790,290 L 780,360 L 690,340 Z" class="geo-neighbor-country" />
          <text x="740" y="325" class="geo-neighbor-label">SUISSE</text>

          <!-- Italie -->
          <path d="M 720,410 L 800,430 L 780,560 L 710,530 Z" class="geo-neighbor-country" />
          <text x="750" y="480" class="geo-neighbor-label">ITALIE</text>

          <!-- Espagne -->
          <path d="M 240,650 L 520,660 L 500,750 L 220,740 Z" class="geo-neighbor-country" />
          <text x="360" y="700" class="geo-neighbor-label">ESPAGNE</text>
        </g>

        <!-- ==========================================
             COUCHE DES 13 RÉGIONS MÉTROPOLITAINES
             ========================================== -->
        <g class="geo-regions-layer" filter="url(#map-shadow)">
          <!-- 1. Hauts-de-France -->
          <path id="reg-hdf" 
                class="geo-region-path" 
                data-id="hdf"
                d="M 440,50 L 510,40 L 550,70 L 570,130 L 530,150 L 460,150 L 430,110 Z"
                fill="#06b6d4" 
                onclick="window.handleMapElementClick('region', 'hdf')" />
          <text x="500" y="105" class="geo-region-label" onclick="window.handleMapElementClick('region', 'hdf')">Hauts-de-France</text>

          <!-- 2. Normandie -->
          <path id="reg-nor" 
                class="geo-region-path" 
                data-id="nor"
                d="M 280,140 L 370,120 L 430,110 L 460,150 L 430,200 L 330,220 L 290,190 Z"
                fill="#f97316" 
                onclick="window.handleMapElementClick('region', 'nor')" />
          <text x="360" y="170" class="geo-region-label" onclick="window.handleMapElementClick('region', 'nor')">Normandie</text>

          <!-- 3. Île-de-France -->
          <path id="reg-idf" 
                class="geo-region-path" 
                data-id="idf"
                d="M 460,150 L 530,150 L 540,210 L 510,250 L 440,240 L 430,200 Z"
                fill="#3b82f6" 
                onclick="window.handleMapElementClick('region', 'idf')" />
          <!-- Étoile Capitale Paris -->
          <circle cx="485" cy="195" r="7" class="geo-capital-dot" />
          <text x="485" y="180" class="geo-capital-label">★ PARIS</text>
          <text x="485" y="225" class="geo-region-label" onclick="window.handleMapElementClick('region', 'idf')">Île-de-France</text>

          <!-- 4. Grand Est -->
          <path id="reg-ges" 
                class="geo-region-path" 
                data-id="ges"
                d="M 530,150 L 570,130 L 640,110 L 730,150 L 730,230 L 680,260 L 570,250 L 540,210 Z"
                fill="#8b5cf6" 
                onclick="window.handleMapElementClick('region', 'ges')" />
          <text x="635" y="195" class="geo-region-label" onclick="window.handleMapElementClick('region', 'ges')">Grand Est</text>

          <!-- 5. Bretagne -->
          <path id="reg-bre" 
                class="geo-region-path" 
                data-id="bre"
                d="M 120,220 L 230,190 L 290,190 L 280,270 L 210,300 L 140,270 Z"
                fill="#14b8a6" 
                onclick="window.handleMapElementClick('region', 'bre')" />
          <text x="210" y="245" class="geo-region-label" onclick="window.handleMapElementClick('region', 'bre')">Bretagne</text>

          <!-- 6. Pays de la Loire -->
          <path id="reg-pdl" 
                class="geo-region-path" 
                data-id="pdl"
                d="M 280,270 L 330,220 L 380,260 L 370,360 L 280,370 L 260,330 Z"
                fill="#84cc16" 
                onclick="window.handleMapElementClick('region', 'pdl')" />
          <text x="325" y="310" class="geo-region-label" onclick="window.handleMapElementClick('region', 'pdl')">Pays de la Loire</text>

          <!-- 7. Centre-Val de Loire -->
          <path id="reg-cvl" 
                class="geo-region-path" 
                data-id="cvl"
                d="M 380,260 L 430,200 L 440,240 L 510,250 L 500,360 L 420,380 L 370,360 Z"
                fill="#0ea5e9" 
                onclick="window.handleMapElementClick('region', 'cvl')" />
          <text x="440" y="305" class="geo-region-label" onclick="window.handleMapElementClick('region', 'cvl')">Centre-Val de Loire</text>

          <!-- 8. Bourgogne-Franche-Comté -->
          <path id="reg-bfc" 
                class="geo-region-path" 
                data-id="bfc"
                d="M 510,250 L 570,250 L 680,260 L 700,340 L 640,380 L 540,380 L 500,360 Z"
                fill="#eab308" 
                onclick="window.handleMapElementClick('region', 'bfc')" />
          <text x="600" y="315" class="geo-region-label" onclick="window.handleMapElementClick('region', 'bfc')">Bourgogne-Franche-Comté</text>

          <!-- 9. Nouvelle-Aquitaine -->
          <path id="reg-naq" 
                class="geo-region-path" 
                data-id="naq"
                d="M 280,370 L 370,360 L 420,380 L 420,490 L 360,590 L 250,580 L 270,440 Z"
                fill="#10b981" 
                onclick="window.handleMapElementClick('region', 'naq')" />
          <text x="340" y="480" class="geo-region-label" onclick="window.handleMapElementClick('region', 'naq')">Nouvelle-Aquitaine</text>

          <!-- 10. Auvergne-Rhône-Alpes -->
          <path id="reg-ara" 
                class="geo-region-path" 
                data-id="ara"
                d="M 420,380 L 500,360 L 540,380 L 640,380 L 700,340 L 720,430 L 680,510 L 560,520 L 460,490 Z"
                fill="#6366f1" 
                onclick="window.handleMapElementClick('region', 'ara')" />
          <text x="590" y="445" class="geo-region-label" onclick="window.handleMapElementClick('region', 'ara')">Auvergne-Rhône-Alpes</text>

          <!-- 11. Occitanie -->
          <path id="reg-occ" 
                class="geo-region-path" 
                data-id="occ"
                d="M 360,590 L 420,490 L 460,490 L 560,520 L 540,620 L 480,650 L 330,640 Z"
                fill="#f59e0b" 
                onclick="window.handleMapElementClick('region', 'occ')" />
          <text x="450" y="585" class="geo-region-label" onclick="window.handleMapElementClick('region', 'occ')">Occitanie</text>

          <!-- 12. Provence-Alpes-Côte d'Azur (PACA) -->
          <path id="reg-paca" 
                class="geo-region-path" 
                data-id="paca"
                d="M 560,520 L 680,510 L 720,550 L 680,630 L 570,630 L 540,620 Z"
                fill="#ec4899" 
                onclick="window.handleMapElementClick('region', 'paca')" />
          <text x="635" y="575" class="geo-region-label" onclick="window.handleMapElementClick('region', 'paca')">Provence-Alpes-Côte d'Azur</text>

          <!-- 13. Corse -->
          <g id="reg-cor" class="geo-corse-group" onclick="window.handleMapElementClick('region', 'cor')">
            <path class="geo-region-path" 
                  data-id="cor"
                  d="M 780,620 Q 805,620 810,660 Q 805,710 780,720 Q 765,680 770,640 Z"
                  fill="#d946ef" />
            <text x="790" y="675" class="geo-region-label">Corse</text>
          </g>
        </g>

        <!-- ==========================================
             COUCHE DES 5 GRANDS FLEUVES
             ========================================== -->
        <g class="geo-rivers-layer" id="layer-rivers">
          <!-- 1. La Loire (1 006 km) -->
          <path id="riv-loire" 
                class="geo-river-path" 
                data-id="loire"
                d="M 540,490 Q 520,400 460,340 Q 430,300 370,300 Q 300,310 240,320" 
                onclick="window.handleMapElementClick('river', 'loire')" />
          <text x="350" y="285" class="geo-river-label" onclick="window.handleMapElementClick('river', 'loire')">≈ La Loire</text>

          <!-- 2. La Seine (777 km) -->
          <path id="riv-seine" 
                class="geo-river-path" 
                data-id="seine"
                d="M 580,270 Q 520,230 485,195 Q 430,170 340,150" 
                onclick="window.handleMapElementClick('river', 'seine')" />
          <text x="420" y="160" class="geo-river-label" onclick="window.handleMapElementClick('river', 'seine')">≈ La Seine</text>

          <!-- 3. Le Rhône (812 km) -->
          <path id="riv-rhone" 
                class="geo-river-path" 
                data-id="rhone"
                d="M 690,360 Q 640,400 620,430 Q 600,480 570,550 Q 560,600 560,630" 
                onclick="window.handleMapElementClick('river', 'rhone')" />
          <text x="615" y="490" class="geo-river-label" onclick="window.handleMapElementClick('river', 'rhone')">≈ Le Rhône</text>

          <!-- 4. La Garonne (529 km) -->
          <path id="riv-garonne" 
                class="geo-river-path" 
                data-id="garonne"
                d="M 400,640 Q 430,590 400,530 Q 340,480 290,430" 
                onclick="window.handleMapElementClick('river', 'garonne')" />
          <text x="360" y="520" class="geo-river-label" onclick="window.handleMapElementClick('river', 'garonne')">≈ La Garonne</text>

          <!-- 5. Le Rhin (frontière) -->
          <path id="riv-rhin" 
                class="geo-river-path" 
                data-id="rhin"
                d="M 695,255 L 720,200 L 710,135" 
                onclick="window.handleMapElementClick('river', 'rhin')" />
          <text x="730" y="215" class="geo-river-label" onclick="window.handleMapElementClick('river', 'rhin')">≈ Le Rhin</text>
        </g>

        <!-- ==========================================
             COUCHE DES 5 MASSIFS MONTAGNEUX
             ========================================== -->
        <g class="geo-mountains-layer" id="layer-mountains">
          <!-- Alpes & Mont Blanc -->
          <g id="mtn-alpes" class="geo-mountain-group" onclick="window.handleMapElementClick('mountain', 'alpes')">
            <path d="M 670,410 L 685,385 L 700,410 Z M 690,430 L 705,405 L 720,430 Z M 670,460 L 685,435 L 700,460 Z" class="geo-peak-icon" />
            <circle cx="685" cy="385" r="4.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5" />
            <text x="670" y="375" class="geo-mountain-name">▲ ALPES (Mont Blanc 4 808 m)</text>
          </g>

          <!-- Pyrénées -->
          <g id="mtn-pyrenees" class="geo-mountain-group" onclick="window.handleMapElementClick('mountain', 'pyrenees')">
            <path d="M 330,650 L 345,630 L 360,650 Z M 380,655 L 395,635 L 410,655 Z M 440,655 L 455,635 L 470,655 Z" class="geo-peak-icon" />
            <text x="380" y="675" class="geo-mountain-name">▲ PYRÉNÉES</text>
          </g>

          <!-- Massif central -->
          <g id="mtn-massif-central" class="geo-mountain-group" onclick="window.handleMapElementClick('mountain', 'massif-central')">
            <path d="M 470,450 L 485,430 L 500,450 Z M 500,470 L 515,450 L 530,470 Z" class="geo-peak-icon" />
            <text x="440" y="440" class="geo-mountain-name">▲ MASSIF CENTRAL</text>
          </g>

          <!-- Jura -->
          <g id="mtn-jura" class="geo-mountain-group" onclick="window.handleMapElementClick('mountain', 'jura')">
            <path d="M 660,330 L 675,310 L 690,330 Z" class="geo-peak-icon" />
            <text x="670" y="305" class="geo-mountain-name">▲ JURA</text>
          </g>

          <!-- Vosges -->
          <g id="mtn-vosges" class="geo-mountain-group" onclick="window.handleMapElementClick('mountain', 'vosges')">
            <path d="M 680,210 L 695,190 L 710,210 Z" class="geo-peak-icon" />
            <text x="660" y="180" class="geo-mountain-name">▲ VOSGES</text>
          </g>
        </g>
      </svg>
    `;
  }

  /**
   * Visibilité des couches selon filtre actif
   */
  function updateMapLayersVisibility() {
    const rivers = document.getElementById('layer-rivers');
    const mountains = document.getElementById('layer-mountains');
    const regions = document.querySelectorAll('.geo-region-path');
    const omRibbon = document.getElementById('geo-outremer-ribbon');

    if (rivers) {
      rivers.style.display = (activeGeoLayer === 'all' || activeGeoLayer === 'rivers') ? 'block' : 'none';
    }
    if (mountains) {
      mountains.style.display = (activeGeoLayer === 'all' || activeGeoLayer === 'mountains') ? 'block' : 'none';
    }
    if (omRibbon) {
      omRibbon.style.display = (activeGeoLayer === 'all' || activeGeoLayer === 'outremer') ? 'flex' : 'none';
    }

    // Mise en valeur des régions
    regions.forEach(r => {
      if (activeGeoLayer === 'rivers' || activeGeoLayer === 'mountains') {
        r.style.opacity = '0.35';
      } else {
        r.style.opacity = '1';
      }
    });
  }

  /**
   * Clic sur un élément de la carte SVG
   */
  function handleMapElementClick(type, id) {
    if (activeGeoTab === 'quiz') {
      handleQuizAnswerSelection(type, id);
      return;
    }
    selectGeoEntity(type, id);
  }

  /**
   * Sélectionner une entité et actualiser la fiche inspecteur
   */
  function selectGeoEntity(type, id) {
    if (!geoData) return;
    let data = null;

    if (type === 'region') {
      data = geoData.regions.find(r => r.id === id);
    } else if (type === 'river') {
      data = geoData.rivers.find(r => r.id === id);
    } else if (type === 'mountain') {
      data = geoData.mountains.find(m => m.id === id);
    } else if (type === 'outremer') {
      data = geoData.outremer.find(o => o.id === id);
    }

    if (!data) return;

    selectedEntity = { type, data };

    // Highlight sur la carte
    document.querySelectorAll('.geo-region-path, .geo-river-path, .geo-mountain-group, .geo-om-chip').forEach(el => {
      el.classList.remove('active-target');
    });

    if (type === 'region') {
      const el = document.getElementById(`reg-${id}`);
      if (el) el.classList.add('active-target');
    } else if (type === 'river') {
      const el = document.getElementById(`riv-${id}`);
      if (el) el.classList.add('active-target');
    } else if (type === 'mountain') {
      const el = document.getElementById(`mtn-${id}`);
      if (el) el.classList.add('active-target');
    } else if (type === 'outremer') {
      const el = document.getElementById(`chip-${id}`);
      if (el) el.classList.add('active-target');
    }

    const inspector = document.getElementById('geo-inspector-pane');
    if (inspector) {
      inspector.innerHTML = renderInspectorCard();
    }
  }

  /**
   * Rendu de la fiche d'inspection détaillée
   */
  function renderInspectorCard() {
    if (!selectedEntity || !selectedEntity.data) {
      return `
        <div class="geo-inspector-empty">
          <i class="fa-solid fa-hand-pointer"></i>
          <h4>Cliquez sur la carte</h4>
          <p>Sélectionnez une région, un fleuve, un massif ou un DROM pour afficher sa fiche d'assimilation civique.</p>
        </div>
      `;
    }

    const { type, data } = selectedEntity;
    const isSpeaking = currentSpeakingId === data.id;

    let badgeText = "Repère Géographique";
    let iconClass = "fa-map-pin";
    if (type === 'region') { badgeText = "Région Métropolitaine"; iconClass = "fa-draw-polygon"; }
    else if (type === 'river') { badgeText = "Grand Fleuve Français"; iconClass = "fa-water"; }
    else if (type === 'mountain') { badgeText = "Massif Montagneux"; iconClass = "fa-mountain"; }
    else if (type === 'outremer') { badgeText = data.statut || "Outre-Mer"; iconClass = "fa-earth-americas"; }

    return `
      <div class="geo-card">
        <div class="geo-card-header">
          <span class="geo-card-badge"><i class="fa-solid ${iconClass}"></i> ${badgeText}</span>
          <button type="button" 
                  class="geo-speech-btn ${isSpeaking ? 'active-speaking' : ''}" 
                  onclick="window.toggleGeoSpeech('${data.id}')"
                  title="Écouter la fiche vocale">
            <i class="fa-solid ${isSpeaking ? 'fa-stop' : 'fa-volume-high'}"></i>
            <span>${isSpeaking ? 'Arrêter' : 'Écouter'}</span>
          </button>
        </div>

        <h3 class="geo-card-title">${data.name}</h3>

        ${data.chefLieu ? `
          <div class="geo-meta-pill">
            <strong><i class="fa-solid fa-landmark"></i> Chef-lieu / Préfecture :</strong>
            <span>${data.chefLieu}</span>
          </div>
        ` : ''}

        ${data.length ? `
          <div class="geo-meta-pill">
            <strong><i class="fa-solid fa-ruler-horizontal"></i> Longueur :</strong>
            <span>${data.length}</span>
          </div>
        ` : ''}

        ${data.highestPeak ? `
          <div class="geo-meta-pill">
            <strong><i class="fa-solid fa-mountain-sun"></i> Point culminant :</strong>
            <span>${data.highestPeak}</span>
          </div>
        ` : ''}

        ${data.ocean ? `
          <div class="geo-meta-pill">
            <strong><i class="fa-solid fa-compass"></i> Situation :</strong>
            <span>${data.ocean}</span>
          </div>
        ` : ''}

        ${data.cities ? `
          <div class="geo-meta-pill">
            <strong><i class="fa-solid fa-city"></i> Villes arrosées :</strong>
            <span>${data.cities}</span>
          </div>
        ` : ''}

        <p class="geo-card-desc">${data.description || data.highlights || ''}</p>

        ${data.interviewTip ? `
          <div class="geo-interview-tip">
            <div class="geo-tip-title">
              <i class="fa-solid fa-lightbulb"></i>
              <span>Question type à l'entretien</span>
            </div>
            <p>${data.interviewTip}</p>
          </div>
        ` : ''}

        ${data.departments ? `
          <div class="geo-departments-box">
            <span class="geo-dept-count"><strong>Départements (${data.departmentsCount}) :</strong></span>
            <span class="geo-dept-list">${data.departments}</span>
          </div>
        ` : ''}
      </div>
    `;
  }

  /**
   * Synthèse vocale de l'entité
   */
  function toggleGeoSpeech(id) {
    if (currentSpeakingId === id) {
      stopGeoSpeech();
      return;
    }

    if (!selectedEntity || !selectedEntity.data) return;
    const data = selectedEntity.data;

    stopGeoSpeech();
    currentSpeakingId = id;
    const inspector = document.getElementById('geo-inspector-pane');
    if (inspector) inspector.innerHTML = renderInspectorCard();

    const textToRead = `${data.name}. ${data.chefLieu ? 'Chef-lieu : ' + data.chefLieu + '. ' : ''}${data.highestPeak ? 'Point culminant : ' + data.highestPeak + '. ' : ''}${data.length ? 'Longueur : ' + data.length + '. ' : ''}${data.description || data.highlights || ''}. Important pour l'entretien : ${data.interviewTip || ''}`;

    if (window.FrenchAIReader) {
      window.FrenchAIReader.speak(textToRead, {
        onEnd: () => {
          currentSpeakingId = null;
          const ins = document.getElementById('geo-inspector-pane');
          if (ins) ins.innerHTML = renderInspectorCard();
        },
        onError: () => {
          currentSpeakingId = null;
          const ins = document.getElementById('geo-inspector-pane');
          if (ins) ins.innerHTML = renderInspectorCard();
        }
      });
    } else if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(textToRead);
      utter.lang = 'fr-FR';
      utter.rate = 1.0;
      utter.onend = () => {
        currentSpeakingId = null;
        const ins = document.getElementById('geo-inspector-pane');
        if (ins) ins.innerHTML = renderInspectorCard();
      };
      window.speechSynthesis.speak(utter);
    }
  }

  function stopGeoSpeech() {
    if (window.FrenchAIReader) window.FrenchAIReader.stop();
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    currentSpeakingId = null;
  }

  // =========================================================================
  // MODE QUIZ CARTE (« POINTER & TROUVER »)
  // =========================================================================
  function startGeoQuiz() {
    quizCurrentIndex = 0;
    quizScore = 0;
    quizAnswered = false;
    renderGeographyUI();
  }

  function renderQuizView() {
    if (!geoData || !geoData.quizQuestions) return '<p>Aucune question disponible.</p>';
    const questions = geoData.quizQuestions;

    if (quizCurrentIndex >= questions.length) {
      // Quiz terminé
      const pct = Math.round((quizScore / questions.length) * 100);
      const passed = pct >= 80;
      return `
        <div class="geo-quiz-finished-card">
          <div class="geo-finished-icon ${passed ? 'success' : 'retry'}">
            <i class="fa-solid ${passed ? 'fa-award' : 'fa-rotate-left'}"></i>
          </div>
          <h3>${passed ? 'Félicitations ! Géographie Républicaine Validée' : 'Entraînement Recommandé'}</h3>
          <p class="geo-finished-score">Votre score : <strong>${quizScore} / ${questions.length}</strong> (${pct}%)</p>
          <p class="geo-finished-comment">
            ${passed 
              ? 'Excellent ! Vous maîtrisez les régions, fleuves, massifs et DROM essentiels pour l\'examen civique et l\'entretien en préfecture.' 
              : 'Revoyez les repères sur la carte et recommencez pour viser au moins 8/10.'}
          </p>
          <div class="geo-finished-actions">
            <button type="button" class="btn btn-primary" onclick="window.startGeoQuiz()">
              <i class="fa-solid fa-rotate-left"></i> Rejouer le Quiz Carte
            </button>
            <button type="button" class="btn btn-secondary" onclick="window.switchGeoTab('exploration')">
              <i class="fa-solid fa-map"></i> Retour au Mode Carte
            </button>
          </div>
        </div>
      `;
    }

    quizActiveQuestion = questions[quizCurrentIndex];

    return `
      <div class="geo-quiz-layout">
        <!-- Bannière de Question -->
        <div class="geo-quiz-banner">
          <div class="geo-quiz-header-row">
            <span class="geo-quiz-badge">Question ${quizCurrentIndex + 1} / ${questions.length}</span>
            <span class="geo-quiz-score-badge"><i class="fa-solid fa-star"></i> Score : ${quizScore} pts</span>
          </div>
          <h3 class="geo-quiz-question-text">${quizActiveQuestion.question}</h3>
          <p class="geo-quiz-instruction">
            <i class="fa-solid fa-hand-pointer"></i> 
            Cliquez directement sur l'élément correspondant sur la carte ou choisissez une réponse ci-dessous :
          </p>

          <!-- Choix multiples express -->
          <div class="geo-quiz-options-grid" id="geo-quiz-options">
            ${quizActiveQuestion.options.map(opt => `
              <button type="button" 
                      class="geo-quiz-opt-btn" 
                      onclick="window.handleQuizButtonAnswer('${opt.replace(/'/g, "\\'")}')">
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>

          <!-- Zone de feedback après réponse -->
          <div class="geo-quiz-feedback-box" id="geo-quiz-feedback" style="display:none;"></div>
        </div>

        <!-- Carte SVG pour pointer directement -->
        <div class="geo-quiz-map-container">
          ${renderFranceSvgMap()}
        </div>
      </div>
    `;
  }

  function handleQuizAnswerSelection(type, id) {
    if (quizAnswered || !quizActiveQuestion) return;

    const isMatch = (quizActiveQuestion.targetId === id) || 
                    (quizActiveQuestion.correct.toLowerCase().includes(id.toLowerCase()));

    processQuizResult(isMatch);
  }

  function handleQuizButtonAnswer(selectedOption) {
    if (quizAnswered || !quizActiveQuestion) return;

    const isMatch = (selectedOption === quizActiveQuestion.correct);
    processQuizResult(isMatch);
  }

  function processQuizResult(isCorrect) {
    quizAnswered = true;
    if (isCorrect) quizScore++;

    const feedbackBox = document.getElementById('geo-quiz-feedback');
    const optionsContainer = document.getElementById('geo-quiz-options');

    // Mettre en valeur les boutons
    if (optionsContainer) {
      optionsContainer.querySelectorAll('.geo-quiz-opt-btn').forEach(btn => {
        const text = btn.textContent.trim();
        if (text === quizActiveQuestion.correct) {
          btn.classList.add('correct');
        } else {
          btn.classList.add('faded');
        }
      });
    }

    if (feedbackBox) {
      feedbackBox.style.display = 'block';
      feedbackBox.className = `geo-quiz-feedback-box ${isCorrect ? 'feedback-correct' : 'feedback-error'}`;
      feedbackBox.innerHTML = `
        <div class="feedback-icon-row">
          <i class="fa-solid ${isCorrect ? 'fa-circle-check' : 'fa-circle-xmark'}"></i>
          <strong>${isCorrect ? 'Excellente réponse !' : 'Réponse incorrecte'}</strong>
        </div>
        <p><strong>Bonne réponse :</strong> ${quizActiveQuestion.correct}</p>
        <p class="feedback-tip"><i class="fa-solid fa-lightbulb"></i> <strong>Astuce Entretien :</strong> ${quizActiveQuestion.tip}</p>
        <button type="button" class="btn btn-primary btn-sm" onclick="window.nextGeoQuizQuestion()" style="margin-top:0.75rem;">
          Question suivante <i class="fa-solid fa-arrow-right"></i>
        </button>
      `;
    }

    // Mettre en valeur la cible sur la carte
    const targetEl = document.getElementById(`reg-${quizActiveQuestion.targetId}`) || 
                     document.getElementById(`riv-${quizActiveQuestion.targetId}`) || 
                     document.getElementById(`mtn-${quizActiveQuestion.targetId}`);
    if (targetEl) {
      targetEl.classList.add('quiz-highlight-target');
    }
  }

  function nextGeoQuizQuestion() {
    quizCurrentIndex++;
    quizAnswered = false;
    renderGeographyUI();
  }

  // =========================================================================
  // MODE TABLEAU DES REPÈRES GÉOGRAPHIQUES
  // =========================================================================
  function renderReperesView() {
    if (!geoData) return '<p>Données non chargées.</p>';

    return `
      <div class="geo-reperes-container">
        <!-- Section Fleuves -->
        <div class="geo-rep-card">
          <h4><i class="fa-solid fa-water" style="color:#0284c7;"></i> Les 5 Grands Fleuves Français</h4>
          <div class="geo-table-responsive">
            <table class="geo-summary-table">
              <thead>
                <tr>
                  <th>Fleuve</th>
                  <th>Longueur</th>
                  <th>Source</th>
                  <th>Embouchure</th>
                  <th>Villes principales</th>
                </tr>
              </thead>
              <tbody>
                ${geoData.rivers.map(r => `
                  <tr>
                    <td><strong>${r.name}</strong></td>
                    <td><span class="badge-pill">${r.length}</span></td>
                    <td>${r.source}</td>
                    <td>${r.mouth}</td>
                    <td>${r.cities}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Section Massifs Montagneux -->
        <div class="geo-rep-card">
          <h4><i class="fa-solid fa-mountain" style="color:#f59e0b;"></i> Les 5 Massifs Montagneux</h4>
          <div class="geo-table-responsive">
            <table class="geo-summary-table">
              <thead>
                <tr>
                  <th>Massif</th>
                  <th>Point culminant</th>
                  <th>Frontières / Localisation</th>
                  <th>Régions</th>
                </tr>
              </thead>
              <tbody>
                ${geoData.mountains.map(m => `
                  <tr>
                    <td><strong>${m.name}</strong></td>
                    <td><span class="badge-pill highlight">${m.highestPeak}</span></td>
                    <td>${m.borders}</td>
                    <td>${m.regions}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Section Outre-Mer (DROM) -->
        <div class="geo-rep-card">
          <h4><i class="fa-solid fa-earth-americas" style="color:#10b981;"></i> Les 5 DROM (Départements et Régions d'Outre-Mer)</h4>
          <div class="geo-table-responsive">
            <table class="geo-summary-table">
              <thead>
                <tr>
                  <th>Territoire</th>
                  <th>Statut</th>
                  <th>Chef-lieu</th>
                  <th>Océan / Localisation</th>
                  <th>Clé Entretien</th>
                </tr>
              </thead>
              <tbody>
                ${geoData.outremer.map(om => `
                  <tr>
                    <td><strong>${om.name} (${om.code || 'DOM'})</strong></td>
                    <td><span class="badge-pill">${om.statut}</span></td>
                    <td><strong>${om.chefLieu}</strong></td>
                    <td>${om.ocean}</td>
                    <td>${om.interviewTip}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Section Pays Frontaliers -->
        <div class="geo-rep-card">
          <h4><i class="fa-solid fa-flag" style="color:#ef4444;"></i> Les 8 Pays Frontaliers Terrestres</h4>
          <div class="geo-table-responsive">
            <table class="geo-summary-table">
              <thead>
                <tr>
                  <th>Pays frontalier</th>
                  <th>Orientation</th>
                  <th>Type de frontière</th>
                  <th>Capitale</th>
                </tr>
              </thead>
              <tbody>
                ${geoData.borders.map(b => `
                  <tr>
                    <td><strong>${b.name}</strong></td>
                    <td>${b.direction}</td>
                    <td>${b.type}</td>
                    <td>${b.capital}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    `;
  }

  // Écouteur Escape pour fermer la modale
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      const modal = document.getElementById('geography-modal');
      if (modal && modal.classList.contains('active')) {
        closeGeographyModal();
      }
    }
  });

  // Exposer les fonctions globalement
  window.openGeographyModal = openGeographyModal;
  window.closeGeographyModal = closeGeographyModal;
  window.switchGeoTab = switchGeoTab;
  window.setGeoLayer = setGeoLayer;
  window.selectGeoEntity = selectGeoEntity;
  window.handleMapElementClick = handleMapElementClick;
  window.toggleGeoSpeech = toggleGeoSpeech;
  window.startGeoQuiz = startGeoQuiz;
  window.handleQuizButtonAnswer = handleQuizButtonAnswer;
  window.nextGeoQuizQuestion = nextGeoQuizQuestion;

})();
