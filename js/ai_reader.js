/**
 * ==========================================================================
 * FRENCH AI AUDIO READER (Lecteur Vocal IA - Français B2)
 * ==========================================================================
 * Unified Text-to-Speech Engine dedicated exclusively to French language.
 * Enforces strictly French voices, prioritizes neural/studio voices
 * (Vivienne, Denise, Google français, Thomas, Audrey),
 * cleans HTML/abbreviations, and prevents English/fallback errors.
 */

(function(window) {
  'use strict';

  class FrenchAIReaderService {
    constructor() {
      this.voices = [];
      this.bestVoice = null;
      this.isSpeaking = false;
      this.activeButton = null;
      this.currentUtterance = null;
      this.initialized = false;
      this.defaultRate = 0.94; // Calm, clear French B2 pace
      this.init();
    }

    init() {
      if (!('speechSynthesis' in window)) {
        console.warn('FrenchAIReader: speechSynthesis is not supported by this browser.');
        return;
      }

      this.loadVoices();
      if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = () => this.loadVoices();
      }
    }

    loadVoices() {
      try {
        const allVoices = window.speechSynthesis.getVoices();
        if (!allVoices || allVoices.length === 0) return;

        // Strictly French only voices (fr, fr-FR, fr-CA, fr-BE, fr-CH)
        this.voices = allVoices.filter(v => v.lang && v.lang.toLowerCase().startsWith('fr'));
        this.bestVoice = this.resolveBestFrenchVoice(this.voices);
        this.initialized = true;
      } catch (e) {
        console.warn('FrenchAIReader voice loading error:', e);
      }
    }

    resolveBestFrenchVoice(frenchVoices) {
      if (!frenchVoices || frenchVoices.length === 0) return null;

      // 1. Check for Microsoft Vivienne / Denise / Henri (same studio neural voice as Edge-TTS)
      const vivienne = frenchVoices.find(v => {
        const n = v.name.toLowerCase();
        return n.includes('vivienne') || n.includes('denise') || n.includes('henri');
      });
      if (vivienne) return vivienne;

      // 2. Online / Natural / Neural French voices
      const neural = frenchVoices.find(v => {
        const n = v.name.toLowerCase();
        return n.includes('natural') || n.includes('neural') || n.includes('online') || n.includes('multilingual');
      });
      if (neural) return neural;

      // 3. Google français (High quality Chrome neural French voice)
      const googleFr = frenchVoices.find(v => v.name.toLowerCase().includes('google') && v.lang.toLowerCase().startsWith('fr'));
      if (googleFr) return googleFr;

      // 4. Apple Enhanced / Premium French Voices (Thomas, Audrey, Amélie, Jacques, Siri)
      const appleEnhanced = frenchVoices.find(v => {
        const n = v.name.toLowerCase();
        return (n.includes('enhanced') || n.includes('premium')) && (n.includes('thomas') || n.includes('audrey') || n.includes('amélie'));
      });
      if (appleEnhanced) return appleEnhanced;

      const appleStandard = frenchVoices.find(v => {
        const n = v.name.toLowerCase();
        return n.includes('thomas') || n.includes('audrey') || n.includes('amélie') || n.includes('jacques') || n.includes('siri');
      });
      if (appleStandard) return appleStandard;

      // 5. France French (fr-FR)
      const frFR = frenchVoices.find(v => v.lang.toLowerCase() === 'fr-fr');
      if (frFR) return frFR;

      // 6. Any Francophone voice (fr-CA, fr-BE, fr-CH)
      return frenchVoices[0];
    }

    getVoiceName() {
      if (this.bestVoice) return this.bestVoice.name;
      return "Voix IA Française (Studio B2)";
    }

    /**
     * Clean and normalize French text for speech:
     * - Expands common citizenship abbreviations
     * - Converts HTML/markdown into natural breaths
     * - Strips symbols and metadata
     */
    cleanTextForSpeech(text) {
      if (!text) return "";
      let t = text;

      // HTML breaks and paragraphs to natural pauses
      t = t.replace(/<br\s*\/?>/gi, '. ');
      t = t.replace(/<\/p>/gi, '. ');
      t = t.replace(/<\/div>/gi, '. ');
      t = t.replace(/<\/li>/gi, '. ');
      t = t.replace(/<[^>]+>/g, ' ');

      // Common French administrative & civics abbreviations expansion
      t = t.replace(/\b1er\b/gi, 'premier');
      t = t.replace(/\b1ère\b/gi, 'première');
      t = t.replace(/\bVe\b/g, 'Cinquième');
      t = t.replace(/\bIVe\b/g, 'Quatrième');
      t = t.replace(/\bIIIe\b/g, 'Troisième');
      t = t.replace(/\bIIe\b/g, 'Deuxième');
      t = t.replace(/\bIère\b/g, 'Première');
      t = t.replace(/\bVème\b/gi, 'Cinquième');
      t = t.replace(/\bIVème\b/gi, 'Quatrième');
      t = t.replace(/\bIIIème\b/gi, 'Troisième');
      t = t.replace(/\bart\.\s*(\d+)/gi, 'article $1');
      t = t.replace(/\bUE\b/g, "Union Européenne");
      t = t.replace(/\bDROM\b/g, "Départements et Régions d'Outre-Mer");
      t = t.replace(/\bCOM\b/g, "Collectivités d'Outre-Mer");
      t = t.replace(/\bIVG\b/g, "Interruption Volontaire de Grossesse");
      t = t.replace(/\bSAMU\b/g, "Samu");
      t = t.replace(/\bSMIC\b/g, "Smic");
      t = t.replace(/\bCECRL\b/g, "Cadre européen pour les langues");
      t = t.replace(/\bex\s*:/gi, "par exemple :");

      // Clean bullet points and symbols
      t = t.replace(/[•★▪►✔✓✗✖*#]/g, ' ');
      t = t.replace(/~/g, ' ');
      t = t.replace(/&nbsp;/gi, ' ');
      t = t.replace(/&amp;/gi, ' et ');
      t = t.replace(/&quot;/gi, '"');
      t = t.replace(/&lt;/gi, ' ');
      t = t.replace(/&gt;/gi, ' ');
      t = t.replace(/[\(\)\[\]\{\}]/g, ' ');

      // Strip image filenames
      t = t.replace(/fc_[a-zA-Z0-9_-]+\.png/gi, '');
      t = t.replace(/assets\/[^\s]+/gi, '');

      // Normalize spaces
      t = t.replace(/\s+/g, ' ').trim();
      return t;
    }

    /**
     * Speak text using French AI Voice.
     * Toggles playback off if already speaking on the given button.
     */
    speak(rawText, options = {}) {
      if (!('speechSynthesis' in window)) {
        if (options.onError) options.onError(new Error("Synthèse vocale non disponible."));
        return;
      }

      const btn = options.buttonElement || null;

      // Toggle off if currently speaking on this exact button
      if (this.isSpeaking && this.activeButton === btn && btn !== null) {
        this.stop();
        return;
      }

      this.stop();

      const clean = this.cleanTextForSpeech(rawText);
      if (!clean) return;

      if (!this.bestVoice || this.voices.length === 0) {
        this.loadVoices();
      }

      const utter = new SpeechSynthesisUtterance(clean);
      utter.lang = 'fr-FR'; // Strictly French language
      if (this.bestVoice) {
        utter.voice = this.bestVoice;
        utter.lang = this.bestVoice.lang || 'fr-FR';
      }

      utter.rate = options.rate || this.defaultRate;
      utter.pitch = options.pitch || 1.0;

      this.isSpeaking = true;
      this.currentUtterance = utter;
      this.activeButton = btn;

      if (btn) btn.classList.add('speaking');
      if (options.onStart) options.onStart();

      utter.onend = () => {
        this.isSpeaking = false;
        this.currentUtterance = null;
        if (this.activeButton) {
          this.activeButton.classList.remove('speaking');
          this.activeButton = null;
        }
        if (options.onEnd) options.onEnd();
      };

      utter.onerror = (err) => {
        this.isSpeaking = false;
        this.currentUtterance = null;
        if (this.activeButton) {
          this.activeButton.classList.remove('speaking');
          this.activeButton = null;
        }
        if (options.onError) options.onError(err);
      };

      window.speechSynthesis.speak(utter);
    }

    stop() {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
      this.isSpeaking = false;
      this.currentUtterance = null;
      if (this.activeButton) {
        this.activeButton.classList.remove('speaking');
        this.activeButton = null;
      }
      document.querySelectorAll('.action-btn.speaking, .quiz-audio-btn.speaking').forEach(el => {
        el.classList.remove('speaking');
      });
    }
  }

  // Instantiate and export globally
  window.FrenchAIReader = new FrenchAIReaderService();

})(window);
