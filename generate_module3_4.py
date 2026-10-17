#!/usr/bin/env python3
"""
Video Lessons Generator for Module 3 and Module 4 of Livret du Citoyen 2026.
Module 3: Droits et Devoirs (2 chaps)
Module 4: Histoire, Géographie et Culture Françaises (5 chaps)
"""

import json

def get_module3_4_lessons():
    return {
        # =========================================================================
        # MODULE 3: DROITS ET DEVOIRS DES CITOYENS
        # =========================================================================
        "m3-c1": {
            "chapterId": "m3-c1",
            "moduleId": "module-3",
            "title": "Les Droits Fondamentaux et Libertés Individuelles",
            "subtitle": "Libertés publiques, droit de vote, égalité femmes-hommes et justice",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Les Textes Fondateurs des Droits de l'Homme",
                    "badge": "DDHC 1789",
                    "durationSeconds": 18,
                    "visualTheme": "tricolore",
                    "heading": "La France, Terre des Droits de l'Homme",
                    "subheading": "« Les hommes naissent et demeurent libres et égaux en droits »",
                    "icon": "fa-scroll",
                    "keyPoints": [
                        "Déclaration des Droits de l'Homme et du Citoyen du 26 août 1789",
                        "Préambule de la Constitution de 1946 (droits économiques et sociaux)",
                        "Convention Européenne des Droits de l'Homme (CEDH)",
                        "Charte de l'environnement de 2004 adossée à la Constitution"
                    ],
                    "narrationText": "Bienvenue dans cette leçon consacrée à vos droits fondamentaux. Proclamée en 1789, la Déclaration des Droits de l'Homme et du Citoyen affirme que tous les hommes naissent et demeurent libres et égaux en droits, fondement universel de notre démocratie.",
                    "takeaway": "L'article 1er de la DDHC de 1789 est le plus célèbre de l'histoire française.",
                    "audioSrc": "audio/video_lessons/m3-c1/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Les Libertés Individuelles et Publiques",
                    "badge": "Libertés Républicaines",
                    "durationSeconds": 20,
                    "visualTheme": "liberte",
                    "heading": "L'Étendue des Libertés Publiques",
                    "subheading": "Opinion, presse, réunion, association et culte",
                    "icon": "fa-dove",
                    "keyPoints": [
                        "Liberté d'opinion et de culte : croire ou ne pas croire en toute sérénité",
                        "Liberté de la presse et d'expression (grande loi du 29 juillet 1881)",
                        "Liberté d'association (loi du 1er juillet 1901)",
                        "Droit de grève et liberté syndicale garantis par la Constitution"
                    ],
                    "narrationText": "En France, vous bénéficiez de libertés fondamentales protégées par les tribunaux : liberté d'expression, liberté de la presse, liberté de culte, et liberté d'association issue de la célèbre loi de 1901.",
                    "takeaway": "La loi de 1901 régit encore aujourd'hui la création de toutes les associations.",
                    "audioSrc": "audio/video_lessons/m3-c1/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "L'Égalité Femmes-Hommes",
                    "badge": "Grande Cause Nationale",
                    "durationSeconds": 22,
                    "visualTheme": "egalite",
                    "heading": "Une Égalité Stricte et Inconditionnelle",
                    "subheading": "Droits politiques, professionnels et intégrité personnelle",
                    "icon": "fa-venus-mars",
                    "keyPoints": [
                        "Droit de vote des femmes obtenu en 1944 (ordonnance du général de Gaulle)",
                        "Premier vote des femmes aux élections municipales d'avril 1945",
                        "Égalité salariale et parité en politique inscrites dans la loi",
                        "Tolérance zéro pour les violences conjugales et discriminations"
                    ],
                    "narrationText": "L'égalité absolue entre les femmes et les hommes est un principe intangible. Les femmes françaises ont obtenu le droit de vote en 1944. Elles disposent exactement des mêmes droits politiques, économiques et civils que les hommes.",
                    "takeaway": "Retenez bien l'année 1944 pour le droit de vote des femmes.",
                    "audioSrc": "audio/video_lessons/m3-c1/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "Le Droit de Vote et d'Éligibilité",
                    "badge": "Suffrage Universel",
                    "durationSeconds": 18,
                    "visualTheme": "fraternite",
                    "heading": "Le Vote : Cœur de la Souveraineté",
                    "subheading": "Une voix égale pour chaque citoyen majeur",
                    "icon": "fa-check-to-slot",
                    "keyPoints": [
                        "Suffrage universel masculin instauré en 1848, universel complet en 1944",
                        "Scrutin secret sous isoloir pour garantir l'indépendance de chaque électeur",
                        "Éligibilité : tout citoyen peut se présenter aux élections s'il remplit les critères",
                        "Le vote est un droit civique précieux et un devoir moral"
                    ],
                    "narrationText": "En acquérant la nationalité française, vous obtenez le droit de vote et d'éligibilité pour tous les scrutins nationaux et locaux. Voter sous l'isoloir garantit le secret et la liberté absolue de votre choix.",
                    "takeaway": "Le vote est un droit civique fondamental acquis avec la naturalisation.",
                    "audioSrc": "audio/video_lessons/m3-c1/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Égalité et Valeurs",
                    "badge": "Question Décisive",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Questions Types de l'Instructeur",
                    "subheading": "« Que pensez-vous de l'égalité femmes-hommes ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Affirmez sans la moindre ambiguïté votre attachement à cette égalité",
                        "Précisez qu'aucune coutume ou tradition ne peut justifier une inégalité",
                        "Mentionnez des exemples concrets dans l'éducation et la vie de famille",
                        "Rappelez que la loi française protège la liberté de chaque femme"
                    ],
                    "narrationText": "L'agent portera une attention particulière à vos réponses sur l'égalité femmes-hommes et la liberté de conscience. Montrez que ces principes républicains guident votre quotidien et votre vie familiale en France.",
                    "takeaway": "L'égalité femmes-hommes est non négociable pour obtenir la nationalité.",
                    "audioSrc": "audio/video_lessons/m3-c1/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Vérifiez vos repères sur les droits fondamentaux",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "En quelle année les femmes ont-elles obtenu le droit de vote en France ?",
                        "options": [
                            "1789",
                            "1944",
                            "1968"
                        ],
                        "correctIndex": 1,
                        "explanation": "Le droit de vote a été accordé aux femmes en France par ordonnance du 21 avril 1944 signée par le général de Gaulle à Alger."
                    },
                    "narrationText": "Testez vos connaissances : en quelle année les femmes ont-elles obtenu le droit de vote en France ? Choisissez la bonne réponse pour valider la leçon.",
                    "takeaway": "Bravo ! L'année 1944 est un repère historique capital.",
                    "audioSrc": "audio/video_lessons/m3-c1/scene_6.mp3"
                }
            ]
        },

        "m3-c2": {
            "chapterId": "m3-c2",
            "moduleId": "module-3",
            "title": "Les Devoirs et Obligations Civiques",
            "subtitle": "Respect des lois, impôt républicain, défense et fraternité active",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Les Droits Ont pour Corollaire les Devoirs",
                    "badge": "Le Pacte Républicain",
                    "durationSeconds": 18,
                    "visualTheme": "tricolore",
                    "heading": "Être Citoyen : Droits et Devoirs",
                    "subheading": "La citoyenneté n'est pas seulement un statut, c'est un engagement",
                    "icon": "fa-handshake-angle",
                    "keyPoints": [
                        "Pas de droits républicains durables sans respect des devoirs communs",
                        "Respect inconditionnel des lois de la République",
                        "Contribution aux charges publiques par l'impôt",
                        "Participation à la défense et à la justice (juré d'assises)"
                    ],
                    "narrationText": "La citoyenneté française forme un équilibre indissociable : chaque droit accordé par la République a pour contrepartie des devoirs civiques essentiels que chaque citoyen s'engage à respecter loyalement.",
                    "takeaway": "Nul n'est censé ignorer la loi (adage fondamental du droit français).",
                    "audioSrc": "audio/video_lessons/m3-c2/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Le Respect de la Loi et de l'Ordre Public",
                    "badge": "Légalité Républicaine",
                    "durationSeconds": 20,
                    "visualTheme": "liberte",
                    "heading": "La Primauté de la Loi Républicaine",
                    "subheading": "L'expression de la volonté générale au-dessus des règles particulières",
                    "icon": "fa-gavel",
                    "keyPoints": [
                        "La loi est votée par les représentants élus de la Nation",
                        "Elle s'applique uniformément à tous, sans privilège ni exemption",
                        "Interdiction stricte de faire justice soi-même",
                        "Respect des symboles de la République et des agents de l'autorité"
                    ],
                    "narrationText": "Le premier devoir civique est d'obéir aux lois votées par le Parlement. La loi républicaine est la même pour tous : elle protège les faibles et s'impose à toutes les convictions personnelles ou religieuses.",
                    "takeaway": "Les règles civiles et pénales prévalent toujours sur les coutumes ou règles religieuses.",
                    "audioSrc": "audio/video_lessons/m3-c2/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "L'Impôt : Devoir Républicain et Solidarité",
                    "badge": "Article 13 DDHC",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "La Contribution Commune aux Charges Publiques",
                    "subheading": "Financer les hôpitaux, écoles, routes et la sécurité",
                    "icon": "fa-receipt",
                    "keyPoints": [
                        "Article 13 de la DDHC de 1789 : contribution également répartie selon les facultés",
                        "Financement des services publics gratuits : écoles, hôpitaux, police, justice",
                        "Impôt sur le revenu progressif et Taxe sur la Valeur Ajoutée (TVA)",
                        "Obligation de déclaration et de transparence fiscale"
                    ],
                    "narrationText": "Payer ses impôts est un devoir fondamental fondé sur l'article 13 de la Déclaration de 1789. Chacun contribue selon ses capacités financières pour faire vivre nos services publics, nos écoles et notre système de santé.",
                    "takeaway": "L'exemplarité fiscale est un critère scrupuleusement vérifié pour la naturalisation.",
                    "audioSrc": "audio/video_lessons/m3-c2/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "La Défense Nationale & Être Juré d'Assises",
                    "badge": "Engagement Civique",
                    "durationSeconds": 20,
                    "visualTheme": "fraternite",
                    "heading": "Participer à la Défense et à la Justice",
                    "subheading": "Journée Défense et Citoyenneté (JDC) et cour d'assises",
                    "icon": "fa-shield",
                    "keyPoints": [
                        "Recensement citoyen obligatoire à 16 ans pour tous les jeunes français",
                        "Journée Défense et Citoyenneté (JDC) pour sensibiliser aux enjeux de défense",
                        "Possibilité d'intégrer la réserve opérationnelle militaire ou citoyenne",
                        "Devoir de siéger comme juré d'assises tiré au sort sur les listes électorales"
                    ],
                    "narrationText": "Le citoyen participe à la défense de la Nation par le recensement obligatoire et la Journée Défense et Citoyenneté. En outre, tout citoyen peut être tiré au sort pour siéger comme juré populaire dans une cour d'assises et rendre la justice au nom du peuple.",
                    "takeaway": "Le rôle de juré d'assises est un devoir civique obligatoire.",
                    "audioSrc": "audio/video_lessons/m3-c2/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Légalité et Devoirs",
                    "badge": "Préparation Préfecture",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Question Type de l'Instructeur",
                    "subheading": "« Pourquoi paye-t-on des impôts en France ? »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Expliquez que l'impôt finance la solidarité nationale et les infrastructures",
                        "Donnez des exemples : éducation gratuite, hôpitaux publics, secours d'urgence",
                        "Soulignez que vous êtes à jour de vos obligations fiscales et déclaratives",
                        "Affirmez votre fierté de contribuer à la prospérité commune"
                    ],
                    "narrationText": "Si l'agent vous demande pourquoi les citoyens payent des impôts, répondez avec clarté : l'impôt permet de financer les services publics, de protéger les plus démunis et d'assurer le fonctionnement de la justice et de la sécurité.",
                    "takeaway": "Lier l'impôt à la solidarité nationale démontre une excellente maturité citoyenne.",
                    "audioSrc": "audio/video_lessons/m3-c2/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Vérifiez vos acquis sur les devoirs civiques",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Quel article de la DDHC de 1789 établit la nécessité de la contribution publique (l'impôt) selon les capacités de chacun ?",
                        "options": [
                            "Article 1er",
                            "Article 4",
                            "Article 13"
                        ],
                        "correctIndex": 2,
                        "explanation": "L'article 13 de la DDHC de 1789 dispose qu'une contribution commune est indispensable et doit être également répartie entre tous les citoyens, en raison de leurs facultés."
                    },
                    "narrationText": "Testez vos connaissances : quel article de la Déclaration de 1789 établit l'obligation fiscale commune ? Choisissez la bonne réponse.",
                    "takeaway": "Bravo ! Vous comprenez le lien indissociable entre droits et devoirs.",
                    "audioSrc": "audio/video_lessons/m3-c2/scene_6.mp3"
                }
            ]
        },

        # =========================================================================
        # MODULE 4: HISTOIRE, GÉOGRAPHIE ET CULTURE FRANÇAISES
        # =========================================================================
        "m4-c1": {
            "chapterId": "m4-c1",
            "moduleId": "module-4",
            "title": "Les Grandes Périodes et Rois de France",
            "subtitle": "De la Gaule à la Révolution de 1789, Clovis, Charlemagne, Henri IV et Louis XIV",
            "totalScenes": 6,
            "estimatedDuration": "2 min 10",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Les Origines : Gaulois et Gallo-Romains",
                    "badge": "Antiquité & Moyen Âge",
                    "durationSeconds": 20,
                    "visualTheme": "tricolore",
                    "heading": "Des Gaulois à Clovis",
                    "subheading": "Vercingétorix, Alésia (-52) et le baptême de Clovis (496)",
                    "icon": "fa-monument",
                    "keyPoints": [
                        "52 avant J.-C. : défaite de Vercingétorix à Alésia face à Jules César",
                        "Période gallo-romaine : développement des villes, des aqueducs et des voies romaines",
                        "496 : baptême de Clovis, premier roi chrétien des Francs à Reims",
                        "Naissance du royaume des Francs qui donnera le nom de France"
                    ],
                    "narrationText": "L'histoire de France prend racine dans la rencontre entre les Gaulois et la civilisation romaine après la bataille d'Alésia en cinquante-deux avant Jésus-Christ. En quatre cent quatre-vingt-seize, Clovis, roi des Francs, se fait baptiser à Reims, scellant les débuts du royaume.",
                    "takeaway": "Retenez l'année 496 pour le baptême de Clovis à Reims.",
                    "audioSrc": "audio/video_lessons/m4-c1/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Charlemagne & La Renaissance",
                    "badge": "Moyen Âge & Renaissance",
                    "durationSeconds": 22,
                    "visualTheme": "liberte",
                    "heading": "Charlemagne et François Ier",
                    "subheading": "Couronnement de l'an 800 et ordonnance de Villers-Cotterêts (1539)",
                    "icon": "fa-crown",
                    "keyPoints": [
                        "An 800 : Charlemagne couronné Empereur d'Occident à Rome, développement des écoles",
                        "Guerre de Cent Ans : épopée de Jeanne d'Arc qui délivre Orléans en 1429",
                        "François Ier : roi de la Renaissance, protecteur des arts et de Léonard de Vinci",
                        "1539 : Ordonnance de Villers-Cotterêts imposant le français dans tous les actes officiels"
                    ],
                    "narrationText": "En l'an huit cents, Charlemagne est couronné empereur et unifie l'Occident. Plus tard, sous la Renaissance, le roi François Premier adopte en quinze cent trente-neuf l'ordonnance de Villers-Cotterêts, faisant du français la langue juridique et administrative officielle du pays.",
                    "takeaway": "L'ordonnance de Villers-Cotterêts de 1539 a fondé l'usage officiel du français.",
                    "audioSrc": "audio/video_lessons/m4-c1/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Henri IV & L'Édit de Nantes",
                    "badge": "Tolérance Religieuse",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Henri IV et la Pacification",
                    "subheading": "L'Édit de Nantes de 1598 met fin aux guerres de religion",
                    "icon": "fa-feather-pointed",
                    "keyPoints": [
                        "Guerres de religion tragiques entre catholiques et protestants (Saint-Barthélemy 1572)",
                        "1598 : Henri IV promulgue l'Édit de Nantes accordant la liberté de culte aux protestants",
                        "Souverain populaire surnommé « le Bon Roi Henri », assassiné par Ravaillac en 1610",
                        "Premier grand pas historique vers la tolérance et la paix civile"
                    ],
                    "narrationText": "Après de sanglantes guerres de religion, le roi Henri Quatre rétablit la paix civile en signant l'Édit de Nantes en quinze cent quatre-vingt-dix-huit, accordant aux protestants la liberté de conscience et de culte.",
                    "takeaway": "1598 : signature de l'Édit de Nantes par Henri IV.",
                    "audioSrc": "audio/video_lessons/m4-c1/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "Louis XIV & Le Siècle des Lumières",
                    "badge": "Monarchie & Lumières",
                    "durationSeconds": 22,
                    "visualTheme": "fraternite",
                    "heading": "Le Roi-Soleil et les Philosophes",
                    "subheading": "De Versailles (1682) aux idées des Lumières (Voltaire, Rousseau)",
                    "icon": "fa-sun",
                    "keyPoints": [
                        "Louis XIV (1643-1715) : apogée de la monarchie absolue, construction du château de Versailles",
                        "Le XVIIIe siècle : Siècle des Lumières incarné par Voltaire, Rousseau, Montesquieu et Diderot",
                        "Critique de l'absolutisme, promotion de la raison, de la liberté et de l'égalité",
                        "Inspiration intellectuelle directe de la Révolution française de 1789"
                    ],
                    "narrationText": "Au dix-septième siècle, Louis Quatorze, le Roi-Soleil, installe la cour à Versailles. Au siècle suivant, les philosophes des Lumières comme Voltaire, Rousseau et Diderot diffusent les idéaux de raison, de tolérance et d'égalité qui conduiront à la Révolution.",
                    "takeaway": "Sachez citer au moins trois philosophes des Lumières (Voltaire, Rousseau, Montesquieu).",
                    "audioSrc": "audio/video_lessons/m4-c1/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Rois & Personnages",
                    "badge": "Questions d'Histoire",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Questions Fréquentes de l'Instructeur",
                    "subheading": "« Citez un roi de France et son action majeure »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Clovis : premier roi des Francs baptisé en 496",
                        "Charlemagne : empereur d'Occident en 800, réformateur des écoles",
                        "Henri IV : signataire de l'Édit de Nantes en 1598 (paix religieuse)",
                        "Louis XIV : le Roi-Soleil, constructeur de Versailles et souverain absolu"
                    ],
                    "narrationText": "L'agent vous demandera de citer deux ou trois rois de France et ce qu'ils ont accompli. Privilégiez Henri Quatre et l'Édit de Nantes, ou François Premier et la langue française à Villers-Cotterêts.",
                    "takeaway": "Associez toujours le roi à son événement marquant pour une réponse parfaite.",
                    "audioSrc": "audio/video_lessons/m4-c1/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos repères sur l'histoire royale",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Quel roi de France a signé l'Édit de Nantes en 1598 pour pacifier les guerres de religion ?",
                        "options": [
                            "Clovis",
                            "Henri IV",
                            "Louis XIV"
                        ],
                        "correctIndex": 1,
                        "explanation": "C'est Henri IV qui a signé l'Édit de Nantes en avril 1598, accordant la liberté de culte aux protestants et pacifiant le royaume."
                    },
                    "narrationText": "Testez votre culture historique : quel roi de France a signé l'Édit de Nantes en quinze cent quatre-vingt-dix-huit ? Cliquez sur la bonne réponse.",
                    "takeaway": "Bravo ! Vos connaissances historiques sont solides.",
                    "audioSrc": "audio/video_lessons/m4-c1/scene_6.mp3"
                }
            ]
        },

        "m4-c2": {
            "chapterId": "m4-c2",
            "moduleId": "module-4",
            "title": "Du XIXe Siècle aux Deux Guerres Mondiales",
            "subtitle": "Révolution de 1789, Napoléon, République, 1914-1918 et la Résistance (1939-1945)",
            "totalScenes": 6,
            "estimatedDuration": "2 min 10",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "La Révolution Française (1789)",
                    "badge": "Rupture Historique",
                    "durationSeconds": 20,
                    "visualTheme": "tricolore",
                    "heading": "1789 : La Naissance de la Nation Moderne",
                    "subheading": "Prise de la Bastille, abolition des privilèges et DDHC",
                    "icon": "fa-fire",
                    "keyPoints": [
                        "14 juillet 1789 : Prise de la forteresse de la Bastille par le peuple parisien",
                        "Nuit du 4 août 1789 : Abolition des privilèges de la noblesse et du clergé",
                        "26 août 1789 : Déclaration des Droits de l'Homme et du Citoyen",
                        "1792 : Proclamation de la Première République (chute de la royauté)"
                    ],
                    "narrationText": "L'année dix-sept cent quatre-vingt-neuf marque la rupture fondatrice de notre histoire contemporaine. Le quatorze juillet, la prise de la Bastille renverse l'arbitraire royal, avant l'abolition des privilèges et la Déclaration des Droits de l'Homme.",
                    "takeaway": "L'année 1789 est le repère le plus important de l'histoire de France.",
                    "audioSrc": "audio/video_lessons/m4-c2/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Napoléon Bonaparte & Le Code Civil",
                    "badge": "Consulat & Empire",
                    "durationSeconds": 20,
                    "visualTheme": "liberte",
                    "heading": "Napoléon et la Modernisation de l'État",
                    "subheading": "Le Code civil de 1804 et les préfets",
                    "icon": "fa-landmark-dome",
                    "keyPoints": [
                        "Coup d'État du 18 Brumaire (1799) et sacre comme Empereur en 1804",
                        "Création du Code civil des Français (1804), base juridique du droit civil actuel",
                        "Création des préfets, des lycées, du baccalauréat et de la Banque de France",
                        "Chute définitive à Waterloo en 1815 et exil à Sainte-Hélène"
                    ],
                    "narrationText": "Arrivé au pouvoir en dix-sept cent quatre-vingt-dix-neuf, Napoléon Premier réorganise profondément l'État. Il promulgue le Code civil en dix-huit cent quatre, institue les préfets et fonde les lycées et la Banque de France.",
                    "takeaway": "Le Code civil des Français date de 1804.",
                    "audioSrc": "audio/video_lessons/m4-c2/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "La Première Guerre Mondiale (1914-1918)",
                    "badge": "Grande Guerre",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "La Grande Guerre et le Devoir de Mémoire",
                    "subheading": "Bataille de Verdun (1916) et armistice du 11 Novembre 1918",
                    "icon": "fa-helmet-safety",
                    "keyPoints": [
                        "Conflit mondial dévastateur : 1,4 million de soldats français morts",
                        "1916 : Bataille héroïque de Verdun opposant Français et Allemands",
                        "Georges Clemenceau surnommé « le Tigre » ou « le Père la Victoire »",
                        "11 novembre 1918 : Signature de l'Armistice à Rethondes (commémoration nationale)"
                    ],
                    "narrationText": "De dix-neuf cent quatorze à dix-neuf cent dix-huit, la France traverse l'épreuve tragique de la Première Guerre mondiale. Après l'enfer des tranchées de Verdun, l'armistice est signé le onze novembre dix-neuf cent dix-huit, jour férié de commémoration de tous les morts pour la France.",
                    "takeaway": "Le 11 novembre commémore l'Armistice de 1918.",
                    "audioSrc": "audio/video_lessons/m4-c2/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "La Seconde Guerre Mondiale (1939-1945)",
                    "badge": "Appel du 18 Juin & Libération",
                    "durationSeconds": 22,
                    "visualTheme": "fraternite",
                    "heading": "De Gaulle, la Résistance et la Victoire",
                    "subheading": "L'Appel du 18 juin 1940 et la capitulation du 8 Mai 1945",
                    "icon": "fa-medal",
                    "keyPoints": [
                        "18 juin 1940 : Appel à la Résistance lancé de Londres par le général de Gaulle sur la BBC",
                        "Jean Moulin : héros qui unifie la Résistance intérieure au sein du CNR",
                        "Régime collaborationniste de Vichy dirigé par le maréchal Pétain",
                        "6 juin 1944 : Débarquement allié en Normandie et 8 mai 1945 : Victoire alliée en Europe"
                    ],
                    "narrationText": "Envahie en dix-neuf cent quarante, la France refuse la capitulation grâce à l'Appel du dix-huit juin lancé depuis Londres par le général de Gaulle. Avec Jean Moulin et les héros de la Résistance, la France participe à la Libération jusqu'à la victoire du huit mai dix-neuf cent quarante-cinq.",
                    "takeaway": "Le 8 mai célèbre la fin de la Seconde Guerre mondiale en Europe.",
                    "audioSrc": "audio/video_lessons/m4-c2/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Dates Commémoratives",
                    "badge": "Questions Incontournables",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Les 3 Dates Clés Posées à l'Entretien",
                    "subheading": "« Que célèbrent le 14 juillet, le 8 mai et le 11 novembre ? »",
                    "icon": "fa-calendar-days",
                    "keyPoints": [
                        "14 Juillet : Fête nationale (prise de la Bastille et Fête de la Fédération)",
                        "8 Mai : Victoire de 1945 mettant fin à la Seconde Guerre mondiale",
                        "11 Novembre : Armistice de 1918 mettant fin à la Première Guerre mondiale",
                        "Connaître le nom de Jean Moulin (président du Conseil National de la Résistance)"
                    ],
                    "narrationText": "Ne confondez jamais le huit mai et le onze novembre lors de votre entretien. Le onze novembre commémore l'armistice de dix-neuf cent dix-huit, tandis que le huit mai célèbre la capitulation nazie et la victoire de dix-neuf cent quarante-cinq.",
                    "takeaway": "Distinguer clairement le 11 novembre et le 8 mai est capital.",
                    "audioSrc": "audio/video_lessons/m4-c2/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos repères sur les deux guerres",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Que commémore le jour férié national du 8 mai en France ?",
                        "options": [
                            "L'armistice de la Première Guerre mondiale (1918)",
                            "La fin de la Seconde Guerre mondiale en Europe (1945)",
                            "La prise de la Bastille (1789)"
                        ],
                        "correctIndex": 1,
                        "explanation": "Le 8 mai commémore la capitulation sans condition de l'Allemagne nazie en 1945 et la victoire des Alliés marquant la fin de la Seconde Guerre mondiale en Europe."
                    },
                    "narrationText": "Testez votre culture civique : que commémore le jour férié du 8 mai en France ? Cliquez sur la bonne réponse.",
                    "takeaway": "Parfait ! Vous maîtrisez les commémorations républicaines.",
                    "audioSrc": "audio/video_lessons/m4-c2/scene_6.mp3"
                }
            ]
        },

        "m4-c3": {
            "chapterId": "m4-c3",
            "moduleId": "module-4",
            "title": "La Ve République et ses Présidents",
            "subtitle": "De Charles de Gaulle à Emmanuel Macron : 1958 à nos jours",
            "totalScenes": 6,
            "estimatedDuration": "2 min 10",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "La Naissance de la Ve République (1958)",
                    "badge": "Constitution Actuelle",
                    "durationSeconds": 20,
                    "visualTheme": "tricolore",
                    "heading": "1958 : Le Retour du Général de Gaulle",
                    "subheading": "Adoption de la Constitution du 4 octobre 1958",
                    "icon": "fa-landmark",
                    "keyPoints": [
                        "Crise de la guerre d'Algérie provoquant l'instabilité de la IVe République",
                        "Charles de Gaulle rédige une nouvelle Constitution avec Michel Debré",
                        "Approuvée par référendum à plus de 82 % le 28 septembre 1958",
                        "Régime stable renforçant les pouvoirs de l'exécutif face au Parlement"
                    ],
                    "narrationText": "En mille neuf cent cinquante-huit, pour surmonter l'instabilité de la Quatrième République et la crise d'Algérie, le général de Gaulle donne à la France la Constitution de la Cinquième République, adoptée par référendum le quatre octobre mille neuf cent cinquante-huit.",
                    "takeaway": "Notre Constitution actuelle est celle du 4 octobre 1958.",
                    "audioSrc": "audio/video_lessons/m4-c3/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "De Gaulle et Pompidou",
                    "badge": "Les Pionniers",
                    "durationSeconds": 20,
                    "visualTheme": "liberte",
                    "heading": "Charles de Gaulle et Georges Pompidou",
                    "subheading": "Souveraineté, élection au suffrage universel et modernisation",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Charles de Gaulle (1958-1969) : réforme de 1962 instaurant l'élection du Président au suffrage direct",
                        "Développement de la dissuasion nucléaire et décolonisation",
                        "Georges Pompidou (1969-1974) : grande modernisation industrielle (Concorde, TGV, Airbus)",
                        "Création du Centre d'art moderne Georges Pompidou à Beaubourg (Paris)"
                    ],
                    "narrationText": "Charles de Gaulle dote la France d'une stature internationale forte et instaure en mille neuf cent soixante-deux l'élection du Président au suffrage universel direct. Georges Pompidou lui succède et accélère la modernisation industrielle du pays.",
                    "takeaway": "L'élection directe du Président par les citoyens date du référendum de 1962.",
                    "audioSrc": "audio/video_lessons/m4-c3/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Giscard d'Estaing & Mitterrand",
                    "badge": "Grandes Réformes de Société",
                    "durationSeconds": 22,
                    "visualTheme": "egalite",
                    "heading": "Majorité à 18 ans et Abolition de la Peine de Mort",
                    "subheading": "Les grandes avancées démocratiques et sociales",
                    "icon": "fa-scale-balanced",
                    "keyPoints": [
                        "Valéry Giscard d'Estaing (1974-1981) : abaissement de la majorité à 18 ans (1974) et loi Veil (1975)",
                        "François Mitterrand (1981-1995) : premier Président socialiste de la Ve République (2 septennats)",
                        "Abolition historique de la peine de mort en 1981 défendue par Robert Badinter",
                        "Semaine de 39 heures, 5e semaine de congés payés et retraite à 60 ans"
                    ],
                    "narrationText": "Sous Valéry Giscard d'Estaing, la majorité passe à dix-huit ans et Simone Veil légalise l'IVG. Élu en dix-neuf cent quatre-vingt-un, François Mitterrand abolit la peine de mort grâce au combat historique de Robert Badinter.",
                    "takeaway": "L'abolition de la peine de mort en France date de 1981.",
                    "audioSrc": "audio/video_lessons/m4-c3/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "Chirac, Sarkozy, Hollande & Macron",
                    "badge": "Histoire Contemporaine",
                    "durationSeconds": 22,
                    "visualTheme": "fraternite",
                    "heading": "De Jacques Chirac à Emmanuel Macron",
                    "subheading": "Le passage au quinquennat et les défis du XXIe siècle",
                    "icon": "fa-clock-rotate-left",
                    "keyPoints": [
                        "Jacques Chirac (1995-2007) : fin du service militaire obligatoire, passage au quinquennat (5 ans)",
                        "Nicolas Sarkozy (2007-2012) : révision constitutionnelle de 2008 renforçant le Parlement",
                        "François Hollande (2012-2017) : loi sur le mariage pour tous (2013) et accords de Paris sur le climat",
                        "Emmanuel Macron (élu en 2017, réélu en 2022) : plus jeune Président de la République"
                    ],
                    "narrationText": "Jacques Chirac instaure le mandat présidentiel de cinq ans. Nicolas Sarkozy puis François Hollande lui succèdent, marquant notamment l'adoption du mariage pour tous en deux mille treize. Emmanuel Macron est élu en deux mille dix-sept puis réélu en deux mille vingt-deux.",
                    "takeaway": "Sachez citer dans l'ordre chronologique les Présidents de la Ve République.",
                    "audioSrc": "audio/video_lessons/m4-c3/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : L'Ordre des Présidents",
                    "badge": "Classique Préfecture",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "La Question Classique de l'Instructeur",
                    "subheading": "« Citez trois Présidents de la Ve République »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Réciter de mémoire : De Gaulle, Pompidou, Giscard d'Estaing, Mitterrand, Chirac, Sarkozy, Hollande, Macron",
                        "Indiquer qui a fondé la Ve République : le général de Gaulle en 1958",
                        "Mentionner qui a aboli la peine de mort : François Mitterrand en 1981",
                        "Préciser qui est le Président actuel en exercice"
                    ],
                    "narrationText": "L'agent vous demandera de citer plusieurs Présidents de la Cinquième République ou de dire qui a aboli la peine de mort. Entraînez-vous à citer la chronologie exacte pour démontrer votre solide culture politique.",
                    "takeaway": "Une récitation fluide des Présidents inspire une confiance immédiate.",
                    "audioSrc": "audio/video_lessons/m4-c3/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos repères sur la Ve République",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Sous la présidence de quel Chef de l'État la peine de mort a-t-elle été abolie en France en 1981 ?",
                        "options": [
                            "Charles de Gaulle",
                            "François Mitterrand",
                            "Jacques Chirac"
                        ],
                        "correctIndex": 1,
                        "explanation": "La peine de mort a été abolie sous la présidence de François Mitterrand par la loi du 9 octobre 1981 portée avec courage par son ministre de la Justice Robert Badinter."
                    },
                    "narrationText": "Testez vos acquis : sous quel Président la peine de mort a-t-elle été abolie en mille neuf cent quatre-vingt-un ? Choisissez la bonne réponse pour valider la leçon.",
                    "takeaway": "Bravo ! Vous connaissez parfaitement les grands repères de la Ve République.",
                    "audioSrc": "audio/video_lessons/m4-c3/scene_6.mp3"
                }
            ]
        },

        "m4-c4": {
            "chapterId": "m4-c4",
            "moduleId": "module-4",
            "title": "Géographie, Reliefs et Territoire Français",
            "subtitle": "L'Hexagone, fleuves, massifs montagneux, mers et pays frontaliers",
            "totalScenes": 6,
            "estimatedDuration": "2 min",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "L'Hexagone et sa Superficie",
                    "badge": "Le Territoire National",
                    "durationSeconds": 18,
                    "visualTheme": "tricolore",
                    "heading": "L'Hexagone Français",
                    "subheading": "Un carrefour géographique majeur au cœur de l'Europe",
                    "icon": "fa-mountain-sun",
                    "keyPoints": [
                        "Surnommée « l'Hexagone » en raison de sa forme géométrique à six côtés",
                        "Plus grand pays d'Europe occidentale par sa superficie (environ 643 000 km² avec l'outre-mer)",
                        "Population : environ 68 millions d'habitants",
                        "Deuxième domaine maritime mondial grâce aux territoires d'outre-mer"
                    ],
                    "narrationText": "Bienvenue dans cette leçon de géographie. Surnommée l'Hexagone par sa forme à six côtés, la France est le plus vaste pays de l'Union européenne, avec environ soixante-huit millions d'habitants et le deuxième espace maritime de la planète.",
                    "takeaway": "La France est bordée par 4 façades maritimes.",
                    "audioSrc": "audio/video_lessons/m4-c4/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Les 5 Grands Fleuves de France",
                    "badge": "Hydrographie",
                    "durationSeconds": 22,
                    "visualTheme": "liberte",
                    "heading": "Les Cinq Grands Fleuves Français",
                    "subheading": "La Seine, la Loire, le Rhône, la Garonne et le Rhin",
                    "icon": "fa-water",
                    "keyPoints": [
                        "La Loire : le plus long fleuve de France (1 006 km), célèbre pour ses châteaux",
                        "La Seine : traverse Paris et Rouen avant de se jeter dans la Manche au Havre",
                        "Le Rhône : fleuve le plus puissant, prend sa source en Suisse et se jette en Méditerranée",
                        "La Garonne : traverse Toulouse et Bordeaux, formant l'estuaire de la Gironde",
                        "Le Rhin : fleuve frontière naturel entre la France et l'Allemagne"
                    ],
                    "narrationText": "La France est irriguée par cinq grands fleuves : la Loire, le plus long avec plus de mille kilomètres, la Seine qui traverse Paris, le puissant Rhône qui descend vers la Méditerranée, la Garonne dans le Sud-Ouest, et le Rhin à la frontière allemande.",
                    "takeaway": "La Loire est le plus long fleuve entièrement situé en France.",
                    "audioSrc": "audio/video_lessons/m4-c4/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Les Massifs Montagneux & Le Mont Blanc",
                    "badge": "Reliefs & Sommets",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Les Chaînes de Montagnes et le Toit de l'Europe",
                    "subheading": "Alpes, Pyrénées, Massif central, Jura et Vosges",
                    "icon": "fa-mountain",
                    "keyPoints": [
                        "Les Alpes : abritent le Mont Blanc, plus haut sommet d'Europe occidentale (4 807 mètres)",
                        "Les Pyrénées : barrière naturelle séparant la France de l'Espagne",
                        "Le Massif central : plus grand massif montagneux au centre de la France (volcans d'Auvergne)",
                        "Le Jura et les Vosges : massifs bordant l'Est et les frontières suisse et allemande"
                    ],
                    "narrationText": "Le relief français comprend cinq grands massifs montagneux : les Alpes, qui culminent au sommet du Mont Blanc à quatre mille huit cent sept mètres, les Pyrénées à la frontière espagnole, le Massif central et ses volcans, le Jura et les Vosges.",
                    "takeaway": "Le Mont Blanc culmine à 4 807 mètres d'altitude.",
                    "audioSrc": "audio/video_lessons/m4-c4/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "Les Mers et Pays Frontaliers",
                    "badge": "Frontières & Littoraux",
                    "durationSeconds": 20,
                    "visualTheme": "fraternite",
                    "heading": "Frontières Terrestres et Façades Maritimes",
                    "subheading": "4 mers et 8 pays frontaliers en métropole",
                    "icon": "fa-compass",
                    "keyPoints": [
                        "4 façades maritimes : La Manche, la mer du Nord, l'océan Atlantique et la mer Méditerranée",
                        "8 pays frontaliers terrestres : Belgique, Luxembourg, Allemagne, Suisse, Italie, Monaco, Espagne, Andorre",
                        "Frontières ultramarines : Le Brésil et le Suriname sont frontaliers de la Guyane française",
                        "Plus longue frontière terrestre de la France : avec le Brésil (environ 730 km)"
                    ],
                    "narrationText": "La métropole est bordée par quatre mers et huit pays voisins, dont l'Espagne, l'Italie, l'Allemagne et la Belgique. Anecdote majeure : la plus longue frontière terrestre française est partagée en Amérique du Sud entre la Guyane et le Brésil.",
                    "takeaway": "La plus longue frontière terrestre de la France est celle avec le Brésil.",
                    "audioSrc": "audio/video_lessons/m4-c4/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Fleuves & Villes",
                    "badge": "Questions Fréquentes",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Questions Types de l'Instructeur",
                    "subheading": "« Citez trois fleuves et deux massifs montagneux »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Citer sans hésiter : Seine, Loire, Rhône ou Garonne",
                        "Citer les Alpes et les Pyrénées et mentionner le Mont Blanc",
                        "Préciser le fleuve qui traverse votre propre ville ou département",
                        "Savoir citer trois grandes métropoles françaises (Paris, Marseille, Lyon, Toulouse, Nice)"
                    ],
                    "narrationText": "L'agent vous demandera de citer des fleuves ou les montagnes de France. Répondez naturellement : la Seine et la Loire pour les fleuves, les Alpes et les Pyrénées pour les montagnes, en précisant que le Mont Blanc culmine à quatre mille huit cent sept mètres.",
                    "takeaway": "Donner l'altitude du Mont Blanc (4 807 m) valorise votre préparation.",
                    "audioSrc": "audio/video_lessons/m4-c4/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos repères géographiques",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Quel est le plus long fleuve coulant entièrement sur le territoire français ?",
                        "options": [
                            "La Seine (777 km)",
                            "La Loire (1 006 km)",
                            "Le Rhône (812 km)"
                        ],
                        "correctIndex": 1,
                        "explanation": "La Loire est le plus long fleuve de France avec une longueur de 1 006 kilomètres, prenant sa source au mont Gerbier-de-Jonc."
                    },
                    "narrationText": "Vérifions vos connaissances : quel est le plus long fleuve de France ? Cliquez sur la bonne réponse pour valider la leçon.",
                    "takeaway": "Bravo ! Vous maîtrisez la géographie française.",
                    "audioSrc": "audio/video_lessons/m4-c4/scene_6.mp3"
                }
            ]
        },

        "m4-c5": {
            "chapterId": "m4-c5",
            "moduleId": "module-4",
            "title": "Culture, Patrimoine, Gastronomie et Sciences",
            "subtitle": "Écrivains, peintres, scientifiques, monuments et art de vivre français",
            "totalScenes": 6,
            "estimatedDuration": "2 min 05",
            "scenes": [
                {
                    "id": "scene-1",
                    "number": 1,
                    "title": "Le Rayonnement Culturel de la France",
                    "badge": "Patrimoine Mondial",
                    "durationSeconds": 18,
                    "visualTheme": "tricolore",
                    "heading": "La France et le Rayonnement Culturel",
                    "subheading": "Un patrimoine littéraire, artistique et architectural d'exception",
                    "icon": "fa-palette",
                    "keyPoints": [
                        "Première destination touristique mondiale (monuments, musées, paysages)",
                        "Musée du Louvre : plus grand musée d'art du monde (La Joconde, Vénus de Milo)",
                        "Monuments emblématiques : Tour Eiffel (1889), Arc de Triomphe, Notre-Dame de Paris",
                        "Châteaux de la Loire et château de Versailles classés à l'UNESCO"
                    ],
                    "narrationText": "Bienvenue dans cette leçon consacrée à la culture française. Reconnue dans le monde entier pour ses écrivains, ses peintres, son architecture et sa gastronomie, la France cultive un attachement passionné à la création et à l'esprit critique.",
                    "takeaway": "La Tour Eiffel a été construite par Gustave Eiffel pour l'Exposition universelle de 1889.",
                    "audioSrc": "audio/video_lessons/m4-c5/scene_1.mp3"
                },
                {
                    "id": "scene-2",
                    "number": 2,
                    "title": "Les Grands Écrivains et Dramaturges",
                    "badge": "Littérature & Théâtre",
                    "durationSeconds": 22,
                    "visualTheme": "liberte",
                    "heading": "De Molière à Victor Hugo",
                    "subheading": "Les géants des lettres françaises",
                    "icon": "fa-book",
                    "keyPoints": [
                        "Molière (XVIIe siècle) : le génie du théâtre comique (Le Malade imaginaire, Tartuffe)",
                        "Jean de La Fontaine : Les Fables (morale populaire et intemporelle)",
                        "Victor Hugo (XIXe siècle) : Les Misérables, Notre-Dame de Paris, député républicain",
                        "Émile Zola : Germinal, et son célèbre « J'accuse » pour défendre Dreyfus"
                    ],
                    "narrationText": "La langue française est souvent appelée la « langue de Molière » en hommage au célèbre dramaturge du dix-septième siècle. Au dix-neuvième siècle, Victor Hugo incarne le génie romantique et l'engagement républicain avec Les Misérables.",
                    "takeaway": "Le français est surnommé la « langue de Molière ».",
                    "audioSrc": "audio/video_lessons/m4-c5/scene_2.mp3"
                },
                {
                    "id": "scene-3",
                    "number": 3,
                    "title": "Les Savants et Scientifiques Illustres",
                    "badge": "Sciences & Progrès",
                    "durationSeconds": 20,
                    "visualTheme": "egalite",
                    "heading": "Pasteur et Marie Curie : Le Progrès Médical",
                    "subheading": "Des découvertes qui ont sauvé des millions de vies",
                    "icon": "fa-flask",
                    "keyPoints": [
                        "Louis Pasteur : inventeur du vaccin contre la rage en 1885 et de la pasteurisation",
                        "Marie Curie : deux prix Nobel (Physique et Chimie) pour ses travaux sur la radioactivité",
                        "Première femme inhumée au Panthéon pour ses propres mérites",
                        "Le Panthéon à Paris : « Aux grands hommes, la Patrie reconnaissante »"
                    ],
                    "narrationText": "La France est une terre de science. Louis Pasteur invente le vaccin contre la rage en dix-huit cent quatre-vingt-cinq, révolutionnant la médecine. Marie Curie, double prix Nobel de physique et chimie, repose au Panthéon au côté des plus illustres personnalités de la Nation.",
                    "takeaway": "Marie Curie est la première femme honorée au Panthéon pour ses mérites scientifiques.",
                    "audioSrc": "audio/video_lessons/m4-c5/scene_3.mp3"
                },
                {
                    "id": "scene-4",
                    "number": 4,
                    "title": "La Gastronomie et l'Art de Vivre",
                    "badge": "Patrimoine Immatériel UNESCO",
                    "durationSeconds": 18,
                    "visualTheme": "fraternite",
                    "heading": "Le Repas Gastronomique des Français",
                    "subheading": "Classé au patrimoine culturel immatériel de l'humanité",
                    "icon": "fa-utensils",
                    "keyPoints": [
                        "Repas gastronomique français inscrit au patrimoine de l'UNESCO depuis 2010",
                        "Art du bien manger et de la convivialité : entrée, plat, fromages et dessert",
                        "Plats emblématiques : bœuf bourguignon, pot-au-feu, quiche lorraine, ratatouille",
                        "La baguette de pain française : inscrite elle aussi à l'UNESCO en 2022"
                    ],
                    "narrationText": "En France, la gastronomie est bien plus qu'une cuisine : c'est un art de vivre et un moment de partage inscrit à l'UNESCO. De la baguette traditionnelle aux grands fromages et vins de terroir, elle fait la fierté de nos régions.",
                    "takeaway": "La baguette de pain et le repas gastronomique sont tous deux inscrits à l'UNESCO.",
                    "audioSrc": "audio/video_lessons/m4-c5/scene_4.mp3"
                },
                {
                    "id": "scene-5",
                    "number": 5,
                    "title": "Conseils Entretien : Auteurs & Peintres",
                    "badge": "Culture Générale",
                    "durationSeconds": 18,
                    "visualTheme": "interview",
                    "heading": "Questions Types de l'Instructeur",
                    "subheading": "« Citez un écrivain, un scientifique et un monument français »",
                    "icon": "fa-user-tie",
                    "keyPoints": [
                        "Écrivains sûrs à citer : Victor Hugo (Les Misérables), Molière, Émile Zola",
                        "Scientifiques incontournables : Louis Pasteur (vaccin contre la rage), Marie Curie",
                        "Peintres : Claude Monet (Les Nymphéas), Auguste Renoir (impressionnisme)",
                        "Plat français préféré : ayez un exemple personnel prêt à partager avec enthousiasme"
                    ],
                    "narrationText": "L'agent instructeur vous demandera de citer vos auteurs préférés, un scientifique ou un plat français. Citez Victor Hugo, Louis Pasteur ou Claude Monet, et exprimez avec sincérité ce que vous appréciez dans la culture française.",
                    "takeaway": "Parler avec passion d'un livre ou d'un lieu français plaît énormément à l'agent.",
                    "audioSrc": "audio/video_lessons/m4-c5/scene_5.mp3"
                },
                {
                    "id": "scene-6",
                    "number": 6,
                    "title": "Checkpoint : Mini-Quiz Vidéo",
                    "badge": "Auto-Évaluation",
                    "durationSeconds": 16,
                    "visualTheme": "quiz",
                    "heading": "Validez vos Connaissances",
                    "subheading": "Testez vos acquis sur la culture française",
                    "icon": "fa-circle-check",
                    "quiz": {
                        "question": "Quel scientifique français a découvert le vaccin contre la rage en 1885 ?",
                        "options": [
                            "Louis Pasteur",
                            "Marie Curie",
                            "René Descartes"
                        ],
                        "correctIndex": 0,
                        "explanation": "Louis Pasteur a mis au point le vaccin contre la rage en 1885 et a fondé l'Institut Pasteur, pionnier mondial de la recherche microbiologique."
                    },
                    "narrationText": "Testez vos connaissances : quel scientifique français a inventé le vaccin contre la rage en mille huit cent quatre-vingt-cinq ? Choisissez la bonne réponse.",
                    "takeaway": "Bravo ! Vous maîtrisez les grandes figures de la culture et de la science françaises.",
                    "audioSrc": "audio/video_lessons/m4-c5/scene_6.mp3"
                }
            ]
        }
    }

def update_module3_4():
    with open("data/video_lessons.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    new_lessons = get_module3_4_lessons()
    for k, v in new_lessons.items():
        data["lessons"][k] = v

    with open("data/video_lessons.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated Module 3 and 4 lessons. Total lessons now: {len(data['lessons'])}")

if __name__ == "__main__":
    update_module3_4()
