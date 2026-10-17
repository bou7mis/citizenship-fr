#!/usr/bin/env python3
"""
Video Lessons Generator for Module 5 and Module 6 of Livret du Citoyen 2026.
Module 5: Vivre dans la Société Française (3 chaps)
Module 6: Guide de l'Examen Civique et Entretien 2026 (1 chap)
"""

import json

def get_module5_6_lessons():
    return {
        # =========================================================================
        # MODULE 5: VIVRE DANS LA SOCIÉTÉ FRANÇAISE
        # =========================================================================
        "m5-c1": {
            "chapterId": "m5-c1",
            "moduleId": "module-5",
            "title": "La Vie Quotidienne, Santé et Sécurité",
            "subtitle": "Numéros d'urgence (15, 17, 18, 112), Carte Vitale, Sécurité sociale et civisme",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Les Numéros d'Urgence Gratuits",
                    "badge": "Sécurité au Quotidien",
                    "durationSeconds": 20,
                    "visualTheme": "tricolore",
                    "heading": "Les Services d'Urgence en France",
                    "subheading": "Accessibles 24h/24 et 7j/7 gratuitement depuis tout téléphone",
                    "icon": "fa-phone-volume",
                    "keyPoints": [
                        "15 : Le SAMU (urgence médicale vitale, médecin régulateur)",
                        "17 : Police Secours et Gendarmerie (infraction, danger immédiat)",
                        "18 : Les Sapeurs-Pompiers (incendies, accidents de la route, secours)",
                        "112 : Numéro d'urgence européen unique (fonctionne sans carte SIM)"
                    ],
                    "narrationText": "Bienvenue dans cette leçon consacrée à la vie quotidienne et à la santé. En France, quatre numéros d'urgence gratuits sauvent des vies au quotidien : le 15 pour le SAMU, le 17 pour la police, le 18 pour les pompiers, et le 112 pour toute l'Europe.",
                    "takeaway": "L'agent vous demandera très souvent à quoi correspondent le 15, le 17 et le 18.",
                    "audioSrc": "audio/video_lessons/m5-c1/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "La Santé & L'Assurance Maladie",
                    "badge": "Protection Sociale",
                    "durationSeconds": 20,
                    "visualTheme": "liberte",
                    "heading": "L'Accès Universel aux Soins",
                    "subheading": "Protection Universelle Maladie (PUMA) et Carte Vitale",
                    "icon": "fa-heart-pulse",
                    "keyPoints": [
                        "PUMA : toute personne résidant en France de manière stable a droit aux soins",
                        "Carte Vitale : carte électronique personnelle attestant des droits ouverts",
                        "Médecin traitant : garantit un parcours de soins coordonné et un meilleur remboursement",
                        "Complémentaire santé solidaire (CSS) : pour les personnes aux revenus modestes"
                    ],
                    "narrationText": "Le système de santé français est fondé sur la solidarité universelle. Grâce à la Protection Universelle Maladie et à la Carte Vitale, toute personne résidant régulièrement en France a droit à la prise en charge de ses dépenses de santé.",
                    "takeaway": "Le médecin traitant permet d'être remboursé au taux maximal de la Sécurité sociale.",
                    "audioSrc": "audio/video_lessons/m5-c1/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "La Sécurité Publique & Les Forces de l'Ordre",
                    "badge": "Police & Gendarmerie",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Protéger la Population et Maintenir l'Ordre",
                    "subheading": "Police nationale en zone urbaine et Gendarmerie en zone rurale",
                    "icon": "fa-shield-halved",
                    "keyPoints": [
                        "Police nationale : fonctionnaires civils opérant dans les grandes villes et agglomérations",
                        "Gendarmerie nationale : militaires rattachés au ministère de l'Intérieur en zone rurale et périurbaine",
                        "Police municipale : agents de proximité placés sous l'autorité directe du maire",
                        "Toutes les forces de l'ordre sont soumises à un code de déontologie strict"
                    ],
                    "narrationText": "La sécurité publique est assurée conjointement par la Police nationale dans les grandes villes et la Gendarmerie nationale dans les zones rurales et périurbaines. Elles agissent sous l'autorité des lois pour garantir la tranquillité de tous.",
                    "takeaway": "La gendarmerie a un statut militaire, tandis que la police est civile.",
                    "audioSrc": "audio/video_lessons/m5-c1/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "Le Civisme et le Vivre-Ensemble",
                    "badge": "Tranquillité Publique",
                    "durationSeconds": 18,
                    "visualTheme": "fraternite",
                    "heading": "Le Respect d'Autrui dans l'Espace Public",
                    "subheading": "Tranquillité du voisinage, propreté et écocitoyenneté",
                    "icon": "fa-people-roof",
                    "keyPoints": [
                        "Respect de la tranquillité nocturne et interdiction du tapage injurieux",
                        "Respect de la propreté urbaine et tri sélectif des déchets ménagers",
                        "Courtoisie et respect mutuel dans les transports en commun et commerces",
                        "Signalement des maltraitances et solidarité avec les aînés et personnes fragiles"
                    ],
                    "narrationText": "Vivre en France implique un attachement quotidien au civisme : respect de la tranquillité des voisins, propreté des espaces partagés, protection de l'environnement et politesse dans les relations de voisinage.",
                    "takeaway": "Le civisme est la traduction concrète du respect républicain au quotidien.",
                    "audioSrc": "audio/video_lessons/m5-c1/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Numéros & Urgences",
                    "badge": "Questions Pratiques",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "La Question Incontournable de l'Agent",
                    "subheading": "« Quel numéro appelez-vous en cas d'incendie ou d'urgence médicale ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "15 pour le SAMU (malaise, accident cardiaque, détresse respiratoire)",
                        "18 pour les pompiers (incendie, accident de la route)",
                        "17 pour la police (cambriolage, agression, vol)",
                        "112 pour toute urgence depuis un portable partout dans l'Union européenne"
                    ],
                    "narrationText": "L'instructeur vous demandera à coup sûr quel numéro vous composez pour appeler les pompiers ou le SAMU. Donnez immédiatement le dix-huit pour les pompiers et le quinze pour le SAMU pour prouver vos réflexes citoyens.",
                    "takeaway": "Connaître le 15, le 17 et le 18 est indispensable pour réussir l'entretien.",
                    "audioSrc": "audio/video_lessons/m5-c1/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos réflexes d'urgence",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Quel numéro d'urgence devez-vous composer pour joindre le SAMU en cas d'urgence médicale vitale ?",
                        "options": [
                            "Le 15",
                            "Le 17",
                            "Le 18"
                        ],
                        "correctIndex": 0,
                        "explanation": "Le 15 est le numéro d'urgence médical national qui permet de joindre directement le Service d'Aide Médicale Urgente (SAMU)."
                    },
                    "narrationText": "Testez vos réflexes : quel numéro devez-vous composer pour joindre le SAMU en cas d'urgence médicale ? Choisissez la bonne réponse.",
                    "takeaway": "Bravo ! Vos réflexes de sécurité sont au point.",
                    "audioSrc": "audio/video_lessons/m5-c1/scene_6.mp3"
                }
            ]
        },

        "m5-c2": {
            "chapterId": "m5-c2",
            "moduleId": "module-5",
            "title": "Travailler en France et Droits des Salariés",
            "subtitle": "Contrat de travail, CDI/CDD, SMIC, temps de travail (35h) et formation",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Le Droit du Travail en France",
                    "badge": "Code du Travail",
                    "durationSeconds": 18,
                    "visualTheme": "tricolore",
                    "heading": "Le Travail : Valeur d'Émancipation et d'Intégration",
                    "subheading": "Encadré par le Code du travail et les conventions collectives",
                    "icon": "fa-briefcase",
                    "keyPoints": [
                        "Le travail permet l'indépendance financière et l'insertion sociale",
                        "Le Code du travail protège la santé et les droits de chaque salarié",
                        "Interdiction stricte de toute discrimination à l'embauche (origine, sexe, âge, handicap)",
                        "Obligation d'un contrat de travail écrit ou d'une déclaration préalable"
                    ],
                    "narrationText": "Bienvenue dans cette leçon consacrée au travail. En France, le travail est un droit et un facteur majeur d'intégration républicaine. Les relations entre employeurs et employés sont rigoureusement encadrées par le Code du travail.",
                    "takeaway": "L'intégration professionnelle par le travail est un critère d'assimilation essentiel.",
                    "audioSrc": "audio/video_lessons/m5-c2/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Les Types de Contrats : CDI & CDD",
                    "badge": "Contrats de Travail",
                    "durationSeconds": 20,
                    "visualTheme": "liberte",
                    "heading": "CDI, CDD et Période d'Essai",
                    "subheading": "Le contrat à durée indéterminée comme norme générale",
                    "icon": "fa-file-signature",
                    "keyPoints": [
                        "CDI (Contrat à Durée Indéterminée) : la forme normale et générale de l'emploi",
                        "CDD (Contrat à Durée Déterminée) : réservé à des missions temporaires et précises",
                        "Période d'essai : permet d'évaluer les compétences du salarié",
                        "Protection contre le licenciement abusif : motif réel et sérieux obligatoire"
                    ],
                    "narrationText": "La loi française privilégie le Contrat à Durée Indéterminée, ou CDI, garantissant la stabilité de l'emploi. Le CDD ne peut être conclu que pour des motifs temporaires légaux comme le remplacement d'un salarié ou un surcroît d'activité.",
                    "takeaway": "Le CDI est la forme normale d'embauche en France.",
                    "audioSrc": "audio/video_lessons/m5-c2/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Le SMIC et la Durée Légale du Travail",
                    "badge": "Rémunération & 35 Heures",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Le SMIC et les 35 Heures",
                    "subheading": "Salaire minimum interprofessionnel de croissance et repos obligatoire",
                    "icon": "fa-coins",
                    "keyPoints": [
                        "SMIC : salaire horaire minimal en dessous duquel aucun salarié ne peut être payé",
                        "Revalorisé automatiquement chaque année en fonction de l'inflation",
                        "Durée légale du travail fixée à 35 heures par semaine (au-delà : heures supplémentaires majorées)",
                        "Droit à 5 semaines de congés payés par an pour tout salarié à temps plein"
                    ],
                    "narrationText": "Tout travailleur en France bénéficie du Salaire Minimum de Croissance, ou SMIC, qui garantit un seuil de rémunération décent. La durée légale du travail est de trente-cinq heures hebdomadaires, avec cinq semaines de congés payés annuels.",
                    "takeaway": "Les 5 semaines de congés payés et les 35 heures sont des acquis sociaux emblématiques.",
                    "audioSrc": "audio/video_lessons/m5-c2/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "La Liberté Syndicale et le Dialogue Social",
                    "badge": "Droit Syndical & Grève",
                    "durationSeconds": 20,
                    "visualTheme": "fraternite",
                    "heading": "Représentation du Personnel et Dialogue Social",
                    "subheading": "Comité Social et Économique (CSE) et syndicats",
                    "icon": "fa-users-gear",
                    "keyPoints": [
                        "Liberté syndicale reconnue depuis la loi Waldeck-Rousseau de 1884",
                        "Droit de grève garanti par le préambule de la Constitution de 1946",
                        "Comité Social et Économique (CSE) obligatoire dès 11 salariés",
                        "Formation professionnelle continue accessible tout au long de la carrière via le CPF"
                    ],
                    "narrationText": "Chaque travailleur a le droit d'adhérer au syndicat de son choix et d'exercer le droit de grève dans le respect de la loi. Dans les entreprises, les représentants élus du personnel veillent aux conditions de travail et à la sécurité des salariés.",
                    "takeaway": "La liberté syndicale a été reconnue en France en 1884.",
                    "audioSrc": "audio/video_lessons/m5-c2/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Situation Professionnelle",
                    "badge": "Parcours Personnel",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Questions sur Votre Emploi",
                    "subheading": "« Que faites-vous en France ? Quel est votre parcours professionnel ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Décrivez votre métier avec précision et valorisez vos compétences",
                        "Expliquez en quoi votre activité est utile à la société et à vos collègues",
                        "Montrez votre autonomie financière et votre stabilité résidentielle",
                        "Évoquez vos perspectives d'évolution ou vos projets professionnels futurs"
                    ],
                    "narrationText": "L'instructeur vous demandera de décrire votre travail actuel. Soyez précis, fier de votre parcours et montrez que votre activité professionnelle vous permet de subvenir à vos besoins et de contribuer activement à l'économie française.",
                    "takeaway": "Montrer que vous êtes inséré et autonome financièrement est décisif.",
                    "audioSrc": "audio/video_lessons/m5-c2/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos repères sur le monde du travail",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Combien de semaines de congés payés par an un salarié à temps plein acquiert-il en France ?",
                        "options": [
                            "3 semaines",
                            "4 semaines",
                            "5 semaines"
                        ],
                        "correctIndex": 2,
                        "explanation": "En France, tout salarié bénéficie d'au moins 5 semaines de congés payés par an (soit 30 jours ouvrables ou 25 jours ouvrés)."
                    },
                    "narrationText": "Testez vos connaissances : combien de semaines de congés payés un salarié à temps plein a-t-il droit en France chaque année ? Cliquez sur la bonne réponse.",
                    "takeaway": "Bravo ! Vous connaissez les droits fondamentaux des salariés en France.",
                    "audioSrc": "audio/video_lessons/m5-c2/scene_6.mp3"
                }
            ]
        },

        "m5-c3": {
            "chapterId": "m5-c3",
            "moduleId": "module-5",
            "title": "La Famille, l'Éducation et la Protection de l'Enfance",
            "subtitle": "École obligatoire de 3 à 16 ans, autorité parentale partagée et laïcité scolaire",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "L'École de la République",
                    "badge": "Les Lois Jules Ferry",
                    "durationSeconds": 20,
                    "visualTheme": "tricolore",
                    "heading": "L'École Publique : Gratuite, Laïque et Obligatoire",
                    "subheading": "Les lois historiques de Jules Ferry (1881-1882)",
                    "icon": "fa-graduation-cap",
                    "keyPoints": [
                        "Lois de 1881 et 1882 : école primaire publique gratuite et laïque pour tous",
                        "Instruction obligatoire de 3 à 16 ans pour tous les enfants résidant en France",
                        "L'école transmet les savoirs fondamentaux et les valeurs de la République",
                        "L'égalité des chances : l'ascenseur républicain fondé sur le mérite"
                    ],
                    "narrationText": "Bienvenue dans cette leçon consacrée à la famille et à l'éducation. L'école républicaine, fondée par Jules Ferry à la fin du dix-neuvième siècle, est gratuite, laïque et obligatoire pour tous les enfants de trois à seize ans.",
                    "takeaway": "L'instruction est obligatoire dès l'âge de 3 ans.",
                    "audioSrc": "audio/video_lessons/m5-c3/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "La Laïcité à l'École",
                    "badge": "Loi du 15 mars 2004",
                    "durationSeconds": 20,
                    "visualTheme": "liberte",
                    "heading": "La Laïcité dans les Écoles Publiques",
                    "subheading": "Protéger les élèves de toute pression et préserver la neutralité",
                    "icon": "fa-school",
                    "keyPoints": [
                        "Loi du 15 mars 2004 : interdiction des signes religieux ostensibles dans les écoles, collèges et lycées publics",
                        "Charte de la laïcité à l'école affichée dans tous les établissements scolaires",
                        "Respect du programme national : assiduité obligatoire à tous les cours (dont sport et sciences)",
                        "L'école est un espace d'émancipation, de tolérance et d'esprit critique"
                    ],
                    "narrationText": "À l'école publique, la loi du quinze mars deux mille quatre interdit le port de signes ou tenues par lesquels les élèves manifestent ostensiblement une appartenance religieuse. Cette règle garantit la neutralité de l'enseignement et protège les enfants de toute pression.",
                    "takeaway": "La loi du 15 mars 2004 s'applique aux écoles, collèges et lycées publics.",
                    "audioSrc": "audio/video_lessons/m5-c3/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "L'Autorité Parentale Conjointe",
                    "badge": "Droit de la Famille",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "L'Égalité des Parents dans l'Éducation",
                    "subheading": "Autorité parentale conjointe et protection de l'intérêt supérieur de l'enfant",
                    "icon": "fa-children",
                    "keyPoints": [
                        "Le père et la mère ont exactement les mêmes droits et les mêmes devoirs envers leurs enfants",
                        "Obligation d'éducation, de scolarisation, d'entretien et de surveillance",
                        "Les décisions importantes (santé, scolarité, religion) sont prises d'un commun accord",
                        "En cas de séparation, l'autorité parentale reste conjointe pour le bien de l'enfant"
                    ],
                    "narrationText": "En droit français, l'autorité parentale appartient conjointement au père et à la mère jusqu'à la majorité de l'enfant. Les parents ont le devoir partagé de nourrir, protéger, surveiller et instruire leurs enfants.",
                    "takeaway": "L'autorité parentale est strictement conjointe et égale entre père et mère.",
                    "audioSrc": "audio/video_lessons/m5-c3/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "La Protection de l'Enfance & Le 119",
                    "badge": "Protection des Mineurs",
                    "durationSeconds": 18,
                    "visualTheme": "fraternite",
                    "heading": "Protéger les Enfants contre les Violences",
                    "subheading": "Le numéro d'urgence 119 (Enfance en Danger)",
                    "icon": "fa-hands-holding-child",
                    "keyPoints": [
                        "Interdiction formelle des violences physiques, des châtiments corporels et des humiliations",
                        "119 : numéro national gratuit d'appel d'urgence pour l'Enfance en Danger",
                        "Aide Sociale à l'Enfance (ASE) gérée par les conseils départementaux",
                        "Juge des enfants : magistrat spécialisé chargé de protéger les mineurs en danger"
                    ],
                    "narrationText": "La République protège rigoureusement chaque enfant contre toute forme de maltraitance, de négligence ou de violence physique. Le cent dix-neuf est le numéro d'urgence gratuit et anonyme dédié à l'enfance en danger.",
                    "takeaway": "Le 119 est le numéro d'urgence dédié à l'Enfance en Danger.",
                    "audioSrc": "audio/video_lessons/m5-c3/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Éducation des Enfants",
                    "badge": "Questions Éducatives",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Question Type de l'Instructeur",
                    "subheading": "« Quel âge a l'école obligatoire ? Comment élevez-vous vos enfants ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Âges de l'école obligatoire : de 3 ans à 16 ans",
                        "Précisez que vos enfants sont assidus à tous les cours scolaires",
                        "Affirmez votre volonté de leur transmettre la langue française et l'esprit républicain",
                        "Mentionnez la participation aux réunions parents-professeurs et aux devoirs"
                    ],
                    "narrationText": "L'agent vous demandera à quel âge commence l'école obligatoire et comment vous suivez la scolarité de vos enfants. Répondez que l'instruction commence dès trois ans et montrez votre investissement dans leur réussite scolaire.",
                    "takeaway": "Retenez l'âge de 3 ans fixé depuis la rentrée 2019.",
                    "audioSrc": "audio/video_lessons/m5-c3/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos repères sur l'instruction obligatoire",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "En France, à partir de quel âge l'instruction est-elle obligatoire pour tous les enfants ?",
                        "options": [
                            "Dès l'âge de 3 ans",
                            "Dès l'âge de 6 ans",
                            "Dès l'âge de 7 ans"
                        ],
                        "correctIndex": 0,
                        "explanation": "Depuis la loi pour une école de la confiance entrée en vigueur à la rentrée 2019, l'instruction est obligatoire dès l'âge de 3 ans (école maternelle)."
                    },
                    "narrationText": "Vérifions vos acquis : à partir de quel âge l'instruction est-elle obligatoire pour les enfants en France ? Cliquez sur la bonne réponse.",
                    "takeaway": "Bravo ! L'instruction obligatoire dès 3 ans est un repère essentiel.",
                    "audioSrc": "audio/video_lessons/m5-c3/scene_6.mp3"
                }
            ]
        },

        # =========================================================================
        # MODULE 6: GUIDE DE L'EXAMEN CIVIQUE ET ENTRETIEN 2026
        # =========================================================================
        "m6-c1": {
            "chapterId": "m6-c1",
            "moduleId": "module-6",
            "title": "La Réforme 2026 : Examen Civique et Niveau B2",
            "subtitle": "Nouveau test civique standardisé, exigence linguistique B2 et déroulement de l'entretien",
            "totalScenes": 6,
            "estimatedDuration": "2 min 10",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "La Réforme Historique de la Naturalisation 2026",
                    "badge": "Nouveautés Réglementaires 2026",
                    "durationSeconds": 20,
                    "visualTheme": "tricolore",
                    "heading": "Les 2 Changements Majeurs de 2026",
                    "subheading": "Examen civique standardisé et exigence de français au niveau B2",
                    "icon": "fa-certificate",
                    "keyPoints": [
                        "1. Examen civique obligatoire : QCM standardisé de 40 questions sur ordinateur",
                        "Seuil de réussite fixé à 80 % (32 bonnes réponses sur 40 exigées)",
                        "2. Niveau de langue française relevé au niveau B2 (au lieu de B1 auparavant)",
                        "L'entretien individuel en préfecture valide l'assimilation globale"
                    ],
                    "narrationText": "Bienvenue dans cette capsule cruciale consacrée à la Réforme deux mille vingt-six de la naturalisation. Deux exigences majeures s'appliquent désormais : la réussite à un examen civique officiel de quarante questions et la maîtrise du français au niveau B2.",
                    "takeaway": "L'examen civique 2026 exige au minimum 32 bonnes réponses sur 40 (80 %).",
                    "audioSrc": "audio/video_lessons/m6-c1/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "L'Examen Civique Standardisé (QCM)",
                    "badge": "Format de l'Examen",
                    "durationSeconds": 22,
                    "visualTheme": "liberte",
                    "heading": "Modalités de l'Examen Civique Officiel",
                    "subheading": "40 questions aléatoires en 45 minutes chrono",
                    "icon": "fa-desktop",
                    "keyPoints": [
                        "Répartition équilibrée : Principes républicains, Institutions, Histoire, Géographie et Société",
                        "Passé dans un centre d'examen agréé ou en préfecture sur tablette sécurisée",
                        "Attestation de réussite valable 2 ans pour la complétude du dossier",
                        "Notre simulateur d'examen 2026 vous entraîne exactement dans ces conditions"
                    ],
                    "narrationText": "L'examen civique comporte quarante questions à choix multiples tirées au sort, à compléter en quarante-cinq minutes. Il évalue votre compréhension des valeurs républicaines, des institutions, de l'histoire et de la société française.",
                    "takeaway": "Entraînez-vous régulièrement sur notre simulateur d'examen blanc pour atteindre 80 %.",
                    "audioSrc": "audio/video_lessons/m6-c1/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Le Niveau B2 en Langue Française",
                    "badge": "Exigence B2",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Comprendre et S'Exprimer avec Aisance (B2)",
                    "subheading": "Compréhension orale, écrite et expression spontanée",
                    "icon": "fa-comments",
                    "keyPoints": [
                        "Niveau B2 : utilisateur indépendant capable de participer activement à une discussion",
                        "Comprendre l'essentiel d'émissions de radio, d'articles de presse et de discours civiques",
                        "Justification par diplôme français ou attestation officielle (TCF, TEF, DELF B2)",
                        "L'agent instructeur évalue votre spontanéité et la richesse de votre vocabulaire"
                    ],
                    "narrationText": "Le passage au niveau B2 exige de pouvoir exprimer son opinion avec clarté, comprendre l'actualité et échanger spontanément en français. Vous devez fournir une attestation linguistique reconnue ou un diplôme d'études supérieures françaises.",
                    "takeaway": "Le niveau B2 remplace définitivement l'ancien niveau B1 pour la naturalisation.",
                    "audioSrc": "audio/video_lessons/m6-c1/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "Le Déroulement de l'Entretien en Préfecture",
                    "badge": "L'Entretien Individuel",
                    "durationSeconds": 22,
                    "visualTheme": "fraternite",
                    "heading": "L'Entretien d'Assimilation",
                    "subheading": "30 à 45 minutes d'échange face à un agent de l'État",
                    "icon": "fa-user-check",
                    "keyPoints": [
                        "Vérification de la loyauté, de l'adhésion aux valeurs et des motivations",
                        "Questions sur votre parcours personnel, professionnel, associatif et familial",
                        "Questions précises de culture générale et d'actualité française",
                        "Signature finale de la Charte des droits et devoirs du citoyen français"
                    ],
                    "narrationText": "L'entretien d'assimilation en préfecture dure entre trente et quarante-cinq minutes. L'agent évalue votre loyauté envers la République, vos motivations personnelles à devenir français et votre adhésion sincère aux principes de liberté, d'égalité et de laïcité.",
                    "takeaway": "La motivation personnelle et l'adhésion aux valeurs sont au cœur de l'entretien.",
                    "audioSrc": "audio/video_lessons/m6-c1/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Clés pour le Jour de l'Entretien",
                    "badge": "Conseils Stratégiques",
                    "durationSeconds": 20,
                    "visualTheme": "interview",
                    "heading": "Les 4 Règles d'Or pour Réussir",
                    "subheading": "Ponctualité, tenue correcte, franchise et sérénité",
                    "icon": "fa-star",
                    "keyPoints": [
                        "Arrivez 15 minutes à l'avance avec votre dossier original et vos pièces d'identité",
                        "Adoptez une tenue soignée et professionnelle témoignant de votre respect pour l'institution",
                        "Répondez avec franchise et bienveillance, sans arrogance ni précipitation",
                        "Si vous hésitez sur une question, restez calme et expliquez votre raisonnement"
                    ],
                    "narrationText": "Pour le jour J, préparez soigneusement vos originaux et arrivez en avance. Restez souriant, posé et confiant. Montrez votre fierté de rejoindre la communauté nationale et votre engagement à faire vivre les valeurs de la République.",
                    "takeaway": "La sérénité et la clarté d'expression font la différence auprès de l'agent.",
                    "audioSrc": "audio/video_lessons/m6-c1/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos repères sur la Réforme 2026",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Quel est le seuil de réussite exigé à l'examen civique officiel de 40 questions introduit par la Réforme 2026 ?",
                        "options": [
                            "50 % (20 bonnes réponses sur 40)",
                            "65 % (26 bonnes réponses sur 40)",
                            "80 % (32 bonnes réponses sur 40)"
                        ],
                        "correctIndex": 2,
                        "explanation": "L'examen civique officiel standardisé de 40 questions requiert un score minimal de 80 % de bonnes réponses (soit 32/40) pour être validé."
                    },
                    "narrationText": "Testez votre connaissance de la Réforme deux mille vingt-six : quel est le score minimal requis à l'examen civique ? Choisissez la bonne réponse pour valider cette ultime leçon.",
                    "takeaway": "Félicitations ! Vous avez validé l'ensemble des capsules e-learning du Livret du Citoyen 2026.",
                    "audioSrc": "audio/video_lessons/m6-c1/scene_6.mp3"
                }
            ]
        }
    }

def update_module5_6():
    with open("data/video_lessons.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    new_lessons = get_module5_6_lessons()
    for k, v in new_lessons.items():
        data["lessons"][k] = v

    with open("data/video_lessons.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated Module 5 and 6 lessons. Total lessons now: {len(data['lessons'])}")

if __name__ == "__main__":
    update_module5_6()
