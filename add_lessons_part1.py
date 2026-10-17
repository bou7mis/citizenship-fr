#!/usr/bin/env python3
"""
Comprehensive Video Lessons Data Generator for all 18 Chapters of Livret du Citoyen 2026.
Creates rich structured video scripts with 5 to 6 scenes per chapter:
- Scene 1: Introduction & Repères Officiels
- Scene 2: Premier Pilier / Grand Thème Clé
- Scene 3: Deuxième Pilier / Fondements Juridiques & Dates
- Scene 4: Troisième Pilier / Application & Société
- Scene 5: Conseils Préfecture & Pièges de l'Entretien
- Scene 6: Mini-Quiz Vidéo / Checkpoint Interactif
"""

import json

def build_all_video_lessons():
    # Load existing lessons to preserve m1-c1
    try:
        with open("data/video_lessons.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        data = {"version": "2026.1", "lessons": {}}

    lessons = data.get("lessons", {})

    # m1-c2: Les Symboles de la République Française
    lessons["m1-c2"] = {
        "chapterId": "m1-c2",
        "moduleId": "module-1",
        "title": "Les Symboles de la République Française",
        "subtitle": "Drapeau tricolore, Marseillaise, Marianne, 14 Juillet et Coq gaulois",
        "totalScenes": 6,
        "estimatedDuration": "1 min 55",
        "scenes": [
            {
                "id": "scene-1",
                "number": 1,
                "title": "Introduction : Les Emblèmes Nationaux",
                "badge": "Article 2 Constitution",
                "durationSeconds": 18,
                "visualTheme": "tricolore",
                "heading": "Les Grands Symboles de la France",
                "subheading": "L'incarnation vivante de la République",
                "icon": "fa-flag",
                "keyPoints": [
                    "Fixés par la Constitution de 1958 en son article 2",
                    "Rassemblement de tous les citoyens au-delà des origines",
                    "Présents dans tous les édifices publics et cérémonies",
                    "Questions systématiques lors de l'entretien préfectoral"
                ],
                "narrationText": "Bienvenue dans cette capsule vidéo dédiée aux symboles républicains. Fixés par la Constitution, ils incarnent l'histoire de France et l'unité de tous les citoyens. Maîtriser leur origine est indispensable le jour de l'entretien.",
                "takeaway": "L'agent vous demandera de citer au moins 3 ou 4 symboles républicains.",
                "audioSrc": "audio/video_lessons/m1-c2/scene_1.mp3"
            },
            {
                "id": "scene-2",
                "number": 2,
                "title": "Le Drapeau Tricolore & La Marseillaise",
                "badge": "Emblème & Hymne",
                "durationSeconds": 22,
                "visualTheme": "liberte",
                "heading": "Drapeau Tricolore et Hymne National",
                "subheading": "Bleu, Blanc, Rouge et le chant de Rouget de Lisle",
                "icon": "fa-music",
                "keyPoints": [
                    "Drapeau tricolore : Bleu et Rouge (Paris), Blanc (le Roi)",
                    "Né lors de la Révolution française en 1789",
                    "La Marseillaise : écrite en 1792 par Rouget de Lisle à Strasbourg",
                    "Chant de guerre pour l'armée du Rhin devenu hymne national"
                ],
                "narrationText": "Le drapeau tricolore associe le blanc de la monarchie au bleu et rouge de la ville de Paris. L'hymne national, la Marseillaise, a été composé à Strasbourg en 1792 par Rouget de Lisle avant d'être popularisé par les volontaires marseillais.",
                "takeaway": "Retenez bien le nom de Rouget de Lisle et l'année 1792.",
                "audioSrc": "audio/video_lessons/m1-c2/scene_2.mp3"
            },
            {
                "id": "scene-3",
                "number": 3,
                "title": "Marianne & Le 14 Juillet",
                "badge": "Allégorie & Fête",
                "durationSeconds": 20,
                "visualTheme": "egalite",
                "heading": "Marianne et la Fête Nationale",
                "subheading": "Le bonnet phrygien et la commémoration républicaine",
                "icon": "fa-person",
                "keyPoints": [
                    "Marianne : allégorie de la République et de la Liberté",
                    "Coiffée du bonnet phrygien (affranchissement des esclaves)",
                    "14 Juillet : fête nationale instaurée par la loi en 1880",
                    "Commémore la prise de la Bastille (1789) et la Fédération (1790)"
                ],
                "narrationText": "Marianne représente la République et la liberté. Son bonnet phrygien symbolise l'émancipation des citoyens. La fête nationale du 14 juillet commémore à la fois la prise de la Bastille de 1789 et la Fête de la Fédération de 1790.",
                "takeaway": "La fête nationale a été officialisée en 1880.",
                "audioSrc": "audio/video_lessons/m1-c2/scene_3.mp3"
            },
            {
                "id": "scene-4",
                "number": 4,
                "title": "Autres Symboles : Coq, Sceau & Faisceau",
                "badge": "Symboles Complémentaires",
                "durationSeconds": 18,
                "visualTheme": "fraternite",
                "heading": "Le Coq Gaulois et les Sceaux",
                "subheading": "Des repères historiques séculaires",
                "icon": "fa-feather",
                "keyPoints": [
                    "Le Coq gaulois : symbole de vigilance et fierté sportive",
                    "Le grand Sceau de France : apposé sur les textes constitutionnels",
                    "Le Faisceau de licteur : symbole d'autorité et d'union civique",
                    "La langue française : seule langue officielle de la République"
                ],
                "narrationText": "D'autres symboles complètent ce patrimoine : le Coq gaulois, emblème de vigilance et d'enthousiasme populaire, ainsi que la langue française, seule langue officielle de la République selon l'article 2 de notre Constitution.",
                "takeaway": "L'article 2 stipule : « La langue de la République est le français ».",
                "audioSrc": "audio/video_lessons/m1-c2/scene_4.mp3"
            },
            {
                "id": "scene-5",
                "number": 5,
                "title": "Conseils Entretien : Questions Pièges",
                "badge": "Préparation Préfecture",
                "durationSeconds": 18,
                "visualTheme": "interview",
                "heading": "Les Questions Fréquentes de l'Agent",
                "subheading": "« Que commémore le 14 juillet ? »",
                "icon": "fa-user-tie",
                "keyPoints": [
                    "Piège classique : ne citez pas seulement la prise de la Bastille",
                    "Mentionnez aussi la Fête de la Fédération de 1790 (union nationale)",
                    "Sachez chanter ou réciter le premier couplet de la Marseillaise",
                    "Indiquez où se trouve le buste de Marianne (dans votre mairie)"
                ],
                "narrationText": "Lors de l'entretien, l'agent peut vous demander ce que commémore le 14 juillet. Montrez votre niveau en précisant qu'il commémore aussi la Fête de la Fédération de 1790, marquant l'union de la Nation.",
                "takeaway": "Citer la Fête de la Fédération démontre une excellente culture civique.",
                "audioSrc": "audio/video_lessons/m1-c2/scene_5.mp3"
            },
            {
                "id": "scene-6",
                "number": 6,
                "title": "Checkpoint : Mini-Quiz Vidéo",
                "badge": "Auto-Évaluation",
                "durationSeconds": 16,
                "visualTheme": "quiz",
                "heading": "Validez vos Connaissances",
                "subheading": "Testez votre maîtrise des symboles nationaux",
                "icon": "fa-circle-check",
                "quiz": {
                    "question": "Qui a écrit les paroles de La Marseillaise en 1792 ?",
                    "options": [
                        "Victor Hugo à Paris",
                        "Claude Joseph Rouget de Lisle à Strasbourg",
                        "Jean de La Fontaine à Versailles"
                    ],
                    "correctIndex": 1,
                    "explanation": "La Marseillaise a été écrite en avril 1792 par Claude Joseph Rouget de Lisle, officier du génie en garnison à Strasbourg."
                },
                "narrationText": "Vérifions vos connaissances : qui a écrit les paroles de la Marseillaise en 1792 ? Cliquez sur la bonne réponse pour valider cette leçon.",
                "takeaway": "Bravo pour la validation de ce chapitre clé !",
                "audioSrc": "audio/video_lessons/m1-c2/scene_6.mp3"
            }
        ]
    }

    # m1-c3: Les 4 Principes de la République : Indivisible, Laïque, Démocratique, Sociale
    lessons["m1-c3"] = {
        "chapterId": "m1-c3",
        "moduleId": "module-1",
        "title": "Les 4 Principes Fondamentaux de la République",
        "subtitle": "Indivisible, Laïque, Démocratique et Sociale (Article 1er)",
        "totalScenes": 6,
        "estimatedDuration": "2 min",
        "scenes": [
            {
                "id": "scene-1",
                "number": 1,
                "title": "L'Article 1er de la Constitution",
                "badge": "Fondement Constitutionnel",
                "durationSeconds": 18,
                "visualTheme": "tricolore",
                "heading": "Les 4 Piliers Républicains",
                "subheading": "L'ossature de l'État républicain moderne",
                "icon": "fa-landmark",
                "keyPoints": [
                    "« La France est une République indivisible, laïque, démocratique et sociale »",
                    "Article 1er de la Constitution de la Ve République (1958)",
                    "Définit l'équilibre entre unité, liberté et protection de tous",
                    "Question fondamentale et récurrente à l'entretien de naturalisation"
                ],
                "narrationText": "L'article premier de notre Constitution proclame que la France est une République indivisible, laïque, démocratique et sociale. Ces quatre piliers définissent la nature même de la citoyenneté française.",
                "takeaway": "Vous devez savoir réciter sans hésiter ces 4 qualificatifs.",
                "audioSrc": "audio/video_lessons/m1-c3/scene_1.mp3"
            },
            {
                "id": "scene-2",
                "number": 2,
                "title": "Indivisible & Démocratique",
                "badge": "Unité & Souveraineté",
                "durationSeconds": 20,
                "visualTheme": "liberte",
                "heading": "Une République Indivisible et Démocratique",
                "subheading": "Une seule loi et la souveraineté du peuple",
                "icon": "fa-check-to-slot",
                "keyPoints": [
                    "Indivisible : une seule loi pour tous sur l'ensemble du territoire",
                    "Rejet de tout communautarisme et de tout séparatisme",
                    "Démocratique : gouvernement du peuple, par le peuple et pour le peuple",
                    "Suffrage universel direct et égalité absolue de chaque vote"
                ],
                "narrationText": "Indivisible signifie que les mêmes lois s'appliquent sur tout le territoire et qu'aucune distinction ethnique ou religieuse n'est reconnue par l'État. Démocratique signifie que le pouvoir émane des citoyens par le suffrage universel.",
                "takeaway": "La souveraineté nationale appartient au peuple.",
                "audioSrc": "audio/video_lessons/m1-c3/scene_2.mp3"
            },
            {
                "id": "scene-3",
                "number": 3,
                "title": "Le Principe de Laïcité",
                "badge": "Loi du 9 décembre 1905",
                "durationSeconds": 24,
                "visualTheme": "egalite",
                "heading": "La Laïcité : Pierre Angulaire Républicaine",
                "subheading": "Séparation des Églises et de l'État",
                "icon": "fa-scale-balanced",
                "keyPoints": [
                    "Loi fondamentale du 9 décembre 1905",
                    "L'État ne salarie ni ne subventionne aucun culte",
                    "Neutralité absolue des services publics et des fonctionnaires",
                    "Liberté totale de conscience : croire, ne pas croire ou changer de religion",
                    "L'espace public et l'école protégés des pressions prosélytes"
                ],
                "narrationText": "La laïcité, instituée par la loi du 9 décembre 1905, garantit la liberté de culte tout en séparant strictement l'État des religions. Les agents du service public doivent respecter une neutralité absolue, et les lois de la République sont toujours supérieures aux règles religieuses.",
                "takeaway": "La date du 9 décembre 1905 est incontournable.",
                "audioSrc": "audio/video_lessons/m1-c3/scene_3.mp3"
            },
            {
                "id": "scene-4",
                "number": 4,
                "title": "La République Sociale",
                "badge": "Solidarité & Protection",
                "durationSeconds": 18,
                "visualTheme": "fraternite",
                "heading": "Une République Sociale et Protectrice",
                "subheading": "L'assurance que nul n'est laissé pour compte",
                "icon": "fa-hand-holding-heart",
                "keyPoints": [
                    "Création de la Sécurité sociale en 1945",
                    "Accès garanti aux soins, aux retraites et aux aides d'urgence",
                    "Éducation gratuite, laïque et obligatoire de 3 à 16 ans",
                    "Solidarité nationale financée par l'impôt et les cotisations"
                ],
                "narrationText": "Enfin, la République est sociale : elle protège les plus vulnérables grâce à la Sécurité sociale créée en 1945, à l'accès universel aux soins de santé et à l'école gratuite et obligatoire pour tous les enfants.",
                "takeaway": "La Sécurité sociale a été fondée en 1945 sous le général de Gaulle.",
                "audioSrc": "audio/video_lessons/m1-c3/scene_4.mp3"
            },
            {
                "id": "scene-5",
                "number": 5,
                "title": "Conseils Entretien : Question sur la Laïcité",
                "badge": "Question Décisive",
                "durationSeconds": 20,
                "visualTheme": "interview",
                "heading": "La Question la Plus Posée à l'Entretien",
                "subheading": "« Qu'est-ce que la laïcité pour vous ? »",
                "icon": "fa-user-tie",
                "keyPoints": [
                    "Ne dites pas que la laïcité interdit les religions",
                    "Précisez qu'elle garantit la liberté de croire ou de ne pas croire",
                    "Rappelez que dans l'espace civil, la loi de la République prévaut",
                    "Insistez sur la neutralité des agents de l'État et de l'école républicaine"
                ],
                "narrationText": "Attention, l'agent instructeur vous demandera avec certitude ce que représente la laïcité. Expliquez qu'elle ne combat pas les religions, mais protège la liberté de chacun tout en imposant la neutralité à l'État et le respect des lois communes.",
                "takeaway": "La laïcité est une liberté avant d'être une règle de neutralité.",
                "audioSrc": "audio/video_lessons/m1-c3/scene_5.mp3"
            },
            {
                "id": "scene-6",
                "number": 6,
                "title": "Checkpoint : Mini-Quiz Vidéo",
                "badge": "Auto-Évaluation",
                "durationSeconds": 16,
                "visualTheme": "quiz",
                "heading": "Validez vos Connaissances",
                "subheading": "Vérifiez votre compréhension de l'Article 1er",
                "icon": "fa-circle-check",
                "quiz": {
                    "question": "En quelle année a été adoptée la loi historique de séparation des Églises et de l'État instituant la laïcité ?",
                    "options": [
                        "1789",
                        "1905",
                        "1958"
                    ],
                    "correctIndex": 1,
                    "explanation": "La grande loi de séparation des Églises et de l'État a été promulguée le 9 décembre 1905 sous l'impulsion notamment d'Aristide Briand."
                },
                "narrationText": "Testez vos connaissances : en quelle année a été adoptée la loi historique de séparation des Églises et de l'État ? Choisissez la réponse exacte pour valider la leçon.",
                "takeaway": "Excellente réponse ! Chapitre validé.",
                "audioSrc": "audio/video_lessons/m1-c3/scene_6.mp3"
            }
        ]
    }

    # Save to json file
    with open("data/video_lessons.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Added lessons for m1-c2 and m1-c3. Total lessons:", len(data["lessons"]))

if __name__ == "__main__":
    build_all_video_lessons()
