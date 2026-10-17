#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script to produce complete, structured JSON datasets
for the French Citizenship Interview Preparation App based on the 
official 'LIVRET DU CITOYEN 2026' (Edition mai 2026, incl. Réforme 2026: Examen civique, niveau B2).
"""

import json
import os

os.makedirs('data', exist_ok=True)

# -------------------------------------------------------------
# 1. COURSE DATA (data/course.json)
# -------------------------------------------------------------
course_data = {
    "version": "2026.1",
    "title": "Livret du Citoyen 2026 – Préparation Complète à la Naturalisation",
    "description": "Cours officiel complet structuré en 5 modules thématiques + Guide de l'Examen Civique et Entretien d'assimilation.",
    "modules": [
        {
            "id": "module-1",
            "number": 1,
            "title": "Principes et Valeurs de la République",
            "subtitle": "La devise, les symboles républicains et les principes fondamentaux",
            "icon": "fa-scale-balanced",
            "badge": "Fondamental pour l'entretien",
            "description": "Comprendre les piliers de la République française : Liberté, Égalité, Fraternité, Laïcité, Indivisibilité, Démocratie et Solidarité.",
            "chapters": [
                {
                    "id": "m1-c1",
                    "title": "La Devise de la République : Liberté, Égalité, Fraternité",
                    "readTime": "8 min",
                    "badge": "Devise officielle",
                    "highlights": [
                        "La devise 'Liberté, Égalité, Fraternité' est inscrite au fronton des édifices publics (mairies, préfectures).",
                        "Liberté (Art. 4 DDHC 1789) : pouvoir faire tout ce qui ne nuit pas à autrui.",
                        "Égalité (Art. 1er Constitution 1958 & DDHC) : tous les citoyens ont les mêmes droits sans distinction de sexe, origine, religion.",
                        "L'égalité femmes-hommes est garantie par la Constitution (depuis 1946) et s'applique partout (travail, famille, santé).",
                        "Fraternité : esprit de solidarité et d'entraide entre tous les membres de la communauté nationale."
                    ],
                    "content": [
                        {
                            "type": "intro",
                            "text": "La devise de la France « Liberté, Égalité, Fraternité » consacre les valeurs fondatrices de la République française, repères communs indispensables pour le vivre-ensemble. Elle est gravée au fronton des édifices publics et sur les pièces de monnaie."
                        },
                        {
                            "type": "section",
                            "title": "1. La Liberté",
                            "text": "Les femmes et les hommes sont libres dans leurs choix, leurs opinions, leur foi et leur manière de penser et de vivre. La Déclaration des droits de l'homme et du citoyen (DDHC) du 26 août 1789 proclame en son article 4 : « La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui ».",
                            "points": [
                                "Liberté d'opinion et de conscience (croire, ne pas croire, changer de religion).",
                                "Liberté d'expression : s'exprimer librement par la parole ou l'écrit, dans le respect de la loi.",
                                "Limites légales de la liberté d'expression : l'injure, la diffamation, l'incitation à la haine ou à la violence, le négationnisme sont sévèrement punis par la loi."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "2. L'Égalité",
                            "text": "L'égalité est un principe fondamental de la République (Article 1er de la Constitution de 1958). Tous les citoyens naissent et demeurent libres et égaux en droits.",
                            "points": [
                                "Égalité devant la loi et devant la justice : la même loi s'applique à tous.",
                                "Égalité femmes-hommes : inscrite dans le Préambule de la Constitution de 1946, elle est absolue dans la vie professionnelle, politique, familiale et civile.",
                                "Lutte contre les discriminations : toute différence de traitement injustifiée liée à l'origine, au sexe, à la religion, au handicap ou à l'orientation sexuelle est un délit puni de peines d'amende et d'emprisonnement.",
                                "L'État lutte activement contre le sexisme, le racisme, l'antisémitisme et l'homophobie."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "3. La Fraternité",
                            "text": "La fraternité est le devoir de solidarité et d'entraide qui unit tous les citoyens. Elle s'incarne notamment dans le système français de protection sociale :",
                            "points": [
                                "La Sécurité sociale (créée en 1945) permet à chacun de bénéficier de soins quel que soit son revenu.",
                                "Le principe de redistribution des richesses par l'impôt pour aider les personnes vulnérables (retraités, chômeurs, personnes handicapées).",
                                "La richesse de la vie associative et du bénévolat au service de la collectivité."
                            ]
                        },
                        {
                            "type": "callout",
                            "variant": "warning",
                            "title": "💡 Question classique d'entretien",
                            "text": "L'agent préfectoral demande souvent : « Que signifie pour vous la devise française ? » ou « Quelle valeur de la devise vous touche le plus et pourquoi ? ». Préparez un exemple concret de votre vie quotidienne illustrant l'une de ces trois valeurs."
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Quelle est la devise de la République française ?",
                            "answer": "« Liberté, Égalité, Fraternité ».",
                            "tip": "Citez-la avec assurance et soyez prêt à expliquer ce qu'elle représente pour vous."
                        },
                        {
                            "question": "Donnez la définition de la liberté selon la DDHC de 1789.",
                            "answer": "La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui (Article 4).",
                            "tip": "Cette citation textuelle impressionne positivement l'examinateur."
                        },
                        {
                            "question": "Que pensez-vous de l'égalité entre les femmes et les hommes ?",
                            "answer": "En France, les femmes et les hommes ont rigoureusement les mêmes droits et devoirs : même liberté de choix professionnel, même autorité parentale sur les enfants, même salaire pour un même travail, et droit égal au respect.",
                            "tip": "C'est un point éliminatoire si l'examinateur perçoit la moindre réserve."
                        }
                    ]
                },
                {
                    "id": "m1-c2",
                    "title": "Les Symboles de la République Française",
                    "readTime": "9 min",
                    "badge": "Incontournable",
                    "image": "assets/images/marianne.png",
                    "imageCaption": "Marianne, incarnation de la République et de la Liberté",
                    "highlights": [
                        "Le drapeau tricolore : Bleu, Blanc, Rouge (bleu et rouge = couleurs de Paris, blanc = couleur du Roi).",
                        "L'hymne national : La Marseillaise, écrite en 1792 par Rouget de Lisle à Strasbourg.",
                        "Marianne : figure allégorique de la République, coiffée du bonnet phrygien (symbole d'affranchissement des esclaves antiques).",
                        "La fête nationale : 14 juillet (instauration en 1880, commémore 1789 et la Fête de la Fédération 1790).",
                        "Autres symboles : Le Coq gaulois, le Sceau de la République, le Faisceau de licteur."
                    ],
                    "content": [
                        {
                            "type": "grid",
                            "items": [
                                {
                                    "title": "Le Drapeau Tricolore",
                                    "image": "assets/images/drapeau_francais.png",
                                    "text": "Né sous la Révolution française (1789). Le blanc représentait la monarchie, entouré du bleu et du rouge, couleurs de la ville de Paris. Il est l'emblème national unique de la République (Art. 2 de la Constitution de 1958)."
                                },
                                {
                                    "title": "Marianne",
                                    "image": "assets/images/marianne.png",
                                    "text": "Elle incarne la République et les valeurs de liberté et de raison. Son buste est présent dans toutes les mairies de France et sur les timbres postaux. Elle porte le bonnet phrygien, symbole des esclaves affranchis sous l'Antiquité."
                                },
                                {
                                    "title": "La Marseillaise",
                                    "image": "assets/images/marseillaise.png",
                                    "text": "Composée dans la nuit du 25 au 26 avril 1792 par Rouget de Lisle à Strasbourg, initialement comme « Chant de guerre pour l'armée du Rhin ». Chantée par les volontaires marseillais entrant à Paris, elle devient hymne national en 1795 puis définitivement en 1879."
                                },
                                {
                                    "title": "Le 14 Juillet",
                                    "image": "assets/images/fete_nationale.png",
                                    "text": "Fête nationale instituée en 1880. Elle commémore deux dates : le 14 juillet 1789 (prise de la Bastille, chute de l'arbitraire royal) et le 14 juillet 1790 (Fête de la Fédération, union de la Nation autour de la loi)."
                                }
                            ]
                        },
                        {
                            "type": "section",
                            "title": "Les autres symboles de la France",
                            "points": [
                                "Le Coq : symbole de la vigilance et des origines gauloises (en latin, 'gallus' signifie à la fois coq et gaulois). Utilisé notamment par les équipes sportives nationales.",
                                "Le Sceau de la République : représentant la Liberté assise tenant un faisceau et un gouvernail, utilisé pour sceller les lois constitutionnelles.",
                                "Le Faisceau de licteur : symbole d'autorité et d'union républicaine (les verges liées sont indestructibles)."
                            ]
                        },
                        {
                            "type": "callout",
                            "variant": "info",
                            "title": "Paroles du 1er couplet et refrain de La Marseillaise",
                            "text": "« Allons enfants de la Patrie, le jour de gloire est arrivé ! Contre nous de la tyrannie, l'étendard sanglant est levé... Aux armes, citoyens ! Formez vos bataillons ! Marchons, marchons ! Qu'un sang impur abreuve nos sillons ! »"
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Qui a écrit la Marseillaise et en quelle année ?",
                            "answer": "Claude Joseph Rouget de Lisle en 1792.",
                            "tip": "Sachez aussi qu'elle a été composée à Strasbourg."
                        },
                        {
                            "question": "Que commémore la fête nationale du 14 juillet ?",
                            "answer": "Elle commémore la prise de la Bastille (14 juillet 1789) et la Fête de la Fédération (14 juillet 1790).",
                            "tip": "Citer les deux événements montre une maîtrise parfaite du sujet !"
                        },
                        {
                            "question": "Que porte Marianne sur la tête et que symbolise-t-il ?",
                            "answer": "Elle porte le bonnet phrygien, qui symbolise la liberté et l'émancipation (porté par les esclaves affranchis dans l'Antiquité).",
                            "tip": "Question très fréquente lors des entretiens en préfecture."
                        }
                    ]
                },
                {
                    "id": "m1-c3",
                    "title": "Les 4 Principes de la République : Indivisible, Laïque, Démocratique, Sociale",
                    "readTime": "11 min",
                    "badge": "Article 1er Constitution",
                    "highlights": [
                        "Article 1er de la Constitution de 1958 : « La France est une République indivisible, laïque, démocratique et sociale ».",
                        "Indivisible : une seule loi, une seule langue officielle (le français), intégrité du territoire métropolitain et d'outre-mer.",
                        "Laïque : séparation stricte des Églises et de l'État (loi du 9 décembre 1905). Neutralité absolue de l'État et des agents publics.",
                        "Démocratique : le pouvoir émane du peuple (« gouvernement du peuple, par le peuple et pour le peuple ») par le suffrage universel.",
                        "Sociale : la République garantit à chacun des conditions décentes d'existence et l'accès aux soins, à l'éducation et à la solidarité."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "A. Une République Indivisible",
                            "text": "L'indivisibilité signifie que la souveraineté nationale appartient au peuple dans son ensemble. Aucune section du peuple ni aucun individu ne peut s'en attribuer l'exercice. La même loi républicaine s'applique sur tout le territoire, de Dunkerque à Nouméa, sans distinction d'ethnie ou de religion.",
                            "points": [
                                "La langue de la République est le français (article 2 de la Constitution).",
                                "La France ne reconnaît aucun droit collectif spécifique à des minorités : tous les citoyens sont égaux devant la loi en tant qu'individus."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "B. Une République Laïque (Loi de 1905)",
                            "text": "La laïcité est un principe fondamental garanti par la Constitution. Elle garantit la liberté de conscience : liberté de croire ou de ne pas croire, d'avoir la religion de son choix et d'en changer.",
                            "points": [
                                "Neutralité de l'État : La République ne reconnaît, ne salarie ni ne subventionne aucun culte (Loi du 9 décembre 1905). L'État est neutre vis-à-vis de toutes les religions.",
                                "Neutralité des agents du service public : Tout agent public (fonctionnaire, enseignant, soignant à l'hôpital public, policier) a une obligation stricte de neutralité : il ne doit manifester aucune conviction religieuse ou politique dans l'exercice de ses fonctions.",
                                "École publique laïque : L'école est un lieu préservé où les élèves apprennent à développer leur esprit critique. La loi du 15 mars 2004 interdit le port de signes ou tenues par lesquels les élèves manifestent ostensiblement une appartenance religieuse dans les écoles, collèges et lycées publics.",
                                "Loi du 11 octobre 2010 : Interdiction de la dissimulation du visage dans l'espace public pour des motifs de sécurité et de réciprocité républicaine.",
                                "Le droit de critiquer les idées et religions : En France, le délit de blasphème n'existe pas. En revanche, l'injure ou l'incitation à la haine contre des personnes en raison de leur religion est sévèrement punie."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "C. Une République Démocratique et Sociale",
                            "points": [
                                "Démocratique : Suffrage universel, direct ou indirect, égal et secret. Tous les citoyens majeurs jouissent du droit de vote.",
                                "Sociale : La République lutte contre les exclusions et assure la cohésion sociale à travers les services publics, la Sécurité sociale et l'école gratuite et obligatoire de 3 à 16 ans."
                            ]
                        },
                        {
                            "type": "callout",
                            "variant": "danger",
                            "title": "⚠️ Attention – Laïcité et Entretien de Naturalisation",
                            "text": "L'examinateur teste toujours votre adhésion sincère à la laïcité. Exemples de questions pièges : « Si un médecin homme doit soigner votre femme aux urgences, l'acceptez-vous ? » (Réponse obligatoire : Oui immédiatement, les lois et règles médicales s'imposent à tous). « Les lois religieuses sont-elles supérieures aux lois de la République ? » (Réponse : Non, en France, les lois de la République sont au-dessus de tout)."
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Quels sont les 4 principes de la République française énoncés à l'article 1er de la Constitution ?",
                            "answer": "La France est une République indivisible, laïque, démocratique et sociale.",
                            "tip": "Mémorisez ces 4 adjectifs par cœur !"
                        },
                        {
                            "question": "Quelle est la date clé de la loi de séparation des Églises et de l'État ?",
                            "answer": "La loi du 9 décembre 1905.",
                            "tip": "Précisez que cette loi garantit le libre exercice des cultes tout en instaurant la neutralité religieuse de l'État."
                        },
                        {
                            "question": "Un agent public peut-il porter un signe religieux pendant son travail ?",
                            "answer": "Non, en vertu du principe de neutralité du service public, les agents publics ont l'interdiction totale de manifester leurs convictions religieuses dans leurs fonctions.",
                            "tip": "Cela vaut pour les enseignants, policiers, agents administratifs, soignants du secteur public."
                        }
                    ]
                }
            ]
        },
        {
            "id": "module-2",
            "number": 2,
            "title": "Système Institutionnel et Politique",
            "subtitle": "La séparation des pouvoirs, les institutions de la Ve République et l'Union européenne",
            "icon": "fa-landmark",
            "badge": "Institutions de l'État",
            "description": "Découvrez le fonctionnement démocratique de la France : Président, Gouvernement, Parlement (Assemblée nationale et Sénat), collectivités et UE.",
            "chapters": [
                {
                    "id": "m2-c1",
                    "title": "La Séparation des Pouvoirs et l'État de Droit",
                    "readTime": "8 min",
                    "badge": "Démocratie",
                    "highlights": [
                        "Théorisée par Montesquieu dans 'L'Esprit des lois' (1748) pour éviter la tyrannie.",
                        "Pouvoir exécutif : applique les lois et conduit la politique de la Nation (Président de la République + Premier ministre et Gouvernement).",
                        "Pouvoir législatif : vote les lois et contrôle le gouvernement (Parlement = Assemblée nationale + Sénat).",
                        "Pouvoir judiciaire : applique les lois et règle les litiges (Magistrats indépendants, juges et tribunaux)."
                    ],
                    "content": [
                        {
                            "type": "intro",
                            "text": "L'État de droit est un système institutionnel dans lequel la puissance publique est soumise au droit. Nul n'est au-dessus des lois, pas même les dirigeants. La séparation des trois pouvoirs garantit les libertés des citoyens."
                        },
                        {
                            "type": "grid",
                            "items": [
                                {
                                    "title": "Pouvoir Exécutif",
                                    "icon": "fa-user-tie",
                                    "text": "Le Président de la République (chef de l'État, garant de la Constitution) et le Premier ministre (chef du Gouvernement, applique les lois)."
                                },
                                {
                                    "title": "Pouvoir Législatif",
                                    "icon": "fa-landmark-dome",
                                    "text": "Le Parlement bicaméral composé de l'Assemblée nationale (577 députés) et du Sénat (348 sénateurs). Ils discutent, amendent et votent les lois."
                                },
                                {
                                    "title": "Pouvoir Judiciaire",
                                    "icon": "fa-gavel",
                                    "text": "Les cours et tribunaux, gardiens de la liberté individuelle, veillent au respect de la loi en toute indépendance."
                                }
                            ]
                        },
                        {
                            "type": "section",
                            "title": "Le Conseil Constitutionnel",
                            "points": [
                                "Composé de 9 membres nommés pour 9 ans (3 par le Président de la République, 3 par le Président de l'Assemblée, 3 par le Président du Sénat) + anciens Présidents de la République.",
                                "Rôle : veiller à la conformité des lois avec la Constitution et garantir la régularité des élections nationales."
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Qui a théorisé le principe de séparation des pouvoirs ?",
                            "answer": "Montesquieu au XVIIIe siècle.",
                            "tip": "C'est l'une des figures majeures des Lumières."
                        },
                        {
                            "question": "Quels sont les trois pouvoirs et qui les exerce en France ?",
                            "answer": "L'Exécutif (Président et Gouvernement), le Législatif (Assemblée nationale et Sénat) et le Judiciaire (les tribunaux et magistrats).",
                            "tip": "Répondez avec précision et clarté."
                        }
                    ]
                },
                {
                    "id": "m2-c2",
                    "title": "Le Président de la République et le Gouvernement",
                    "readTime": "10 min",
                    "badge": "Exécutif",
                    "image": "assets/images/assemblee_nationale.png",
                    "imageCaption": "L'Hémicycle du Palais Bourbon (Assemblée Nationale)",
                    "highlights": [
                        "Le Président de la République réside au Palais de l'Élysée.",
                        "Élu au suffrage universel direct pour un mandat de 5 ans (quinquennat), renouvelable une seule fois consécutivement.",
                        "Il est le Chef de l'État, Chef des armées, garant de la Constitution et de l'indépendance nationale.",
                        "Il nomme le Premier ministre (qui réside à l'Hôtel de Matignon) et les ministres sur proposition de ce dernier.",
                        "Il a le pouvoir de dissoudre l'Assemblée nationale (Article 12 de la Constitution).",
                        "L'Assemblée nationale peut renverser le Gouvernement par le vote d'une motion de censure."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "Le Président de la République",
                            "points": [
                                "Promulgue les lois votées par le Parlement dans les 15 jours.",
                                "Dispose du droit de grâce présidentielle.",
                                "Négocie et ratifie les traités internationaux.",
                                "Peut recourir au référendum (Article 11) ou aux pleins pouvoirs en cas de crise majeure (Article 16)."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "Le Parlement Français",
                            "points": [
                                "L'Assemblée Nationale : siège au Palais Bourbon à Paris. Composée de 577 députés élus au suffrage universel direct pour 5 ans. En cas de désaccord persistant avec le Sénat, l'Assemblée a le dernier mot.",
                                "Le Sénat : siège au Palais du Luxembourg à Paris. Composé de 348 sénateurs élus au suffrage universel indirect pour 6 ans (renouvelé par moitié tous les 3 ans) par les grands électeurs (maires, conseillers municipaux, départementaux et régionaux). Le Président du Sénat assure l'intérim de la présidence de la République en cas de vacance."
                            ]
                        },
                        {
                            "type": "callout",
                            "variant": "info",
                            "title": "💡 Qui est le Président actuel ?",
                            "text": "Emmanuel Macron, élu en mai 2017 et réélu en avril 2022. Connaître également le nom du Premier ministre en fonction au jour de votre entretien est indispensable !"
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Pour combien d'années est élu le Président de la République et comment ?",
                            "answer": "Pour 5 ans (quinquennat) au suffrage universel direct au scrutin uninominal majoritaire à deux tours.",
                            "tip": "Le passage du septennat (7 ans) au quinquennat date de l'an 2000."
                        },
                        {
                            "question": "Où réside le Président de la République et où réside le Premier ministre ?",
                            "answer": "Le Président réside au Palais de l'Élysée et le Premier ministre à l'Hôtel de Matignon.",
                            "tip": "Indiquez également le Palais Bourbon (Assemblée) et le Palais du Luxembourg (Sénat)."
                        },
                        {
                            "question": "Qui remplace le Président de la République en cas de décès ou de démission ?",
                            "answer": "Le Président du Sénat assure l'intérim.",
                            "tip": "C'est déjà arrivé avec Alain Poher en 1969 et 1974."
                        }
                    ]
                },
                {
                    "id": "m2-c3",
                    "title": "L'Organisation Territoriale : Communes, Départements, Régions et Outre-Mer",
                    "readTime": "9 min",
                    "badge": "Territoire",
                    "image": "assets/images/carte_regions.png",
                    "imageCaption": "Carte des Régions administratives de France",
                    "highlights": [
                        "3 échelons de collectivités territoriales : la Commune, le Département, la Région.",
                        "La France compte environ 35 000 communes, 101 départements (96 en métropole + 5 en outre-mer) et 18 régions (13 métropolitaines + 5 d'outre-mer).",
                        "Le Maire est à la fois représentant de la commune et agent de l'État (officier d'état civil, célèbre les mariages).",
                        "Le Préfet représente l'État dans le département et la région : garant de l'ordre public, de la sécurité et de la légalité.",
                        "Les 5 DROM (Départements et Régions d'Outre-Mer) : Guadeloupe, Martinique, Guyane, La Réunion, Mayotte."
                    ],
                    "content": [
                        {
                            "type": "grid",
                            "items": [
                                {
                                    "title": "La Commune",
                                    "icon": "fa-city",
                                    "text": "Dirigée par le Maire et le Conseil municipal. Compétences : écoles maternelles et primaires, état civil, urbanisme, police municipale, voirie locale."
                                },
                                {
                                    "title": "Le Département (101)",
                                    "icon": "fa-map-location-dot",
                                    "text": "Dirigé par le Conseil départemental. Compétences : action sociale (RSA, aide sociale à l'enfance, personnes âgées et handicapées), collèges, routes départementales."
                                },
                                {
                                    "title": "La Région (18)",
                                    "icon": "fa-layer-group",
                                    "text": "Dirigée par le Conseil régional. Compétences : développement économique, lycées, transports régionaux (trains TER), aménagement du territoire."
                                },
                                {
                                    "title": "L'Outre-Mer (DROM-COM)",
                                    "icon": "fa-earth-americas",
                                    "text": "5 DROM (Guadeloupe, Martinique, Guyane, Réunion, Mayotte) soumis aux lois françaises et droit de l'UE. Et collectivités à statut particulier (Polynésie française, Nouvelle-Calédonie, Saint-Barthélemy, Saint-Martin, Saint-Pierre-et-Miquelon, Wallis-et-Futuna)."
                                }
                            ]
                        },
                        {
                            "type": "callout",
                            "variant": "warning",
                            "title": "💡 Questions locales à l'entretien",
                            "text": "On vous demandera systématiquement : « Quel est le nom de votre maire ? », « Dans quel département et région habitez-vous ? », « Quel est le chef-lieu (préfecture) de votre département ? ». Renseignez-vous scrupuleusement avant le jour J !"
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Combien y a-t-il de départements et de régions en France ?",
                            "answer": "101 départements (96 en métropole et 5 en outre-mer) et 18 régions (13 métropolitaines et 5 ultramarines).",
                            "tip": "Donnez les chiffres précis."
                        },
                        {
                            "question": "Citez les 5 départements et régions d'outre-mer (DROM).",
                            "answer": "La Guadeloupe, la Martinique, la Guyane, La Réunion et Mayotte.",
                            "tip": "Mémorisez-les tous les 5, c'est une question très fréquente."
                        },
                        {
                            "question": "Quel est le rôle du Préfet ?",
                            "answer": "Le Préfet est le représentant de l'État dans le département ou la région. Il est responsable de la sécurité publique, de l'ordre public, de la gestion des crises et de l'application des lois.",
                            "tip": "Rappelez-vous que c'est en préfecture que se déroule votre entretien !"
                        }
                    ]
                },
                {
                    "id": "m2-c4",
                    "title": "La France dans l'Union Européenne",
                    "readTime": "8 min",
                    "badge": "Europe",
                    "image": "assets/images/carte_europe.png",
                    "imageCaption": "Carte des pays membres de l'Union européenne",
                    "highlights": [
                        "La France est un des 6 pays fondateurs de la construction européenne (traité de Rome de 1957).",
                        "L'Union européenne compte aujourd'hui 27 pays membres.",
                        "Les symboles de l'UE : le drapeau bleu à 12 étoiles dorées, l'hymne européen (l'Ode à la joie de Beethoven), la devise 'Unie dans la diversité', la fête de l'Europe le 9 mai.",
                        "La monnaie unique : l'Euro (€), mis en circulation le 1er janvier 2002.",
                        "L'Espace Schengen : libre circulation des personnes sans contrôle aux frontières intérieures.",
                        "Les institutions européennes : Parlement européen (Strasbourg), Commission européenne (Bruxelles), Conseil européen, Banque Centrale Européenne (Francfort)."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "Les Pères Fondateurs et Grandes Étapes",
                            "points": [
                                "Pères fondateurs français : Robert Schuman (déclaration du 9 mai 1950) et Jean Monnet.",
                                "1951 : CECA (Communauté européenne du charbon et de l'acier) entre 6 pays (France, Allemagne, Italie, Belgique, Pays-Bas, Luxembourg).",
                                "1957 : Traité de Rome instituant la CEE (marché commun).",
                                "1992 : Traité de Maastricht créant l'Union Européenne et la citoyenneté européenne.",
                                "2002 : Mise en circulation des pièces et billets en Euro."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "La Citoyenneté Européenne",
                            "text": "Tout citoyen français est automatiquement citoyen européen. Cela confère le droit de circuler, résider et travailler librement dans tous les pays de l'Union, ainsi que le droit de vote et d'éligibilité aux élections municipales et européennes dans son pays de résidence.",
                            "points": [
                                "Le Parlement européen siège à Strasbourg en France.",
                                "Les citoyens de l'Union élisent leurs députés européens tous les 5 ans."
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Combien de pays compte l'Union européenne ?",
                            "answer": "27 pays membres (depuis le départ du Royaume-Uni en 2020 / Brexit).",
                            "tip": "Ne dites pas 28 !"
                        },
                        {
                            "question": "Où siège le Parlement européen ?",
                            "answer": "À Strasbourg, en France.",
                            "tip": "C'est une grande fierté pour la France d'accueillir cette institution majeure."
                        },
                        {
                            "question": "Quel est l'hymne européen et qui l'a composé ?",
                            "answer": "L'Ode à la joie, extrait de la 9e symphonie de Ludwig van Beethoven.",
                            "tip": "Connaître aussi la date de la journée de l'Europe : le 9 mai."
                        }
                    ]
                }
            ]
        },
        {
            "id": "module-3",
            "number": 3,
            "title": "Droits et Devoirs des Citoyens",
            "subtitle": "Les libertés fondamentales, les obligations civiques et les valeurs républicaines",
            "icon": "fa-user-shield",
            "badge": "Fondement du pacte citoyen",
            "description": "Comprenez en profondeur l'équilibre républicain : liberté individuelle, justice, égalité, et les devoirs civiques (impôts, lois, défense, environnement).",
            "chapters": [
                {
                    "id": "m3-c1",
                    "title": "Les Droits Fondamentaux et Libertés Individuelles",
                    "readTime": "9 min",
                    "badge": "Droits de l'Homme",
                    "image": "assets/images/ddhc_1789.png",
                    "imageCaption": "Déclaration des Droits de l'Homme et du Citoyen de 1789",
                    "highlights": [
                        "Les droits fondamentaux sont proclamés par la DDHC de 1789, le Préambule de la Constitution de 1946 et la Charte de l'environnement de 2004.",
                        "Libertés individuelles : liberté d'opinion, liberté de culte, liberté d'expression, liberté d'aller et venir.",
                        "Droit à la dignité et respect du corps humain : abolition de la peine de mort en France (loi Badinter de 1981).",
                        "Constitutionnalisation de l'IVG en 2024 : la liberté des femmes de recourir à l'interruption volontaire de grossesse est désormais inscrite dans la Constitution.",
                        "Droit au respect de la vie privée et inviolabilité du domicile."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "Les Libertés Individuelles et Collectives",
                            "points": [
                                "Liberté d'aller et venir : chaque citoyen peut se déplacer librement et s'installer où il le souhaite en France et dans l'UE.",
                                "Liberté de réunion et de manifestation : le droit de manifester pacifiquement sur la voie publique après déclaration préalable en préfecture ou mairie.",
                                "Liberté d'association (loi de 1901) : droit de créer librement une association à but non lucratif.",
                                "Droit de grève : garanti par la Constitution dans le respect des lois et de la continuité des services essentiels.",
                                "Liberté syndicale : droit d'adhérer au syndicat professionnel de son choix."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "Les Droits Politiques et Civiques",
                            "points": [
                                "Le droit de vote : accessible à tout citoyen majeur jouissant de ses droits civils et politiques.",
                                "L'éligibilité : droit de se présenter comme candidat aux élections républicaines.",
                                "L'accès égal aux emplois publics sans distinction d'origine sociale ou de conviction."
                            ]
                        },
                        {
                            "type": "callout",
                            "variant": "info",
                            "title": "💡 Récence constitutionnelle 2024",
                            "text": "La France est devenue en mars 2024 le premier pays au monde à inscrire explicitement la liberté garantie d'avoir recours à l'IVG (Interruption Volontaire de Grossesse) dans sa Constitution (article 34). Mentionner ce fait montre que vous suivez l'actualité juridique française !"
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "En quelle année la peine de mort a-t-elle été abolie en France et par qui ?",
                            "answer": "En 1981, sous la présidence de François Mitterrand, grâce au combat du ministre de la Justice Robert Badinter.",
                            "tip": "C'est une date historique indispensable à retenir."
                        },
                        {
                            "question": "Quelle grande liberté a été inscrite dans la Constitution en 2024 ?",
                            "answer": "La liberté de recourir à l'IVG (Interruption Volontaire de Grossesse).",
                            "tip": "Ce fait récent est très apprécié des examinateurs."
                        },
                        {
                            "question": "Qu'est-ce que la loi de 1901 ?",
                            "answer": "C'est la loi qui garantit la liberté d'association à but non lucratif en France.",
                            "tip": "Plus d'un million d'associations existent en France grâce à cette loi."
                        }
                    ]
                },
                {
                    "id": "m3-c2",
                    "title": "Les Devoirs et Obligations Civiques",
                    "readTime": "8 min",
                    "badge": "Devoirs du Citoyen",
                    "image": "assets/images/charte_citoyen.png",
                    "imageCaption": "Charte des droits et devoirs du citoyen",
                    "highlights": [
                        "Être citoyen français implique autant de devoirs que de droits.",
                        "Le respect des lois et de la Constitution est une obligation absolue pour tous.",
                        "L'obligation fiscale : contribuer aux charges publiques selon ses capacités financières par l'impôt.",
                        "Le devoir de défense et de sécurité nationale : recensement citoyen à 16 ans et participation à la JDC (Journée Défense et Citoyenneté).",
                        "Le devoir civique de juré d'assises : tiré au sort sur les listes électorales, le citoyen participe directement à la justice criminelle.",
                        "La scolarité obligatoire de 3 à 16 ans pour tous les enfants résidant en France.",
                        "Le devoir écologique : préserver et améliorer l'environnement (Charte de l'environnement de 2004)."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "1. Le Respect des Lois et des Institutions",
                            "text": "L'adage « Nul n'est censé ignorer la loi » rappelle que chacun doit respecter l'ordre légal républicain. Nul ne peut se soustraire à la règle commune en invoquant des préceptes religieux, culturels ou personnels."
                        },
                        {
                            "type": "section",
                            "title": "2. Contribuer aux Charges Publiques (L'Impôt)",
                            "text": "L'article 13 de la DDHC de 1789 dispose qu'une contribution commune est indispensable pour l'entretien de la force publique et les dépenses d'administration. Elle est répartie entre tous les citoyens en raison de leurs facultés.",
                            "points": [
                                "L'impôt sur le revenu (progressif selon les revenus).",
                                "La TVA (Taxe sur la Valeur Ajoutée) payée sur les biens et services consommés.",
                                "Les cotisations sociales finançant la santé, les retraites et le chômage."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "3. Participation à la Justice et à la Défense",
                            "points": [
                                "Juré d'assises : devoir civique obligatoire si l'on est tiré au sort (sauf motif impérieux admis par la commission). Le juré siège aux côtés des magistrats professionnels pour juger les crimes.",
                                "Journée Défense et Citoyenneté (JDC) : obligatoire pour tous les jeunes Français entre 16 et 25 ans, elle sensibilise aux enjeux de la défense nationale."
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Quels sont les principaux devoirs d'un citoyen français ?",
                            "answer": "Respecter les lois de la République, payer ses impôts et cotisations, participer à la défense nationale (JDC), respecter autrui et les règles de civisme, et siéger comme juré d'assises si l'on est tiré au sort.",
                            "tip": "Citez au moins 4 devoirs distincts."
                        },
                        {
                            "question": "Le vote est-il obligatoire en France ?",
                            "answer": "Le vote est un droit civique et un devoir moral, mais il n'est pas juridiquement obligatoire en France (sauf pour les sénatoriales où les grands électeurs ont obligation de voter).",
                            "tip": "Précisez la nuance entre devoir civique et obligation pénale."
                        },
                        {
                            "question": "Pouvez-vous refuser d'être juré d'assises ?",
                            "answer": "Non, c'est une obligation civique citoyenne. On ne peut être dispensé que pour des motifs graves prévus par la loi (âge de plus de 70 ans, maladie invalidante, motif professionnel exceptionnel reconnu par la cour).",
                            "tip": "Réponse ferme : c'est un devoir direct de souveraineté populaire."
                        }
                    ]
                }
            ]
        },
        {
            "id": "module-4",
            "number": 4,
            "title": "Histoire, Géographie et Culture Françaises",
            "subtitle": "Les grandes étapes de l'histoire, le territoire, les grands personnages et le patrimoine",
            "icon": "fa-monument",
            "badge": "Cœur de l'examen civique",
            "description": "De la préhistoire à nos jours : rois de France, Révolution, guerres mondiales, présidents de la Ve République, géographie et rayonnement culturel.",
            "chapters": [
                {
                    "id": "m4-c1",
                    "title": "Les Grandes Périodes et Rois de France",
                    "readTime": "12 min",
                    "badge": "Histoire de France",
                    "image": "assets/images/revolution_bastille.png",
                    "imageCaption": "La Prise de la Bastille (14 juillet 1789)",
                    "highlights": [
                        "Antiquité : Les Gaulois (Vercingétorix vaincu à Alésia en 52 av. J.-C. par Jules César).",
                        "Moyen Âge : Clovis (1er roi des Francs baptisé vers 496), Charlemagne (couronné empereur en 800), Jeanne d'Arc (héroïne de la guerre de Cent Ans, délivre Orléans en 1429).",
                        "Renaissance : François Ier (ordonnance de Villers-Cotterêts de 1539 établissant le français comme langue officielle de l'administration).",
                        "Guerres de religion & Monarchie : Henri IV (Édit de Nantes de 1598 accordant la liberté de culte aux protestants).",
                        "Monarchie absolue : Louis XIV, le « Roi-Soleil » (château de Versailles, règne de 1643 à 1715).",
                        "Siècle des Lumières (XVIIIe siècle) : Voltaire, Rousseau, Montesquieu, Diderot.",
                        "Révolution française (1789) : Prise de la Bastille (14 juillet), abolition des privilèges (4 août), Déclaration des Droits de l'Homme (26 août), Proclamation de la 1ère République (1792)."
                    ],
                    "content": [
                        {
                            "type": "timeline",
                            "events": [
                                { "date": "52 av. J.-C.", "title": "Bataille d'Alésia", "desc": "Vercingétorix dépose les armes devant Jules César. Début de la Gaule romaine." },
                                { "date": "496", "title": "Baptême de Clovis", "desc": "Premier roi des Francs à se convertir au christianisme à Reims." },
                                { "date": "800", "title": "Couronnement de Charlemagne", "desc": "Sacré empereur d'Occident à Rome, il développe l'éducation et les écoles." },
                                { "date": "1429", "title": "Épopée de Jeanne d'Arc", "desc": "Libère Orléans assiégée par les Anglais pendant la guerre de Cent Ans." },
                                { "date": "1539", "title": "Ordonnance de Villers-Cotterêts", "desc": "François Ier impose la langue française pour tous les actes juridiques." },
                                { "date": "1598", "title": "Édit de Nantes", "desc": "Henri IV met fin aux guerres de religion en accordant la tolérance aux protestants." },
                                { "date": "1661-1715", "title": "Règne personnel de Louis XIV", "desc": "Apogée de la monarchie absolue de droit divin et construction de Versailles." },
                                { "date": "1789", "title": "Révolution Française", "desc": "Fin de l'Ancien Régime, abolition de la société d'ordres et affirmation de la souveraineté de la Nation." }
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Qui était le premier roi des Francs chrétien ?",
                            "answer": "Clovis, baptisé à Reims vers 496.",
                            "tip": "Cet événement fonde la lignée des rois de France."
                        },
                        {
                            "question": "Qui a rédigé l'ordonnance de Villers-Cotterêts et pourquoi est-elle célèbre ?",
                            "answer": "Le roi François Ier en 1539. Elle a imposé le français à la place du latin dans tous les actes administratifs et de justice.",
                            "tip": "C'est l'acte de naissance officiel du français comme langue de l'État."
                        },
                        {
                            "question": "Citez 3 philosophes du siècle des Lumières.",
                            "answer": "Voltaire, Jean-Jacques Rousseau, Montesquieu (ou Denis Diderot).",
                            "tip": "Sachez qu'ils défendaient la raison, la liberté et l'esprit critique."
                        }
                    ]
                },
                {
                    "id": "m4-c2",
                    "title": "Du XIXe Siècle aux Deux Guerres Mondiales",
                    "readTime": "11 min",
                    "badge": "Histoire Moderne",
                    "image": "assets/images/napoleon.png",
                    "imageCaption": "Napoléon Ier, empereur des Français et créateur du Code Civil",
                    "highlights": [
                        "Napoléon Ier : Coup d'État du 18 Brumaire (1799), sacré Empereur en 1804. Il crée le Code civil (1804), les préfectures, les lycées, la Légion d'honneur et la Banque de France.",
                        "1848 : IIe République, abolition définitive de l'esclavage par Victor Schœlcher et instauration du suffrage universel masculin.",
                        "1870-1940 : IIIe République. Grandes lois républicaines : liberté de la presse (1881), école laïque, gratuite et obligatoire (Jules Ferry, 1881-1882), liberté d'association (1901), séparation des Églises et de l'État (1905).",
                        "Première Guerre Mondiale (1914-1918) : Bataille de Verdun (1916). Armistice signé le 11 novembre 1918 (jour férié).",
                        "Seconde Guerre Mondiale (1939-1945) : Appel du 18 juin 1940 par le général de Gaulle depuis Londres. Résistance unifiée par Jean Moulin. Régime de Vichy du maréchal Pétain (collaboration). Débarquement de Normandie (6 juin 1944). Victoire du 8 mai 1945 (jour férié).",
                        "1944 : Droit de vote accordé aux femmes en France par ordonnance du général de Gaulle."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "Figures Majeures du XXe Siècle",
                            "points": [
                                "Général Charles de Gaulle (1890-1970) : Chef de la France Libre pendant l'Occupation, libérateur de Paris, fondateur de la Ve République en 1958.",
                                "Jean Moulin (1899-1943) : Préfet résistant, envoyé par de Gaulle pour unifier la Résistance au sein du Conseil National de la Résistance (CNR). Mort sous la torture de la Gestapo, ses cendres reposent au Panthéon.",
                                "Simone Veil (1927-2017) : Rescapée d'Auschwitz, ministre de la Santé (loi dépénalisant l'avortement en 1975), 1ère présidente du Parlement européen élu au suffrage universel. Panthéonisée en 2018."
                            ]
                        },
                        {
                            "type": "callout",
                            "variant": "warning",
                            "title": "💡 Dates commémoratives fériées à retenir",
                            "text": "8 mai (Victoire 1945 contre le nazisme), 14 juillet (Fête nationale), 11 novembre (Armistice de 1918)."
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "En quelle année les femmes ont-elles obtenu le droit de vote en France ?",
                            "answer": "En 1944 (ordonnance du 21 avril 1944 signée par le général de Gaulle), et elles ont voté pour la première fois en 1945.",
                            "tip": "C'est l'une des questions les plus posées en entretien !"
                        },
                        {
                            "question": "Qui était Jean Moulin ?",
                            "answer": "Un préfet et héros de la Résistance qui a unifié les mouvements de résistance intérieure sous l'autorité du général de Gaulle avant d'être capturé et tué par les nazis en 1943.",
                            "tip": "Citez le CNR (Conseil National de la Résistance) et le Panthéon."
                        },
                        {
                            "question": "Que célèbre-t-on le 8 mai et le 11 novembre ?",
                            "answer": "Le 8 mai commémore la fin de la Seconde Guerre mondiale en Europe (victoire des Alliés en 1945). Le 11 novembre commémore l'armistice de la Première Guerre mondiale (1918).",
                            "tip": "Ne confondez jamais les deux conflits !"
                        }
                    ]
                },
                {
                    "id": "m4-c3",
                    "title": "La Ve République et ses Présidents",
                    "readTime": "9 min",
                    "badge": "Ve République (1958-présent)",
                    "image": "assets/images/de_gaulle.png",
                    "imageCaption": "Le Général de Gaulle, fondateur de la Ve République",
                    "highlights": [
                        "Née en 1958 sous l'impulsion du Général de Gaulle avec la Constitution du 4 octobre 1958.",
                        "Les 8 Présidents de la Ve République :",
                        "1. Charles de Gaulle (1958-1969)",
                        "2. Georges Pompidou (1969-1974)",
                        "3. Valéry Giscard d'Estaing (1974-1981)",
                        "4. François Mitterrand (1981-1995, 2 mandats de 7 ans)",
                        "5. Jacques Chirac (1995-2007, mandat de 7 ans puis quinquennat en 2002)",
                        "6. Nicolas Sarkozy (2007-2012)",
                        "7. François Hollande (2012-2017)",
                        "8. Emmanuel Macron (2017 à aujourd'hui, réélu en 2022)."
                    ],
                    "content": [
                        {
                            "type": "table",
                            "headers": ["Président", "Mandat", "Faits marquants"],
                            "rows": [
                                ["Charles de Gaulle", "1958-1969", "Constitution de 1958, suffrage universel direct en 1962, décolonisation."],
                                ["Georges Pompidou", "1969-1974", "Modernisation industrielle, création du Centre Pompidou."],
                                ["Valéry Giscard d'Estaing", "1974-1981", "Majorité à 18 ans (au lieu de 21), dépénalisation de l'IVG (loi Veil)."],
                                ["François Mitterrand", "1981-1995", "Abolition de la peine de mort (1981), 5e semaine de congés payés, retraite à 60 ans."],
                                ["Jacques Chirac", "1995-2007", "Passage au quinquennat (5 ans), refus de la guerre en Irak (2003), passage à l'Euro."],
                                ["Nicolas Sarkozy", "2007-2012", "Réforme constitutionnelle de 2008, gestion de la crise financière."],
                                ["François Hollande", "2012-2017", "Mariage pour tous (2013), accords de Paris sur le climat (COP21 en 2015)."],
                                ["Emmanuel Macron", "2017-présent", "Réformes économiques, gestion de la crise Covid, inscription de l'IVG dans la Constitution (2024), JO Paris 2024."]
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "En quelle année a été fondée la Ve République et qui en est le fondateur ?",
                            "answer": "En 1958, fondée par le général Charles de Gaulle.",
                            "tip": "C'est la Constitution actuelle de la France."
                        },
                        {
                            "question": "Citez dans l'ordre chronologique 4 présidents de la Ve République.",
                            "answer": "Exemple : Charles de Gaulle, Georges Pompidou, François Mitterrand, Jacques Chirac, Emmanuel Macron.",
                            "tip": "Savoir réciter les 8 présidents dans l'ordre impressionne énormément les agents !"
                        },
                        {
                            "question": "Sous quel président la majorité civile a-t-elle été abaissée à 18 ans ?",
                            "answer": "Sous Valéry Giscard d'Estaing en 1974.",
                            "tip": "Auparavant, la majorité civile était fixée à 21 ans."
                        }
                    ]
                },
                {
                    "id": "m4-c4",
                    "title": "Géographie, Reliefs et Territoire Français",
                    "readTime": "10 min",
                    "badge": "Géographie de la France",
                    "image": "assets/images/carte_geographie.png",
                    "imageCaption": "Reliefs, fleuves et massifs montagneux français",
                    "highlights": [
                        "Superficie : 675 000 km² (métropole + outre-mer). Population en 2025/2026 : environ 68,6 millions d'habitants.",
                        "Forme de l'Hexagone avec trois façades maritimes (Manche/Mer du Nord, Océan Atlantique, Mer Méditerranée).",
                        "Pays frontaliers terrestres (8) : Belgique, Luxembourg, Allemagne, Suisse, Italie, Monaco, Espagne, Andorre (+ Brésil et Suriname en Guyane).",
                        "Les 5 grands fleuves français : La Loire (le plus long, 1 006 km), la Seine (traverse Paris), le Rhône (le plus puissant, se jette dans la Méditerranée), la Garonne (se jette dans l'Atlantique), le Rhin (frontière avec l'Allemagne).",
                        "Les 5 massifs montagneux : Les Alpes (point culminant : Mont Blanc, 4 807 m), les Pyrénées, le Massif central, le Jura et les Vosges.",
                        "2e domaine maritime mondial grâce aux territoires d'outre-mer (10 millions de km² de ZEE)."
                    ],
                    "content": [
                        {
                            "type": "grid",
                            "items": [
                                {
                                    "title": "Les Fleuves Majeurs",
                                    "text": "• La Loire (1 006 km) : Châteaux célèbres, traverse Orléans, Tours, Nantes.\n• La Seine (777 km) : Traverse Troyes, Paris, Rouen et se jette au Havre.\n• Le Rhône (812 km) : Prend sa source en Suisse, traverse Lyon, Avignon, Arles.\n• La Garonne (529 km) : Source en Espagne, traverse Toulouse et Bordeaux.\n• Le Rhin : Fleuve d'Europe du Nord-Ouest, frontière naturelle franco-allemande."
                                },
                                {
                                    "title": "Les Massifs Montagneux",
                                    "text": "• Les Alpes : Frontière avec l'Italie et la Suisse. Mont-Blanc (4 807 m), plus haut sommet d'Europe occidentale.\n• Les Pyrénées : Frontière naturelle avec l'Espagne et l'Andorre.\n• Le Massif Central : Zone de moyenne montagne et volcans éteints d'Auvergne.\n• Le Jura : Frontière avec la Suisse.\n• Les Vosges : Massif au nord-est de la France."
                                }
                            ]
                        },
                        {
                            "type": "section",
                            "title": "Les Départements et Régions d'Outre-Mer (DROM)",
                            "points": [
                                "Guadeloupe (Basse-Terre) - Mer des Caraïbes",
                                "Martinique (Fort-de-France) - Mer des Caraïbes",
                                "Guyane (Cayenne) - Amérique du Sud (base spatiale européenne de Kourou, forêt amazonienne, frontière avec le Brésil)",
                                "La Réunion (Saint-Denis) - Océan Indien (Piton de la Fournaise)",
                                "Mayotte (Dzaoudzi / Mamoudzou) - Océan Indien"
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Quel est le plus long fleuve de France et quel fleuve traverse Paris ?",
                            "answer": "La Loire est le plus long fleuve (1 006 km) et la Seine traverse Paris.",
                            "tip": "Citez également le Rhône et la Garonne si possible."
                        },
                        {
                            "question": "Quel est le point culminant de la France et son altitude ?",
                            "answer": "Le Mont Blanc dans les Alpes, culminant à 4 807 mètres (environ 4 808 m).",
                            "tip": "C'est le plus haut sommet d'Europe occidentale."
                        },
                        {
                            "question": "Quels pays ont une frontière terrestre avec la France métropolitaine ?",
                            "answer": "L'Espagne, l'Italie, la Suisse, l'Allemagne, la Belgique, le Luxembourg, Monaco et Andorre.",
                            "tip": "Mentionnez également le Brésil et le Suriname si l'on prend en compte la Guyane !"
                        }
                    ]
                },
                {
                    "id": "m4-c5",
                    "title": "Culture, Patrimoine, Gastronomie et Sciences",
                    "readTime": "11 min",
                    "badge": "Culture Française",
                    "image": "assets/images/patrimoine_tour_eiffel.png",
                    "imageCaption": "La Tour Eiffel, symbole mondial de Paris et de la France",
                    "highlights": [
                        "Monuments emblématiques : Tour Eiffel (conçue par Gustave Eiffel pour l'exposition universelle de 1889), Musée du Louvre (le plus grand musée d'art du monde, la Joconde), Abbaye du Mont-Saint-Michel, Château de Versailles, Notre-Dame de Paris.",
                        "Écrivains et poètes : Molière, Victor Hugo ('Les Misérables'), Voltaire, Émile Zola, Albert Camus, Marcel Proust, Jean de La Fontaine.",
                        "Artistes peintres : Claude Monet (impressionnisme), Auguste Renoir, Eugène Delacroix ('La Liberté guidant le peuple').",
                        "Savants illustres : Marie Curie (physicienne d'origine polonaise naturalisée française, double prix Nobel de physique et chimie), Louis Pasteur (inventeur du vaccin contre la rage en 1885).",
                        "Gastronomie : Le repas gastronomique des Français est classé au patrimoine mondial immatériel de l'UNESCO depuis 2010. Pains (baguette classée UNESCO), vins, plus de 1 000 variétés de fromages (Camembert, Roquefort, Comté).",
                        "Événements majeurs récents : Jeux Olympiques et Paralympiques de Paris 2024, Tour de France cycliste, Festival de Cannes."
                    ],
                    "content": [
                        {
                            "type": "grid",
                            "items": [
                                {
                                    "title": "Patrimoine & Monuments",
                                    "image": "assets/images/patrimoine_mont_saint_michel.png",
                                    "text": "Le Mont-Saint-Michel (merveille de l'Occident entre Normandie et Bretagne), les Châteaux de la Loire (Chambord, Chenonceau), le Pont du Gard, la Cathédrale Notre-Dame de Paris reconstruite."
                                },
                                {
                                    "title": "Sciences & Médecine",
                                    "image": "assets/images/marie_curie.png",
                                    "text": "Marie Curie (première femme lauréate d'un prix Nobel et seule femme à en avoir reçu deux, reposant au Panthéon) et Louis Pasteur (fondateur de la microbiologie et du vaccin antirabique)."
                                },
                                {
                                    "title": "Art & Peinture",
                                    "image": "assets/images/delacroix_liberte.png",
                                    "text": "Eugène Delacroix : 'La Liberté guidant le peuple' (1830), tableau mythique conservé au Musée du Louvre incarnant le combat républicain pour la liberté."
                                },
                                {
                                    "title": "La Gastronomie",
                                    "image": "assets/images/patrimoine_chateaux_loire.png",
                                    "text": "Classée par l'UNESCO. La culture du partage du repas, des produits du terroir, la tradition viticole et la diversité culinaire régionale."
                                }
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Qui a peint 'La Liberté guidant le peuple' ?",
                            "answer": "Eugène Delacroix en 1830.",
                            "tip": "Ce tableau symbolise les Trois Glorieuses et la République."
                        },
                        {
                            "question": "Qui était Marie Curie ?",
                            "answer": "Une physicienne d'origine polonaise naturalisée française, pionnière de l'étude de la radioactivité, double prix Nobel (physique et chimie), inhumée au Panthéon.",
                            "tip": "Exemple parfait d'assimilation et de contribution au rayonnement français."
                        },
                        {
                            "question": "Citez 3 écrivains français célèbres.",
                            "answer": "Victor Hugo, Molière, Voltaire (ou Albert Camus, Émile Zola).",
                            "tip": "Donnez aussi le titre d'une œuvre (ex: Les Misérables de Victor Hugo)."
                        }
                    ]
                }
            ]
        },
        {
            "id": "module-5",
            "number": 5,
            "title": "Vivre dans la Société Française",
            "subtitle": "La vie quotidienne, le travail, la famille et les règles de civisme",
            "icon": "fa-people-roof",
            "badge": "Intégration & Quotidien",
            "description": "Les repères indispensables pour réussir son intégration : santé, travail (CDI, SMIC, 35h), éducation des enfants, mariage civil et numéros d'urgence.",
            "chapters": [
                {
                    "id": "m5-c1",
                    "title": "La Vie Quotidienne, Santé et Sécurité",
                    "readTime": "8 min",
                    "badge": "Quotidien & Numéros d'urgence",
                    "highlights": [
                        "Le système de santé : l'Assurance maladie (Sécurité sociale) rembourse une partie des soins, complétée par une mutuelle (complémentaire santé).",
                        "La Carte Vitale permet la télétransmission électronique des feuilles de soins.",
                        "Numéros d'urgence gratuits 24h/24 :",
                        "• 15 : SAMU (urgence médicale vitale)",
                        "• 17 : Police ou Gendarmerie (secours immédiat)",
                        "• 18 : Sapeurs-pompiers (incendie, accident)",
                        "• 112 : Numéro d'urgence européen unique",
                        "• 114 : Numéro d'urgence pour personnes sourdes et malentendantes (par SMS)",
                        "• 3919 : Numéro d'écoute pour les violences faites aux femmes",
                        "• 119 : Enfance en danger.",
                        "Le respect de l'espace public : interdiction de fumer dans les lieux fermés accueillant du public, tri sélectif des déchets, respect du code de la route."
                    ],
                    "content": [
                        {
                            "type": "table",
                            "headers": ["Numéro", "Service", "Quand l'utiliser ?"],
                            "rows": [
                                ["15", "SAMU", "Détresse vitale, malaise cardiaque, coma, accident grave."],
                                ["17", "Police / Gendarmerie", "Agression, cambriolage, accident avec délit de fuite."],
                                ["18", "Pompiers", "Incendie, fuite de gaz, accident de la route avec blessés."],
                                ["112", "Urgence Européenne", "Numéro universel fonctionnant depuis tout téléphone dans l'UE."],
                                ["114", "Urgence SMS", "Pour personnes sourdes, aphasiques ou muettes."],
                                ["3919", "Violences conjugales", "Écoute anonyme et gratuite pour femmes victimes de violences."],
                                ["119", "Enfance en danger", "Signalement de maltraitance d'enfants ou adolescents."]
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Quels sont les numéros d'urgence du SAMU, de la Police et des Pompiers ?",
                            "answer": "15 pour le SAMU, 17 pour la Police/Gendarmerie, 18 pour les Pompiers (et 112 au niveau européen).",
                            "tip": "Réponse immédiate et sans hésitation exigée !"
                        },
                        {
                            "question": "Quel est le numéro d'urgence européen ?",
                            "answer": "Le 112.",
                            "tip": "Fonctionne gratuitement depuis n'importe quel téléphone fixe ou mobile."
                        }
                    ]
                },
                {
                    "id": "m5-c2",
                    "title": "Travailler en France et Droits des Salariés",
                    "readTime": "8 min",
                    "badge": "Emploi & Droit du Travail",
                    "image": "assets/images/organisation_travail.png",
                    "imageCaption": "Schéma de l'organisation et du droit du travail",
                    "highlights": [
                        "Le contrat de travail : le CDI (Contrat à Durée Indéterminée) est la forme normale et générale de la relation de travail. Le CDD (Contrat à Durée Déterminée) est une exception encadrée par la loi.",
                        "La durée légale de travail : fixée à 35 heures par semaine (les heures au-delà sont des heures supplémentaires).",
                        "Le SMIC (Salaire Minimum Interprofessionnel de Croissance) : garantit le salaire horaire minimum en dessous duquel aucun salarié ne peut être rémunéré.",
                        "Les congés payés : 5 semaines de congés payés par an (2,5 jours ouvrables par mois travaillé).",
                        "Le dialogue social : liberté syndicale, droit de grève et présence du CSE (Comité Social et Économique) dans les entreprises.",
                        "L'accès à l'emploi public : l'accès aux postes de fonctionnaires titulaires d'autorité publique (police, magistrature, diplomatie) requiert la nationalité française."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "Les Principes Clés du Travail en France",
                            "points": [
                                "Égalité professionnelle femmes-hommes : interdiction absolue de discrimination salariale ou d'embauche liée au sexe, à la maternité ou à la situation familiale.",
                                "Santé et sécurité : l'employeur a l'obligation légale de protéger la santé physique et mentale de ses salariés.",
                                "L'Inspection du travail : veille à l'application du Code du travail et des conventions collectives."
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Quelle est la durée légale hebdomadaire du travail en France ?",
                            "answer": "35 heures par semaine.",
                            "tip": "Instaurée par les lois Aubry en 1998-2000."
                        },
                        {
                            "question": "Que signifie le sigle SMIC ?",
                            "answer": "Salaire Minimum Interprofessionnel de Croissance.",
                            "tip": "Mémorisez la signification exacte des lettres."
                        },
                        {
                            "question": "Combien de semaines de congés payés a un salarié en France ?",
                            "answer": "5 semaines de congés payés par an.",
                            "tip": "Acquis en 1982 sous la présidence de François Mitterrand."
                        }
                    ]
                },
                {
                    "id": "m5-c3",
                    "title": "La Famille, l'Éducation et la Protection de l'Enfance",
                    "readTime": "9 min",
                    "badge": "Vie Familiale & Enfance",
                    "highlights": [
                        "Le mariage civil : seul le mariage civil célébré à la mairie par le maire ou son adjoint a une valeur juridique légale en France. Le mariage religieux est facultatif et ne peut jamais être célébré avant le mariage civil.",
                        "Interdiction absolue de la polygamie et des mariages forcés en France.",
                        "Le PACS (Pacte Civil de Solidarité) : contrat entre deux personnes majeures de même sexe ou de sexe différent pour organiser leur vie commune.",
                        "L'autorité parentale conjointe : exercée à égalité par le père et la mère dans l'intérêt supérieur de l'enfant.",
                        "L'instruction obligatoire : obligatoire pour tous les enfants de 3 à 16 ans (filles et garçons sans distinction).",
                        "L'interdiction des violences corporelles : la loi interdit tout châtiment corporel envers les enfants.",
                        "La protection des mineurs face aux écrans et au numérique."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "Le Mariage Républicain",
                            "text": "Le mariage républicain est fondé sur le libre consentement mutuel des époux. Les deux conjoints sont égaux en droits et en devoirs. La loi punit sévèrement les mariages forcés ou arrangés contre la volonté des intéressés.",
                            "points": [
                                "Le mariage pour tous (loi de 2013) : ouvre le mariage et l'adoption aux couples de personnes de même sexe.",
                                "En France, la polygamie est strictement interdite par la loi."
                            ]
                        },
                        {
                            "type": "section",
                            "title": "L'École Républicaine",
                            "points": [
                                "Obligatoire dès 3 ans (école maternelle) jusqu'à 16 ans.",
                                "Gratuite et laïque dans l'enseignement public.",
                                "Mixité obligatoire : les filles et les garçons suivent les mêmes cours ensemble (sport, sciences, etc.)."
                            ]
                        },
                        {
                            "type": "callout",
                            "variant": "danger",
                            "title": "⚠️ Piège fréquent en entretien",
                            "text": "L'agent peut vous demander : « Vos enfants peuvent-ils refuser d'assister aux cours de piscine ou de sciences naturelles à l'école pour des motifs religieux ? ». Réponse impérative : Non, la fréquentation de tous les cours du programme scolaire est obligatoire pour tous les élèves, sans exception religieuse."
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "À partir de quel âge l'école est-elle obligatoire en France ?",
                            "answer": "À partir de 3 ans (depuis la rentrée 2019) et jusqu'à 16 ans.",
                            "tip": "Précisez que cela concerne garçons et filles avec le même programme."
                        },
                        {
                            "question": "Un mariage religieux a-t-il une valeur légale en France ?",
                            "answer": "Non, seul le mariage civil célébré en mairie par un officier d'état civil a une valeur juridique. Célébrer un mariage religieux avant le mariage civil est même puni par la loi.",
                            "tip": "C'est une illustration majeure de la laïcité de l'État civil."
                        },
                        {
                            "question": "La polygamie est-elle autorisée en France ?",
                            "answer": "Non, la polygamie est strictement interdite en France. Un citoyen ne peut être marié qu'à une seule personne à la fois.",
                            "tip": "Répondre avec fermeté."
                        }
                    ]
                }
            ]
        },
        {
            "id": "module-6",
            "number": 6,
            "title": "Guide de l'Examen Civique et Entretien 2026",
            "subtitle": "La réforme 2026 : Examen civique officiel, niveau B2 et préparation à l'entretien préfectoral",
            "icon": "fa-user-graduate",
            "badge": "Réforme 2026 Officielle",
            "description": "Tout ce que vous devez savoir sur la nouvelle procédure 2026 : Examen civique officiel pour constituer votre dossier, exigence de niveau B2 et simulation d'entretien.",
            "chapters": [
                {
                    "id": "m6-c1",
                    "title": "La Réforme 2026 : Examen Civique et Niveau B2",
                    "readTime": "7 min",
                    "badge": "Nouveautés 2026",
                    "highlights": [
                        "Nouveau prérequis 2026 : Maîtrise de la langue française au niveau B2 (oral ET écrit) du CECRL (au lieu du niveau B1 précédemment).",
                        "L'Examen Civique Officiel : nouveau test standardisé de connaissances civiques obligatoire pour la recevabilité de votre dossier.",
                        "L'Entretien individuel en préfecture ou consulat : évalue votre degré d'assimilation, votre adhésion aux valeurs républicaines et votre pratique dans la vie quotidienne.",
                        "Critères d'assimilation : connaissance de la langue, respect des valeurs (laïcité, égalité hommes-femmes), intégration professionnelle et absence de condamnations pénales."
                    ],
                    "content": [
                        {
                            "type": "section",
                            "title": "Les 3 Piliers de l'Évaluation 2026",
                            "points": [
                                "1. Le niveau de langue B2 : attester d'une aisance courante pour comprendre, échanger et s'exprimer par écrit et oral.",
                                "2. L'Examen civique : QCM de connaissances portant fidèlement sur le contenu du Livret du Citoyen (notre simulateur d'examen 2026 reproduit exactement ce format).",
                                "3. L'Entretien d'assimilation : un entretien individuel de 30 à 45 minutes face à un agent de préfecture pour vérifier votre sincérité républicaine."
                            ]
                        }
                    ],
                    "interviewQuestions": [
                        {
                            "question": "Quel niveau de français est exigé en 2026 pour la naturalisation ?",
                            "answer": "Le niveau B2 oral et écrit du cadre européen commun de référence pour les langues (CECRL).",
                            "tip": "Montrez que vous connaissez les exigences actuelles."
                        },
                        {
                            "question": "Pourquoi souhaitez-vous devenir français(e) ?",
                            "answer": "Pour m'engager pleinement dans la Nation, partager ses valeurs de liberté, d'égalité et de laïcité, participer à la vie démocratique par le vote et construire mon avenir et celui de ma famille dans cette communauté nationale.",
                            "tip": "Exprimez une adhésion sincère aux valeurs et un projet de vie durable."
                        }
                    ]
                }
            ]
        }
    ]
}

with open('data/course.json', 'w', encoding='utf-8') as f:
    json.dump(course_data, f, ensure_ascii=False, indent=2)

print('Generated data/course.json successfully.')

