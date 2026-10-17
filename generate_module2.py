#!/usr/bin/env python3
"""
Full Video Database Generator for all 18 Chapters of Livret du Citoyen 2026.
Creates rich structured video scripts with 5 to 6 scenes per chapter:
- Scene 1: Introduction & Repères Officiels
- Scene 2: Premier Pilier / Grand Thème Clé
- Scene 3: Deuxième Pilier / Fondements Juridiques & Dates
- Scene 4: Troisième Pilier / Application & Société
- Scene 5: Conseils Préfecture & Pièges de l'Entretien
- Scene 6: Mini-Quiz Vidéo / Checkpoint Interactif
"""

import json

def get_full_lessons():
    return {
        # =========================================================================
        # MODULE 2: SYSTÈME INSTITUTIONNEL ET POLITIQUE
        # =========================================================================
        "m2-c1": {
            "chapterId": "m2-c1",
            "moduleId": "module-2",
            "title": "La Séparation des Pouvoirs et l'État de Droit",
            "subtitle": "Pouvoirs exécutif, législatif, judiciaire et hiérarchie des normes",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Le Principe de Séparation des Pouvoirs",
                    "badge": "Fondement Démocratique",
                    "durationSeconds": 18,
                    "visualTheme": "tricolore",
                    "heading": "L'Équilibre Démocratique",
                    "subheading": "Théorisé par Montesquieu dans l'Esprit des Lois (1748)",
                    "icon": "fa-scale-balanced",
                    "keyPoints": [
                        "Éviter la concentration du pouvoir entre les mains d'un seul homme",
                        "Trois branches distinctes et indépendantes les unes des autres",
                        "Garantie fondamentale contre l'arbitraire et la tyrannie",
                        "Inscrit à l'article 16 de la Déclaration des Droits de 1789"
                    ],
                    "narrationText": "Bienvenue dans cette leçon sur les institutions françaises. Pour empêcher tout abus de pouvoir, la démocratie repose sur la séparation stricte de trois pouvoirs indépendants : le pouvoir législatif, le pouvoir exécutif et le pouvoir judiciaire.",
                    "takeaway": "L'article 16 de la DDHC affirme qu'une société sans séparation des pouvoirs n'a point de Constitution.",
                    "audioSrc": "audio/video_lessons/m2-c1/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Le Pouvoir Législatif : Le Parlement",
                    "badge": "Assemblée & Sénat",
                    "durationSeconds": 22,
                    "visualTheme": "liberte",
                    "heading": "Le Parlement Français",
                    "subheading": "Assemblée nationale et Sénat : voter la loi et contrôler l'exécutif",
                    "icon": "fa-landmark",
                    "keyPoints": [
                        "Assemblée nationale : 577 députés élus au suffrage universel direct pour 5 ans",
                        "Siège : Palais Bourbon à Paris. Députés représentent la Nation entière",
                        "Sénat : 348 sénateurs élus au suffrage indirect pour 6 ans (renouvelé par moitié)",
                        "Siège : Palais du Luxembourg à Paris. Représente les collectivités locales"
                    ],
                    "narrationText": "Le pouvoir législatif appartient au Parlement, composé de deux chambres. L'Assemblée nationale réunit cinq cent soixante-dix-sept députés élus au suffrage universel direct. Le Sénat réunit trois cent quarante-huit sénateurs élus au suffrage indirect. Ensemble, ils débattent et votent les lois.",
                    "takeaway": "En cas de désaccord final entre les deux chambres, l'Assemblée nationale a le dernier mot.",
                    "audioSrc": "audio/video_lessons/m2-c1/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Le Pouvoir Exécutif & Le Pouvoir Judiciaire",
                    "badge": "Exécutif & Justice",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Exécutif et Indépendance de la Justice",
                    "subheading": "Appliquer la loi et protéger les libertés fondamentales",
                    "icon": "fa-gavel",
                    "keyPoints": [
                        "Pouvoir exécutif : Président de la République et Premier ministre avec son gouvernement",
                        "Dirige l'administration, promulgue les lois et conduit les affaires de l'État",
                        "Pouvoir judiciaire : magistrats du siège et du parquet indépendants",
                        "Garantit le respect des lois et tranche les litiges en toute impartialité"
                    ],
                    "narrationText": "Le pouvoir exécutif, incarné par le Président et le Gouvernement, veille à l'application des lois et conduit la politique nationale. Le pouvoir judiciaire, composé de juges indépendants, protège les libertés fondamentales et applique les sanctions prévues par le Code civil et pénal.",
                    "takeaway": "Nul n'est au-dessus des lois dans un État de droit.",
                    "audioSrc": "audio/video_lessons/m2-c1/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "L'État de Droit & Le Conseil Constitutionnel",
                    "badge": "Hiérarchie des Normes",
                    "durationSeconds": 20,
                    "visualTheme": "fraternite",
                    "heading": "L'État de Droit et la Constitution",
                    "subheading": "La Constitution de 1958 au sommet de la hiérarchie des lois",
                    "icon": "fa-shield-halved",
                    "keyPoints": [
                        "État de droit : l'État lui-même est soumis aux règles de droit",
                        "Conseil constitutionnel : 9 membres nommés + anciens Présidents de la République",
                        "Contrôle la conformité des lois à la Constitution avant leur promulgation",
                        "Veille à la régularité des élections présidentielles et législatives"
                    ],
                    "narrationText": "Dans un État de droit, même les dirigeants doivent se conformer strictement à la loi. Le Conseil constitutionnel veille à ce qu'aucune loi votée par le Parlement ne contredise la Constitution de 1958 ou les droits fondamentaux.",
                    "takeaway": "Le siège du Conseil constitutionnel se situe au Palais-Royal à Paris.",
                    "audioSrc": "audio/video_lessons/m2-c1/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Député vs Sénateur",
                    "badge": "Question d'Entretien",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Question Piège de l'Instructeur",
                    "subheading": "« Quelle est la différence entre un député et un sénateur ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Le député est élu par tous les citoyens (suffrage direct) au Palais Bourbon",
                        "Le sénateur est élu par les grands électeurs / maires (suffrage indirect) au Luxembourg",
                        "L'Assemblée peut être dissoute par le Président, mais pas le Sénat",
                        "En cas de désaccord sur une loi, l'Assemblée nationale a le dernier mot"
                    ],
                    "narrationText": "Question classique à l'entretien : quelle est la différence entre un député et un sénateur ? Répondez clairement que les députés sont élus directement par le peuple pour cinq ans au Palais Bourbon, tandis que les sénateurs représentent les territoires.",
                    "takeaway": "Préciser que l'Assemblée nationale a le dernier mot impressionne l'agent.",
                    "audioSrc": "audio/video_lessons/m2-c1/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Vérifiez vos acquis sur la séparation des pouvoirs",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Où siège l'Assemblée nationale à Paris ?",
                        "options": [
                            "Au Palais de l'Élysée",
                            "Au Palais Bourbon",
                            "Au Palais du Luxembourg"
                        ],
                        "correctIndex": 1,
                        "explanation": "L'Assemblée nationale siège au Palais Bourbon dans le 7e arrondissement de Paris, tandis que le Sénat siège au Palais du Luxembourg."
                    },
                    "narrationText": "Vérifions vos acquis : où siège l'Assemblée nationale à Paris ? Cliquez sur la bonne réponse pour valider ce chapitre.",
                    "takeaway": "Parfait ! Vous maîtrisez les fondements de nos institutions.",
                    "audioSrc": "audio/video_lessons/m2-c1/scene_6.mp3"
                }
            ]
        },

        "m2-c2": {
            "chapterId": "m2-c2",
            "moduleId": "module-2",
            "title": "Le Président de la République et le Gouvernement",
            "subtitle": "Rôle du Chef de l'État, du Premier ministre et compétences de l'Élysée et Matignon",
            "totalScenes": 6,
            "estimatedDuration": "2 min 05",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Le Président de la République",
                    "badge": "Chef de l'État",
                    "durationSeconds": 20,
                    "visualTheme": "tricolore",
                    "heading": "La Clé de Voûte des Institutions",
                    "subheading": "Élu pour 5 ans au suffrage universel direct",
                    "icon": "fa-building-columns",
                    "keyPoints": [
                        "Résidence officielle : Palais de l'Élysée à Paris",
                        "Élu pour un mandat de 5 ans (quinquennat depuis 2002)",
                        "Chef suprême des armées et garant de l'indépendance nationale",
                        "Nomme le Premier ministre et préside le Conseil des ministres"
                    ],
                    "narrationText": "Le Président de la République est la clé de voûte de la Cinquième République. Élu pour cinq ans au suffrage universel direct, il réside au Palais de l'Élysée, commande les armées et veille au respect de la Constitution.",
                    "takeaway": "Le mandat présidentiel est fixé à 5 ans, renouvelable une seule fois consécutivement.",
                    "audioSrc": "audio/video_lessons/m2-c2/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Les Pouvoirs Propres du Président",
                    "badge": "Pouvoirs Constitutionnels",
                    "durationSeconds": 22,
                    "visualTheme": "liberte",
                    "heading": "Les Pouvoirs Spécifiques du Chef de l'État",
                    "subheading": "Des compétences majeures sans contreseing ministériel",
                    "icon": "fa-stamp",
                    "keyPoints": [
                        "Droit de dissolution de l'Assemblée nationale (Article 12)",
                        "Pouvoirs exceptionnels en cas de crise majeure (Article 16)",
                        "Droit de grâce présidentielle individuelle",
                        "Négociation et ratification des traités internationaux"
                    ],
                    "narrationText": "Le Président dispose de pouvoirs propres très puissants : il peut dissoudre l'Assemblée nationale, soumettre une loi à référendum, et en cas de crise nationale grave, activer les pouvoirs exceptionnels prévus par l'article 16.",
                    "takeaway": "Le Président de la République ne peut pas dissoudre le Sénat.",
                    "audioSrc": "audio/video_lessons/m2-c2/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Le Premier Ministre & Le Gouvernement",
                    "badge": "Hôtel de Matignon",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Le Premier Ministre et Matignon",
                    "subheading": "Chef du gouvernement et responsable devant le Parlement",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Résidence officielle : Hôtel de Matignon (Paris 7e)",
                        "Dirige l'action du Gouvernement et coordonne les ministères",
                        "Responsable devant l'Assemblée nationale (motion de censure)",
                        "Assure l'exécution concrète des lois et dispose de l'administration"
                    ],
                    "narrationText": "Le Premier ministre réside à l'Hôtel de Matignon. Il dirige l'action du gouvernement, coordonne le travail des ministres et assure l'exécution des lois. Il est politiquement responsable devant l'Assemblée nationale.",
                    "takeaway": "Connaître le nom du Premier ministre en fonction est obligatoire pour l'entretien.",
                    "audioSrc": "audio/video_lessons/m2-c2/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "La Cohabitation Politique",
                    "badge": "Régime Mixte",
                    "durationSeconds": 18,
                    "visualTheme": "fraternite",
                    "heading": "Le Phénomène de Cohabitation",
                    "subheading": "Quand le Président et le Premier ministre sont de bords opposés",
                    "icon": "fa-handshake",
                    "keyPoints": [
                        "Se produit lorsque la majorité à l'Assemblée est opposée au Président",
                        "Exemples historiques : Mitterrand/Chirac (1986), Chirac/Jospin (1997)",
                        "Le Premier ministre conduit alors la politique intérieure du pays",
                        "Le Président conserve la politique étrangère et la défense"
                    ],
                    "narrationText": "La cohabitation survient lorsque le Président et la majorité de l'Assemblée nationale appartiennent à des partis opposés. Dans ce cas, le Premier ministre conduit la politique intérieure, tandis que le Président représente la France à l'étranger.",
                    "takeaway": "La France a connu trois cohabitations sous la Ve République.",
                    "audioSrc": "audio/video_lessons/m2-c2/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Noms et Fonctions",
                    "badge": "Indispensable le Jour J",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Questions Types de l'Instructeur",
                    "subheading": "« Qui nomme le Premier ministre ? Où réside le Chef de l'État ? »",
                    "icon": "fa-circle-question",
                    "keyPoints": [
                        "Sachez nommer immédiatement le Président actuel et le Premier ministre",
                        "Précisez leurs résidences : Élysée pour le Président, Matignon pour le Premier ministre",
                        "Rappelez la durée du mandat : quinquennat (5 ans)",
                        "Préparez le nom de votre Ministre de l'Intérieur (ministère de la naturalisation)"
                    ],
                    "narrationText": "Avant votre entretien, vérifiez impérativement l'actualité politique récente. L'agent vous demandera qui est le Président actuel, qui est le Premier ministre, ainsi que le nom du Ministre de l'Intérieur qui supervise la naturalisation.",
                    "takeaway": "Une hésitation sur les noms des dirigeants actuels est pénalisante.",
                    "audioSrc": "audio/video_lessons/m2-c2/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Testez votre Compréhension",
                    "subheading": "Validez vos repères sur l'exécutif",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Quelle est la durée du mandat du Président de la République en France ?",
                        "options": [
                            "4 ans",
                            "5 ans (quinquennat)",
                            "7 ans (septennat)"
                        ],
                        "correctIndex": 1,
                        "explanation": "Depuis la réforme constitutionnelle de l'an 2000 entrée en vigueur en 2002, le mandat présidentiel est de 5 ans (quinquennat)."
                    },
                    "narrationText": "Testez votre compréhension : quelle est la durée du mandat du Président de la République ? Cliquez sur la bonne réponse pour valider votre leçon.",
                    "takeaway": "Excellent ! Retenez bien le terme de quinquennat.",
                    "audioSrc": "audio/video_lessons/m2-c2/scene_6.mp3"
                }
            ]
        },

        "m2-c3": {
            "chapterId": "m2-c3",
            "moduleId": "module-2",
            "title": "L'Organisation Territoriale de la France",
            "subtitle": "Communes, Départements, Régions et Territoires d'Outre-mer",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Le Découpage Administratif de la France",
                    "badge": "Décentralisation",
                    "durationSeconds": 18,
                    "visualTheme": "tricolore",
                    "heading": "Les 3 Échelons Territoriaux",
                    "subheading": "Commune, Département et Région",
                    "icon": "fa-map-location-dot",
                    "keyPoints": [
                        "Environ 35 000 communes en France métropolitaine et outre-mer",
                        "101 départements (96 métropolitains et 5 d'outre-mer)",
                        "18 régions administratives (13 métropolitaines et 5 d'outre-mer)",
                        "Principe constitutionnel : organisation décentralisée de la République"
                    ],
                    "narrationText": "Bienvenue dans cette leçon consacrée aux territoires français. Pour administrer le pays au plus près des citoyens, la France s'organise en trois niveaux de collectivités territoriales : les communes, les départements et les régions.",
                    "takeaway": "La France compte 101 départements et 18 régions.",
                    "audioSrc": "audio/video_lessons/m2-c3/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "La Commune & Le Maire",
                    "badge": "Échelon de Proximité",
                    "durationSeconds": 20,
                    "visualTheme": "liberte",
                    "heading": "La Mairie et le Rôle du Maire",
                    "subheading": "Le premier contact de la citoyenneté au quotidien",
                    "icon": "fa-house-flag",
                    "keyPoints": [
                        "Élus au suffrage direct tous les 6 ans (Conseil municipal)",
                        "Le maire est à la fois agent de la commune et représentant de l'État",
                        "Officier d'état civil (mariages, naissances, décès) et officier de police",
                        "Gère les écoles primaires, l'urbanisme local et la vie associative"
                    ],
                    "narrationText": "La commune est la cellule de base de notre démocratie. Le maire, élu par les conseillers municipaux pour six ans, célèbre les mariages, gère les écoles primaires et représente l'État dans sa ville ou son village.",
                    "takeaway": "Vous devez impérativement connaître le nom du maire de votre commune.",
                    "audioSrc": "audio/video_lessons/m2-c3/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Le Département & Le Préfet",
                    "badge": "Solidarités & État Local",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Département, Conseil Départemental et Préfet",
                    "subheading": "L'action sociale et l'autorité républicaine",
                    "icon": "fa-shield",
                    "keyPoints": [
                        "Créés en 1790 sous la Révolution française (101 départements)",
                        "Conseil départemental : gère l'action sociale (RSA, enfance, personnes âgées) et les collèges",
                        "Le Préfet : haut fonctionnaire nommé par le Président en Conseil des ministres",
                        "Représente l'État, garantit la sécurité publique et instruit les dossiers de naturalisation"
                    ],
                    "narrationText": "Créé sous la Révolution, le département gère la solidarité sociale et les collèges. Dans chaque département, le Préfet représente le gouvernement, veille à l'ordre public et prend la décision sur votre dossier de naturalisation.",
                    "takeaway": "Le préfet est le représentant direct de l'État dans votre département.",
                    "audioSrc": "audio/video_lessons/m2-c3/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "La Région & La France d'Outre-Mer",
                    "badge": "Développement & Outre-mer",
                    "durationSeconds": 22,
                    "visualTheme": "fraternite",
                    "heading": "Régions et Territoires Ultramarins",
                    "subheading": "Lycées, transports et les 5 DROM d'outre-mer",
                    "icon": "fa-globe",
                    "keyPoints": [
                        "La Région : gère le développement économique, les transports régionaux (TER) et les lycées",
                        "Les 5 DROM d'Outre-mer : Guadeloupe, Martinique, Guyane, La Réunion, Mayotte",
                        "Monnaie : l'Euro (sauf en Polynésie, Nouvelle-Calédonie, Wallis-et-Futuna : franc pacifique)",
                        "Partie intégrante de la République et de l'Union européenne"
                    ],
                    "narrationText": "La région assure le développement économique et la gestion des lycées. La France compte également des territoires d'outre-mer exceptionnels, dont cinq départements et régions : la Guadeloupe, la Martinique, la Guyane, La Réunion et Mayotte.",
                    "takeaway": "Sachez citer les 5 départements d'outre-mer sans hésiter.",
                    "audioSrc": "audio/video_lessons/m2-c3/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Connaître son Territoire",
                    "badge": "Questions Locales",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Les Questions sur Votre Ville et Région",
                    "subheading": "« Dans quel département et région habitez-vous ? Qui est votre maire ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Connaître le numéro et le nom de votre département (ex: 75 Paris, 69 Rhône)",
                        "Nom de votre région administrative (ex: Île-de-France, Auvergne-Rhône-Alpes)",
                        "Nom du maire de votre commune de résidence",
                        "Nom de la préfecture ou sous-préfecture dont vous dépendez"
                    ],
                    "narrationText": "L'agent vérifie systématiquement votre ancrage local : il vous demandera le nom de votre maire, le numéro de votre département et le nom de votre région. Préparez ces quatre informations indispensables.",
                    "takeaway": "Une bonne connaissance de votre commune prouve votre intégration.",
                    "audioSrc": "audio/video_lessons/m2-c3/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Vérifiez vos repères territoriaux",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Combien y a-t-il de départements en France au total (métropole et outre-mer) ?",
                        "options": [
                            "96 départements",
                            "101 départements",
                            "120 départements"
                        ],
                        "correctIndex": 1,
                        "explanation": "La France compte 101 départements : 96 en métropole et 5 d'outre-mer (Guadeloupe, Martinique, Guyane, La Réunion et Mayotte)."
                    },
                    "narrationText": "Testez vos repères territoriaux : combien y a-t-il de départements en France au total ? Cliquez sur la bonne réponse pour valider la leçon.",
                    "takeaway": "Bravo ! Vous maîtrisez la géographie administrative de la France.",
                    "audioSrc": "audio/video_lessons/m2-c3/scene_6.mp3"
                }
            ]
        },

        "m2-c4": {
            "chapterId": "m2-c4",
            "moduleId": "module-2",
            "title": "La France dans l'Union Européenne",
            "subtitle": "Traité de Rome, Parlement de Strasbourg, Euro et citoyenneté européenne",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "La Construction Européenne",
                    "badge": "Pères Fondateurs",
                    "durationSeconds": 20,
                    "visualTheme": "tricolore",
                    "heading": "La France au Cœur de l'Europe",
                    "subheading": "La déclaration Schuman de 1950 et le Traité de Rome de 1957",
                    "icon": "fa-flag-usa",
                    "keyPoints": [
                        "Projet né après la Seconde Guerre mondiale pour garantir une paix durable",
                        "Déclaration de Robert Schuman le 9 mai 1950 (Fête de l'Europe)",
                        "Jean Monnet et Robert Schuman : pères fondateurs français",
                        "1957 : Traité de Rome fondant la Communauté Économique Européenne (CEE)"
                    ],
                    "narrationText": "Après les ravages de la Seconde Guerre mondiale, la France a joué un rôle moteur dans la création de l'Union européenne. Initiée par Robert Schuman et Jean Monnet en 1950, l'aventure européenne vise à préserver une paix durable sur notre continent.",
                    "takeaway": "La Fête de l'Europe est célébrée chaque année le 9 mai.",
                    "audioSrc": "audio/video_lessons/m2-c4/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Les Symboles Européens",
                    "badge": "Emblèmes de l'UE",
                    "durationSeconds": 18,
                    "visualTheme": "liberte",
                    "heading": "Les Symboles de l'Union Européenne",
                    "subheading": "Drapeau, Hymne, Devise et Monnaie",
                    "icon": "fa-star",
                    "keyPoints": [
                        "Drapeau européen : cercle de 12 étoiles dorées sur fond bleu (symbole de perfection et d'union)",
                        "Hymne européen : L'Ode à la joie de Beethoven (Neuvième Symphonie)",
                        "Devise de l'UE : « Unie dans la diversité »",
                        "Monnaie unique : L'Euro (€), mise en circulation en 2002"
                    ],
                    "narrationText": "L'Union européenne possède ses propres symboles : un drapeau bleu à douze étoiles dorées, un hymne sans parole tiré de la Neuvième symphonie de Beethoven, la devise « Unie dans la diversité » et la monnaie unique, l'Euro.",
                    "takeaway": "Les 12 étoiles ne représentent pas le nombre de pays, mais la perfection et l'unité.",
                    "audioSrc": "audio/video_lessons/m2-c4/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Institutions de l'UE & Siège à Strasbourg",
                    "badge": "Strasbourg & Bruxelles",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Le Parlement Européen à Strasbourg",
                    "subheading": "La France accueille l'une des capitales de l'Europe",
                    "icon": "fa-building-columns",
                    "keyPoints": [
                        "Parlement européen : siège officiel situé à Strasbourg en France",
                        "Élu au suffrage universel direct tous les 5 ans par tous les citoyens de l'UE",
                        "Commission européenne et Conseil de l'UE : siègent à Bruxelles",
                        "Cour de justice de l'UE : siège à Luxembourg"
                    ],
                    "narrationText": "La France héberge le Parlement européen, dont le siège officiel se trouve à Strasbourg. Les députés européens y sont élus au suffrage universel direct tous les cinq ans pour voter le budget et les directives européennes avec le Conseil.",
                    "takeaway": "Le siège officiel du Parlement européen est bien à Strasbourg, en France.",
                    "audioSrc": "audio/video_lessons/m2-c4/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "La Citoyenneté Européenne",
                    "badge": "Traité de Maastricht 1992",
                    "durationSeconds": 20,
                    "visualTheme": "fraternite",
                    "heading": "Citoyen Français et Citoyen Européen",
                    "subheading": "Des droits nouveaux attachés à la nationalité française",
                    "icon": "fa-passport",
                    "keyPoints": [
                        "Instaurée par le Traité de Maastricht de 1992",
                        "Toute personne ayant la nationalité française est automatiquement citoyenne de l'UE",
                        "Libre circulation, séjour et travail dans les 27 pays membres",
                        "Droit de vote et d'éligibilité aux élections municipales et européennes"
                    ],
                    "narrationText": "En devenant citoyen français, vous devenez automatiquement citoyen de l'Union européenne. Cela vous accorde le droit de circuler, résider et travailler librement dans les vingt-sept pays membres sans visa ni titre de séjour.",
                    "takeaway": "L'Union européenne compte aujourd'hui 27 États membres.",
                    "audioSrc": "audio/video_lessons/m2-c4/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Questions sur l'Europe",
                    "badge": "Questions Fréquentes",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Questions Types de l'Instructeur",
                    "subheading": "« Combien de pays dans l'UE ? Où siège le Parlement ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Nombre d'États membres : 27 (depuis le départ du Royaume-Uni / Brexit)",
                        "Le siège du Parlement européen : Strasbourg",
                        "Nommez au moins 2 ou 3 pères fondateurs : Robert Schuman, Jean Monnet",
                        "La date de la Fête de l'Europe : le 9 mai"
                    ],
                    "narrationText": "L'agent instructeur vous interrogera sur l'Europe : combien de pays composent l'Union ? Où siège le Parlement européen ? Répondez avec assurance : vingt-sept pays, et le Parlement siège à Strasbourg.",
                    "takeaway": "Le chiffre 27 est indispensable à retenir après le Brexit.",
                    "audioSrc": "audio/video_lessons/m2-c4/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Vérifiez vos repères sur l'Europe",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Dans quelle ville française se situe le siège officiel du Parlement européen ?",
                        "options": [
                            "Paris",
                            "Strasbourg",
                            "Lyon"
                        ],
                        "correctIndex": 1,
                        "explanation": "Le siège officiel du Parlement européen est situé à Strasbourg en France, où se tiennent les sessions plénières."
                    },
                    "narrationText": "Testez vos connaissances sur l'Europe : dans quelle ville française se trouve le siège du Parlement européen ? Cliquez sur la bonne réponse.",
                    "takeaway": "Parfait ! Vous maîtrisez la dimension européenne de la France.",
                    "audioSrc": "audio/video_lessons/m2-c4/scene_6.mp3"
                }
            ]
        }
    }

def update_all_lessons():
    with open("data/video_lessons.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    new_lessons = get_full_lessons()
    for k, v in new_lessons.items():
        data["lessons"][k] = v

    with open("data/video_lessons.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated lessons in data/video_lessons.json. Total count now: {len(data['lessons'])}")

if __name__ == "__main__":
    update_all_lessons()
