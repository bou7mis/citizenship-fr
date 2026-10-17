#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script to produce structured E-Learning Video Lessons dataset (data/video_lessons.json)
for the French Citizenship Interview Preparation App.
Starting with Chapter 1: La Devise de la République : Liberté, Égalité, Fraternité.
"""

import json
import os

video_lessons = {
    "version": "2026.1",
    "description": "Scénarios complets des capsules vidéos e-learning pour chaque chapitre du Livret du Citoyen 2026.",
    "lessons": {
        "m1-c1": {
            "chapterId": "m1-c1",
            "moduleId": "module-1",
            "title": "La Devise de la République : Liberté, Égalité, Fraternité",
            "subtitle": "Les fondements de la République et les repères communs du vivre-ensemble",
            "totalScenes": 6,
            "estimatedDuration": "1 min 50",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Introduction & Origines de la Devise",
                    "badge": "Symbole Officiel",
                    "durationSeconds": 18,
                    "visualTheme": "tricolore",
                    "heading": "La Devise de la République Française",
                    "subheading": "« Liberté, Égalité, Fraternité »",
                    "icon": "fa-scale-balanced",
                    "keyPoints": [
                        "Inscrite à l'article 2 de la Constitution de 1958",
                        "Gravée au fronton de toutes les mairies et préfectures",
                        "Présente sur les pièces de monnaie et timbres postaux",
                        "Repère commun indispensable du vivre-ensemble"
                    ],
                    "narrationText": "Bienvenue dans ce cours vidéo officiel de préparation à la naturalisation. La devise de la France est « Liberté, Égalité, Fraternité ». Gravée au fronton des mairies et des préfectures, elle consacre les trois valeurs fondatrices et indissociables de notre République.",
                    "takeaway": "La devise est la première question fréquemment posée le jour de l'entretien."
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "1. Le Principe de Liberté",
                    "badge": "Article 4 - DDHC 1789",
                    "durationSeconds": 20,
                    "visualTheme": "blue",
                    "heading": "La Liberté en Droit Français",
                    "subheading": "« Pouvoir faire tout ce qui ne nuit pas à autrui »",
                    "icon": "fa-dove",
                    "keyPoints": [
                        "Liberté de pensée, d'opinion et de conscience (croire ou ne pas croire)",
                        "Liberté d'expression par la parole, l'écrit et la création",
                        "Limites prévues par la loi : l'injure, la diffamation et la haine sont interdites",
                        "Proclamée par la Déclaration des Droits de l'Homme de 1789"
                    ],
                    "narrationText": "Premier pilier : la Liberté. L'article 4 de la Déclaration des Droits de l'Homme de 1789 dispose que la liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui. Elle garantit à chacun la liberté d'opinion, de religion et d'expression, encadrée par la loi pour protéger les droits de tous.",
                    "takeaway": "Mémorisez la citation de l'article 4 de la DDHC de 1789."
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "2. Le Principe d'Égalité",
                    "badge": "Article 1er Constitution",
                    "durationSeconds": 22,
                    "visualTheme": "red",
                    "heading": "L'Égalité Républicaine",
                    "subheading": "Tous les citoyens naissent et demeurent libres et égaux en droits",
                    "icon": "fa-equals",
                    "keyPoints": [
                        "Égalité stricte devant la loi, la justice et le service public",
                        "Égalité femmes-hommes garantie dans la Constitution depuis 1946",
                        "Mêmes droits et devoirs : travail, salaire, famille, santé",
                        "Lutte pénale contre les discriminations, le racisme et le sexisme"
                    ],
                    "narrationText": "Deuxième pilier : l'Égalité. En France, tous les citoyens sont égaux devant la loi, sans distinction d'origine, de religion ou de sexe. L'égalité entre les femmes et les hommes est absolue et garantie par la Constitution depuis 1946. Les discriminations sont sévèrement réprimées par la justice.",
                    "takeaway": "L'égalité femmes-hommes est un point non négociable lors de l'entretien."
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "3. Le Principe de Fraternité",
                    "badge": "Solidarité Nationale",
                    "durationSeconds": 18,
                    "visualTheme": "gold",
                    "heading": "La Fraternité & La Solidarité",
                    "subheading": "L'esprit d'entraide et de cohésion de la communauté nationale",
                    "icon": "fa-hand-holding-heart",
                    "keyPoints": [
                        "Création de la Sécurité sociale en 1945 : soins pour tous",
                        "Redistribution des richesses par l'impôt pour protéger les plus vulnérables",
                        "Solidarité envers les personnes âgées, malades ou sans emploi",
                        "Force de l'engagement associatif et bénévole citoyen"
                    ],
                    "narrationText": "Troisième pilier : la Fraternité. Elle exprime la solidarité qui unit les membres de la communauté nationale. Elle se traduit concrètement par notre système de Sécurité sociale fondé en 1945, la redistribution par l'impôt et la vitalité du tissu associatif.",
                    "takeaway": "Sachez donner un exemple d'entraide citoyenne qui vous tient à cœur."
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Clés pour l'Entretien Préfectoral",
                    "badge": "Préparation Préfecture",
                    "durationSeconds": 20,
                    "visualTheme": "blue-dark",
                    "heading": "Question Type Posée par l'Agent",
                    "subheading": "« Que signifie pour vous la devise française ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Ne récitez pas une définition théorique par cœur sans conviction",
                        "Donnez un exemple tiré de votre vie quotidienne ou professionnelle",
                        "Soulignez votre fierté d'adopter ces valeurs au sein de la Nation",
                        "Montrez votre volonté de transmettre ces principes à vos enfants"
                    ],
                    "narrationText": "Attention, question classique lors de l'entretien : l'agent instructeur vous demandera quelle valeur de la devise vous touche le plus. Ne vous contentez pas d'une réponse scolaire : illustrez votre attachement avec un exemple personnel de votre quotidien en France.",
                    "takeaway": "Une réponse incarnée et sincère fait toute la différence !"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Validation des Connaissances : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 15,
                    "visualTheme": "green",
                    "heading": "Testez votre Compréhension",
                    "subheading": "Validez ce chapitre pour passer au suivant",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Selon la DDHC de 1789, en quoi consiste la liberté ?",
                        "options": [
                            "À faire absolument tout ce dont on a envie sans restriction",
                            "À pouvoir faire tout ce qui ne nuit pas à autrui dans le respect des lois",
                            "À obéir exclusivement aux coutumes de sa communauté d'origine"
                        ],
                        "correctIndex": 1,
                        "explanation": "L'article 4 de la Déclaration des Droits de l'Homme et du Citoyen de 1789 précise : « La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui »."
                    },
                    "narrationText": "Vérifions maintenant vos connaissances avec ce mini-test de fin de vidéo. Selon la Déclaration des Droits de l'Homme de 1789, en quoi consiste la liberté ? Cliquez sur la bonne réponse pour valider votre leçon.",
                    "takeaway": "Bravo pour avoir complété cette première capsule e-learning !"
                }
            ]
        }
    }
}

os.makedirs('data', exist_ok=True)
with open('data/video_lessons.json', 'w', encoding='utf-8') as f:
    json.dump(video_lessons, f, ensure_ascii=False, indent=2)

print('Generated data/video_lessons.json successfully.')
