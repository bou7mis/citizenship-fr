#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script to produce comprehensive Flashcards dataset (data/flashcards.json)
covering all key concepts, dates, personalities, geography, institutions, and rights/duties.
"""

import json
import os

flashcards = [
    # --- SYMBOLES & VALEURS ---
    {
        "id": "fc-1",
        "category": "Symboles & Valeurs",
        "tag": "Devise",
        "front": "Quelle est la devise officielle de la République française ?",
        "back": "« Liberté, Égalité, Fraternité ».\n\nInscrite à l'article 2 de la Constitution de 1958 et au fronton des mairies et bâtiments officiels.",
        "tip": "Sachez expliquer ce que représente pour vous chacune de ces trois valeurs."
    },
    {
        "id": "fc-2",
        "category": "Symboles & Valeurs",
        "tag": "Drapeau",
        "front": "Quelles sont les couleurs du drapeau français et que signifient-elles ?",
        "back": "Bleu, Blanc, Rouge.\n\nLe bleu et le rouge sont les couleurs de Paris ; le blanc était la couleur de la monarchie. Il est né sous la Révolution française (1789).",
        "tip": "C'est l'emblème national unique défini par l'article 2 de la Constitution."
    },
    {
        "id": "fc-3",
        "category": "Symboles & Valeurs",
        "tag": "Marianne",
        "front": "Que représente Marianne et quel symbole porte-t-elle sur la tête ?",
        "back": "Marianne incarne la République et la Liberté.\n\nElle est coiffée du bonnet phrygien, symbole des esclaves affranchis dans l'Antiquité romaine.",
        "tip": "Son buste est présent dans chaque mairie de France."
    },
    {
        "id": "fc-4",
        "category": "Symboles & Valeurs",
        "tag": "Hymne",
        "front": "Quel est l'hymne national de la France, qui l'a écrit et quand ?",
        "back": "La Marseillaise, écrite par Claude Joseph Rouget de Lisle à Strasbourg en 1792.",
        "tip": "Elle s'appelait initialement 'Chant de guerre pour l'armée du Rhin'."
    },
    {
        "id": "fc-5",
        "category": "Symboles & Valeurs",
        "tag": "Fête nationale",
        "front": "Que célèbre la France chaque 14 juillet lors de la fête nationale ?",
        "back": "1. La prise de la Bastille (14 juillet 1789).\n2. La Fête de la Fédération (14 juillet 1790) unissant la Nation.",
        "tip": "Instituée fête nationale en 1880 sous la IIIe République."
    },
    {
        "id": "fc-6",
        "category": "Symboles & Valeurs",
        "tag": "Coq",
        "front": "Pourquoi le coq est-il un symbole de la France ?",
        "back": "En latin, le mot 'gallus' signifie à la fois 'coq' et 'gaulois'.\n\nIl incarne la fierté, la vigilance et le courage.",
        "tip": "Fréquemment arboré par les sportifs et sur les monuments aux morts."
    },

    # --- PRINCIPES & LAÏCITÉ ---
    {
        "id": "fc-7",
        "category": "Principes Républicains",
        "tag": "Article 1er",
        "front": "Quels sont les 4 principes de la République proclamés à l'article 1er de la Constitution ?",
        "back": "La France est une République :\n1. Indivisible\n2. Laïque\n3. Démocratique\n4. Sociale",
        "tip": "À savoir impérativement par cœur !"
    },
    {
        "id": "fc-8",
        "category": "Principes Républicains",
        "tag": "Laïcité",
        "front": "Que prévoit la loi du 9 décembre 1905 sur la séparation des Églises et de l'État ?",
        "back": "« La République ne reconnaît, ne salarie ni ne subventionne aucun culte ».\n\nElle garantit le libre exercice des cultes et la neutralité religieuse de l'État.",
        "tip": "La laïcité protège la liberté de croire ou de ne pas croire."
    },
    {
        "id": "fc-9",
        "category": "Principes Républicains",
        "tag": "Agents publics",
        "front": "Quelle est l'obligation des fonctionnaires et agents du service public concernant la religion ?",
        "back": "Une obligation stricte de neutralité religieuse, philosophique et politique pendant leur service.",
        "tip": "Interdiction absolue de porter des signes religieux ostensibles."
    },
    {
        "id": "fc-10",
        "category": "Principes Républicains",
        "tag": "École",
        "front": "Que dispose la loi du 15 mars 2004 dans les écoles publiques ?",
        "back": "Elle interdit aux élèves le port de signes ou de tenues manifestant ostensiblement une appartenance religieuse dans les écoles, collèges et lycées publics.",
        "tip": "L'école publique est un espace d'émancipation et d'esprit critique."
    },
    {
        "id": "fc-11",
        "category": "Principes Républicains",
        "tag": "Blasphème",
        "front": "Existe-t-il un délit de blasphème en France ?",
        "back": "Non. Le blasphème n'est pas un délit en France : on peut critiquer, caricaturer ou débattre des religions.\n\nEn revanche, l'injure ou la haine contre les croyants est punie par la loi.",
        "tip": "C'est l'essence même de la liberté d'expression."
    },
    {
        "id": "fc-12",
        "category": "Principes Républicains",
        "tag": "Égalité",
        "front": "Quelle est la règle concernant l'égalité entre les femmes et les hommes ?",
        "back": "L'égalité absolue en droits, en devoirs, dans la famille, au travail, dans la société et en politique (garantie constitutionnelle depuis 1946).",
        "tip": "Aucun prétexte culturel ou religieux ne peut justifier une inégalité."
    },

    # --- INSTITUTIONS & POLITIQUE ---
    {
        "id": "fc-13",
        "category": "Institutions",
        "tag": "Séparation des pouvoirs",
        "front": "Quels sont les trois pouvoirs et qui les exerce en France ?",
        "back": "• Pouvoir exécutif : Président de la République et Gouvernement\n• Pouvoir législatif : Parlement (Assemblée nationale + Sénat)\n• Pouvoir judiciaire : Juges et tribunaux indépendants",
        "tip": "Théorisé par Montesquieu en 1748."
    },
    {
        "id": "fc-14",
        "category": "Institutions",
        "tag": "Président",
        "front": "Pour combien de temps le Président de la République est-il élu et comment ?",
        "back": "Pour 5 ans (quinquennat) au suffrage universel direct au scrutin majoritaire uninominal à 2 tours.\n\nLimité à deux mandats consécutifs.",
        "tip": "Résidence : Le Palais de l'Élysée."
    },
    {
        "id": "fc-15",
        "category": "Institutions",
        "tag": "Premier Ministre",
        "front": "Qui nomme le Premier ministre et où réside-t-il ?",
        "back": "Le Premier ministre est nommé par le Président de la République.\n\nIl réside à l'Hôtel de Matignon à Paris.",
        "tip": "Il dirige l'action du Gouvernement et est responsable devant le Parlement."
    },
    {
        "id": "fc-16",
        "category": "Institutions",
        "tag": "Assemblée Nationale",
        "front": "Combien y a-t-il de députés à l'Assemblée nationale et où siègent-ils ?",
        "back": "577 députés élus pour 5 ans au suffrage universel direct.\n\nIls siègent au Palais Bourbon à Paris.",
        "tip": "L'Assemblée a le dernier mot sur le Sénat en cas de désaccord sur une loi."
    },
    {
        "id": "fc-17",
        "category": "Institutions",
        "tag": "Sénat",
        "front": "Combien y a-t-il de sénateurs et où siègent-ils ?",
        "back": "348 sénateurs élus pour 6 ans au suffrage universel indirect par les grands électeurs.\n\nIls siègent au Palais du Luxembourg à Paris.",
        "tip": "Le Président du Sénat assure l'intérim de la présidence de la République."
    },
    {
        "id": "fc-18",
        "category": "Institutions",
        "tag": "Conseil constitutionnel",
        "front": "Combien de membres composent le Conseil constitutionnel et quelle est leur mission ?",
        "back": "9 membres nommés pour 9 ans (3 par le Président, 3 par le président de l'Assemblée, 3 par le président du Sénat).\n\nMission : vérifier la conformité des lois à la Constitution.",
        "tip": "Les anciens présidents de la République en sont membres de droit."
    },
    {
        "id": "fc-19",
        "category": "Institutions",
        "tag": "Territoire",
        "front": "Combien y a-t-il de départements et de régions en France ?",
        "back": "• 101 départements (96 en métropole + 5 en outre-mer)\n• 18 régions administratives (13 métropolitaines + 5 d'outre-mer)",
        "tip": "Connaître le numéro et le chef-lieu de votre propre département."
    },
    {
        "id": "fc-20",
        "category": "Institutions",
        "tag": "Outre-Mer",
        "front": "Quels sont les 5 Départements et Régions d'Outre-Mer (DROM) ?",
        "back": "1. Guadeloupe\n2. Martinique\n3. Guyane\n4. La Réunion\n5. Mayotte",
        "tip": "Ils sont soumis aux mêmes lois qu'en métropole."
    },
    {
        "id": "fc-21",
        "category": "Institutions",
        "tag": "Union Européenne",
        "front": "Combien de pays compte l'UE et où siège le Parlement européen ?",
        "back": "27 pays membres.\n\nLe Parlement européen siège à Strasbourg en France.",
        "tip": "La monnaie unique Euro (€) est entrée en vigueur le 1er janvier 2002."
    },

    # --- HISTOIRE DE FRANCE ---
    {
        "id": "fc-22",
        "category": "Histoire",
        "tag": "Antiquité",
        "front": "Qui était Vercingétorix et que s'est-il passé à Alésia en 52 av. J.-C. ?",
        "back": "Vercingétorix était le chef gaulois ayant unifié les tribus contre Rome.\n\nEn 52 av. J.-C., il est vaincu à Alésia par Jules César, marquant le début de la Gaule romaine.",
        "tip": "Premier grand héros de l'histoire sur le sol français."
    },
    {
        "id": "fc-23",
        "category": "Histoire",
        "tag": "Moyen Âge",
        "front": "Qui est Clovis et pourquoi son baptême en 496 est-il marquant ?",
        "back": "Clovis est le premier roi des Francs à se convertir au christianisme à Reims vers 496.\n\nIl unifie la Gaule sous la dynastie mérovingienne.",
        "tip": "Reims deviendra la ville du sacre de presque tous les rois de France."
    },
    {
        "id": "fc-24",
        "category": "Histoire",
        "tag": "Moyen Âge",
        "front": "En quelle année Charlemagne a-t-il été sacré empereur ?",
        "back": "En l'an 800 à Rome par le pape Léon III.\n\nIl a développé l'administration et encouragé les écoles.",
        "tip": "Couronné empereur d'Occident."
    },
    {
        "id": "fc-25",
        "category": "Histoire",
        "tag": "Moyen Âge",
        "front": "Qui était Jeanne d'Arc et quel exploit a-t-elle accompli en 1429 ?",
        "back": "Jeanne d'Arc a délivré Orléans assiégée par les Anglais pendant la guerre de Cent Ans et a fait sacrer Charles VII à Reims.",
        "tip": "Brûlée vive à Rouen en 1431, elle est une héroïne nationale."
    },
    {
        "id": "fc-26",
        "category": "Histoire",
        "tag": "Renaissance",
        "front": "Quelle est l'importance de l'ordonnance de Villers-Cotterêts signée par François Ier en 1539 ?",
        "back": "Elle a imposé la langue française comme langue officielle unique pour tous les actes administratifs et juridiques à la place du latin.",
        "tip": "Acte fondateur de la langue française dans l'État."
    },
    {
        "id": "fc-27",
        "category": "Histoire",
        "tag": "Monarchie",
        "front": "Qui a signé l'Édit de Nantes en 1598 et que prévoyait-il ?",
        "back": "Le roi Henri IV.\n\nIl accordait la liberté de culte aux protestants, mettant fin aux sanglantes guerres de religion.",
        "tip": "Révoqué plus tard par Louis XIV en 1685."
    },
    {
        "id": "fc-28",
        "category": "Histoire",
        "tag": "Monarchie",
        "front": "Quel roi a fait construire le château de Versailles et quel était son surnom ?",
        "back": "Louis XIV, surnommé le « Roi-Soleil » (règne de 1643 à 1715).\n\nSymbole absolu de la monarchie de droit divin.",
        "tip": "Plus long règne de l'histoire de France (72 ans)."
    },
    {
        "id": "fc-29",
        "category": "Histoire",
        "tag": "Lumières",
        "front": "Citez 3 philosophes majeurs du Siècle des Lumières (XVIIIe siècle).",
        "back": "1. Voltaire (tolérance, liberté de pensée)\n2. Jean-Jacques Rousseau (contrat social, égalité)\n3. Montesquieu (séparation des pouvoirs)\n(ou Denis Diderot pour l'Encyclopédie).",
        "tip": "Leurs idées ont inspiré la Révolution française."
    },
    {
        "id": "fc-30",
        "category": "Histoire",
        "tag": "Révolution 1789",
        "front": "Quelles sont les 3 dates clés de l'été 1789 ?",
        "back": "• 14 juillet 1789 : Prise de la Bastille\n• 4 août 1789 : Abolition des privilèges féodaux\n• 26 août 1789 : Déclaration des Droits de l'Homme et du Citoyen (DDHC)",
        "tip": "Marque la fin de l'Ancien Régime."
    },
    {
        "id": "fc-31",
        "category": "Histoire",
        "tag": "Empire",
        "front": "Quelles grandes créations de Napoléon Ier structurent encore la France aujourd'hui ?",
        "back": "• Le Code civil (1804)\n• Les préfets et préfectures\n• Les lycées publics\n• La Légion d'honneur\n• La Banque de France et le franc germinal",
        "tip": "Napoléon est sacré empereur à Notre-Dame le 2 décembre 1804."
    },
    {
        "id": "fc-32",
        "category": "Histoire",
        "tag": "XIXe siècle",
        "front": "En quelle année l'esclavage a-t-il été définitivement aboli en France et par qui ?",
        "back": "En 1848 sous la IIe République, grâce au décret rédigé par Victor Schœlcher.",
        "tip": "1848 instaure aussi le suffrage universel masculin."
    },
    {
        "id": "fc-33",
        "category": "Histoire",
        "tag": "IIIe République",
        "front": "Quelles lois scolaires majeures ont été votées par Jules Ferry en 1881-1882 ?",
        "back": "L'école primaire publique est devenue :\n1. Gratuite\n2. Laïque\n3. Obligatoire pour tous les enfants.",
        "tip": "Fondement de l'école républicaine."
    },
    {
        "id": "fc-34",
        "category": "Histoire",
        "tag": "14-18",
        "front": "Quelle grande bataille a marqué l'année 1916 et que célèbre-t-on le 11 novembre ?",
        "back": "• La bataille de Verdun (1916)\n• Le 11 novembre commémore l'Armistice de 1918 mettant fin à la Première Guerre mondiale.",
        "tip": "Jour férié national."
    },
    {
        "id": "fc-35",
        "category": "Histoire",
        "tag": "39-45",
        "front": "Que s'est-il passé le 18 juin 1940 et qui était Jean Moulin ?",
        "back": "• 18 juin 1940 : Appel du général de Gaulle sur la BBC à Londres fondant la Résistance.\n• Jean Moulin : Préfet unificateur des réseaux de la Résistance (CNR), mort pour la France.",
        "tip": "Les cendres de Jean Moulin reposent au Panthéon."
    },
    {
        "id": "fc-36",
        "category": "Histoire",
        "tag": "Vote des femmes",
        "front": "Quand les femmes ont-elles obtenu le droit de vote en France ?",
        "back": "Par l'ordonnance du 21 avril 1944 signée par le général de Gaulle.\n\nPremier vote des femmes en avril 1945.",
        "tip": "Question quasi-systématique en entretien !"
    },
    {
        "id": "fc-37",
        "category": "Histoire",
        "tag": "Ve République",
        "front": "En quelle année la Ve République a-t-elle été instaurée et qui était son premier président ?",
        "back": "En 1958, avec la Constitution du 4 octobre 1958.\n\nPremier président : Le général Charles de Gaulle (1958-1969).",
        "tip": "Régime constitutionnel toujours en vigueur."
    },
    {
        "id": "fc-38",
        "category": "Histoire",
        "tag": "Présidents",
        "front": "Nommez les 8 Présidents de la Ve République dans l'ordre chronologique.",
        "back": "1. Charles de Gaulle\n2. Georges Pompidou\n3. Valéry Giscard d'Estaing\n4. François Mitterrand\n5. Jacques Chirac\n6. Nicolas Sarkozy\n7. François Hollande\n8. Emmanuel Macron",
        "tip": "Connaître cette liste complète est un atout majeur !"
    },
    {
        "id": "fc-39",
        "category": "Histoire",
        "tag": "Peine de mort",
        "front": "En quelle année et sous qui la peine de mort a-t-elle été abolie en France ?",
        "back": "En 1981, sous la présidence de François Mitterrand, plaidée par le garde des Sceaux Robert Badinter.",
        "tip": "Inscrite à l'article 66-1 de la Constitution."
    },

    # --- GÉOGRAPHIE & CULTURE ---
    {
        "id": "fc-40",
        "category": "Géographie",
        "tag": "Fleuves",
        "front": "Citez les 5 grands fleuves français et indiquez le plus long.",
        "back": "1. La Loire (le plus long : 1 006 km)\n2. La Seine (traverse Paris)\n3. Le Rhône (le plus puissant, vers la Méditerranée)\n4. La Garonne (vers l'Atlantique)\n5. Le Rhin (frontière avec l'Allemagne)",
        "tip": "Question géographique très courante."
    },
    {
        "id": "fc-41",
        "category": "Géographie",
        "tag": "Montagnes",
        "front": "Quels sont les 5 principaux massifs montagneux de France métropolitaine ?",
        "back": "1. Les Alpes (Mont Blanc, 4 807 m)\n2. Les Pyrénées (frontière Espagne)\n3. Le Massif central\n4. Le Jura (frontière Suisse)\n5. Les Vosges",
        "tip": "Le Mont Blanc est le plus haut sommet d'Europe de l'Ouest."
    },
    {
        "id": "fc-42",
        "category": "Géographie",
        "tag": "Frontières",
        "front": "Quels sont les 8 pays frontaliers terrestres de la France métropolitaine ?",
        "back": "Belgique, Luxembourg, Allemagne, Suisse, Italie, Monaco, Espagne, Andorre.\n\n(+ Brésil et Suriname via la Guyane).",
        "tip": "La frontière terrestre la plus longue de France est avec le Brésil (730 km) !"
    },
    {
        "id": "fc-43",
        "category": "Culture & Sciences",
        "tag": "Sciences",
        "front": "Qui était Marie Curie et quels honneurs a-t-elle reçus ?",
        "back": "Scientifique naturalisée française d'origine polonaise, pionnière de la radioactivité.\n\nSeule personne double lauréate du prix Nobel dans deux disciplines scientifiques (Physique et Chimie). Repose au Panthéon.",
        "tip": "Exemple d'intégration et de rayonnement mondial."
    },
    {
        "id": "fc-44",
        "category": "Culture & Sciences",
        "tag": "Pasteur",
        "front": "Pour quelle découverte majeure Louis Pasteur est-il mondialement reconnu ?",
        "back": "La mise au point du vaccin contre la rage en 1885 et le procédé de pasteurisation.",
        "tip": "Fondateur de l'Institut Pasteur."
    },
    {
        "id": "fc-45",
        "category": "Culture & Sciences",
        "tag": "Littérature",
        "front": "Citez 3 grands écrivains français classiques et une œuvre pour chacun.",
        "back": "• Victor Hugo ('Les Misérables')\n• Molière ('L'Avare', 'Le Bourgeois gentilhomme')\n• Albert Camus ('L'Étranger', Prix Nobel)\n(ou Émile Zola, Voltaire, La Fontaine).",
        "tip": "Ayez toujours au moins un titre en mémoire."
    },
    {
        "id": "fc-46",
        "category": "Culture & Sciences",
        "tag": "Patrimoine",
        "front": "Citez 3 monuments français majeurs classés au patrimoine mondial de l'UNESCO.",
        "back": "1. Le Mont-Saint-Michel\n2. Le Château de Versailles\n3. La Cathédrale Notre-Dame de Paris\n(ou la Tour Eiffel, les Châteaux de la Loire).",
        "tip": "La gastronomie française est aussi inscrite au patrimoine de l'UNESCO."
    },

    # --- SOCIÉTÉ, DROIT & QUOTIDIEN ---
    {
        "id": "fc-47",
        "category": "Société & Quotidien",
        "tag": "Numéros d'urgence",
        "front": "Quels sont les 4 numéros d'urgence vitale à connaître par cœur ?",
        "back": "• 15 : SAMU (urgence médicale)\n• 17 : Police / Gendarmerie\n• 18 : Sapeurs-pompiers\n• 112 : Numéro d'urgence européen",
        "tip": "Gratuits 24h/24 depuis n'importe quel téléphone."
    },
    {
        "id": "fc-48",
        "category": "Société & Quotidien",
        "tag": "Violences & Enfance",
        "front": "Quels sont les numéros d'urgence pour les violences conjugales et l'enfance en danger ?",
        "back": "• 3919 : Violences faites aux femmes (gratuit et anonyme)\n• 119 : Enfance en danger",
        "tip": "Le 114 est le numéro d'urgence par SMS pour les sourds et malentendants."
    },
    {
        "id": "fc-49",
        "category": "Société & Quotidien",
        "tag": "Droit du travail",
        "front": "Quelles sont les durées légales du travail et des congés payés en France ?",
        "back": "• 35 heures par semaine\n• 5 semaines de congés payés par an (2,5 jours par mois)",
        "tip": "Le CDI est la forme normale du contrat de travail."
    },
    {
        "id": "fc-50",
        "category": "Société & Quotidien",
        "tag": "École",
        "front": "Quelles sont les règles de l'école républicaine en France ?",
        "back": "• Obligatoire de 3 à 16 ans\n• Gratuite et laïque dans le secteur public\n• Mixte (filles et garçons suivent les mêmes cours)",
        "tip": "La présence à tous les cours (dont sport et SVT) est obligatoire."
    },
    {
        "id": "fc-51",
        "category": "Société & Quotidien",
        "tag": "Mariage",
        "front": "Quel mariage a une valeur légale en France et qu'en est-il de la polygamie ?",
        "back": "• Seul le mariage civil en mairie est légalement reconnu.\n• La polygamie est strictement interdite et punie par la loi.",
        "tip": "Le mariage religieux avant le civil est une infraction pénale."
    },
    {
        "id": "fc-52",
        "category": "Réforme 2026",
        "tag": "Nouveautés 2026",
        "front": "Quels sont les deux grands changements de la réforme 2026 pour la naturalisation ?",
        "back": "1. Exigence du niveau B2 oral et écrit du CECRL (au lieu de B1)\n2. Mise en place de l'Examen Civique officiel pour constituer son dossier avant l'entretien.",
        "tip": "Énoncé dans l'Avant-propos de l'édition 2026 du Livret du Citoyen."
    }
]


# Import additional cards from Nationalité text export if available
import csv
import re

extra_file = 'Nationalité-20261024115852.txt'
if not os.path.exists(extra_file):
    extra_file = 'Nationalité-20261024115852.txt'

IMAGE_MAPPING = {
    # fc-70: Principaux responsables de l'État
    'paste-5cdd01775544476cc25abf83924ebbd3b4c330fa.jpg': 'assets/images/flashcards/fc_responsables_etat.png',
    # fc-155: Frontières de la France
    'paste-d35ecd0cde3208fbd6be35d7455a62d1a0fc170c.jpg': 'assets/images/flashcards/fc_frontieres_france.png',
    # fc-171: Devise de la République
    'paste-6e6a84bed2a424a8103ac5938a4066685a6e6635.jpg': 'assets/images/flashcards/fc_devise_republique.png',
    # fc-173: Laïcité
    'paste-a623ca757b4adcc2dc017ca84cabc7c1fd245b07.jpg': 'assets/images/flashcards/fc_laicite.png',
    # fc-176: Démocratie
    'paste-61465234f543ad1305253dd82c7abc8aa132ab95.jpg': 'assets/images/flashcards/fc_democratie.png',
    # fc-177: Droits et devoirs
    'f45f5d_bc1b067ee1164058adc50ddee8e99233~mv2.jpg': 'assets/images/flashcards/fc_droits_devoirs.png',
    # fc-180: Institutions françaises
    'paste-e69f51c12b375f73a8d0356a92ab367571fcc7f6.jpg': 'assets/images/flashcards/fc_institutions.png',
    # fc-181: Symboles de la France
    'paste-279b2783bfb2e521f2c18cf2745c8a7c2a74eb07.jpg': 'assets/images/flashcards/fc_symboles_france.png',
    # fc-182: Fleuves en France
    'paste-45e6d5e44dac1875bb0f4e3157c5525f9f998179.jpg': 'assets/images/flashcards/fc_fleuves_france.png',
    # fc-184: Qui est la Marianne
    'paste-4bc0c28ad4de12e442719ca2dc69e11310102016.jpg': 'assets/images/flashcards/fc_marianne.png',
    # fc-187: Régions françaises
    'paste-4def89a914656854a9b28d1f511851edf0e3e682.jpg': 'assets/images/flashcards/fc_regions_france.png',
    # fc-190: Drapeau tricolore
    'paste-68563df0ae38d17fd3d5935eaf98a174b40c66b1.jpg': 'assets/images/flashcards/fc_drapeau_francais.png',
    # fc-193: Chaînes de montagnes
    'paste-d374db7e32538acbec966411e412a6a736ee702b.jpg': 'assets/images/flashcards/fc_montagnes_france.png',
    # fc-195: Monuments parisiens
    'paste-39650343a0bfdd9dc0232878bf2069f287e76faf.jpg': 'assets/images/flashcards/fc_monuments_parisiens.png',
    # fc-198: Littéraires français
    'paste-911200cf251189bfc5f29d011989570050f176a1.jpg': 'assets/images/flashcards/fc_litteraires_francais.png',
    # fc-203: Alexandre Dumas / Trois Mousquetaires
    'paste-ba7c8c5913829c7bd7d24d8adf20dd6335550c03.jpg': 'assets/images/flashcards/fc_alexandre_dumas.png',
    # fc-205: Plats typiques français
    'paste-1ea475ebfc0877049296ba776a6fe199970f707f.jpg': 'assets/images/flashcards/fc_plats_typiques.png',
    # fc-208: Siège de l\'UE à Bruxelles
    'paste-b2ec9bc60527bab916af9ab0b937487b160dbe53.jpg': 'assets/images/flashcards/fc_siege_ue_bruxelles.png',
    # fc-212: Symboles de l\'Europe
    'paste-9b6c65e1829c82a83b09da737c2880a42b62c063.jpg': 'assets/images/flashcards/fc_symboles_europe.png',
    # fc-213: Questions sur l\'histoire de France (timeline)
    'paste-910bee63646e4909fa468fc0755ce4e538f4e699.jpg': 'assets/images/flashcards/fc_histoire_france_timeline.png',
    # fc-223: Plages du débarquement en Normandie
    'paste-9c7cc609760a3e02f8a84a24975de8f3410b89a4.jpg': 'assets/images/flashcards/fc_debarquement_normandie.png',
    # fc-229: Rois français
    'paste-65004e3bb7151ba6ad1df4beae48e639cf8bab5e.jpg': 'assets/images/flashcards/fc_rois_francais.png',
    # fc-230: Reines de France
    'paste-5adf67ec0d00530c7ab33df3a63a92b0a7f38315.jpg': 'assets/images/flashcards/fc_reines_france.png',
    # fc-231: Présidents de la Ve République
    'paste-448e4c26c9786072aa6dbc0ff785f17707676f2f.jpg': 'assets/images/flashcards/fc_presidents_ve_republique.png',
    # fc-246: Philosophes des Lumières
    'paste-837fbcbcfd3376b97c26368a83746cca08b7f968.jpg': 'assets/images/flashcards/fc_philosophes_lumieres.png',
    # fc-253: Siège de la Présidence (Palais de l\'Élysée)
    'paste-78d5949b687782bd3e3d2a547f69fed01ebf2242.jpg': 'assets/images/flashcards/fc_palais_elysee.png',
    # fc-263: Président du Sénat / Assemblée nationale
    'paste-bd0793fa6e8ab25c754d7e6ac64e67aa0df8e001.jpg': 'assets/images/flashcards/fc_president_senat.png',
    'paste-fc875a06c6a38a2ef853275833d5c3fd343dc566.jpg': 'assets/images/flashcards/fc_presidente_assemblee.png',
    # fc-273: Dernière loi marquante
    'paste-494d3aa3953efbd9879c2fae6560f3e96bde8f0e.jpg': 'assets/images/flashcards/fc_lois_marquantes.png',
    # fc-281: Sièges des 3 pouvoirs
    'paste-9b5b9544c1d436290bea0662229c199d9a9b9972.jpg': 'assets/images/flashcards/fc_sieges_pouvoirs.png',
}

if os.path.exists(extra_file):
    with open(extra_file, 'r', encoding='utf-8') as f:
        lines = [l for l in f if not l.startswith('#')]
    rows = list(csv.reader(lines, delimiter='\t'))
    
    def clean_html(text):
        t = text.strip()
        if (t.startswith('"') and t.endswith('"')) or (t.startswith("'") and t.endswith("'")):
            t = t[1:-1].strip()
        for broken_img, local_img in IMAGE_MAPPING.items():
            if broken_img in t:
                t = t.replace(broken_img, local_img)
        t = re.sub(r'(\s*<br[^>]*>\s*)+$', '', t, flags=re.IGNORECASE)
        t = re.sub(r'^(\s*<br[^>]*>\s*)+', '', t, flags=re.IGNORECASE)
        t = re.sub(r'<img\s+([^>]*?)src=([\'"][^\'"]+[\'"])', r'<img class="flashcard-img" alt="Illustration" \1src=\2', t, flags=re.IGNORECASE)
        return t.strip()

    def extract_tag_and_category(q_raw, a_raw):
        text = (q_raw + ' ' + a_raw).lower()
        if any(k in text for k in ['pourquoi voulez-vous devenir', 'pourquoi devenir français', 'vos liens en france', 'liens en france', 'votre entourage', 'argent à votre pays', 'votre ville de résidence', 'aubervilliers', 'avez-vous des liens', 'participez-vous à des associations']):
            return 'Questions Entretien', 'Entretien'
        if any(k in text for k in ['république est installée', 'première république a été proclamé', 'dates des républiques', 'déclaration des droits de l’homme', 'bastille', 'révolution', '1789', 'napoléon', 'bonaparte', 'guerre', '1914', '1939', '1945', 'de gaulle', 'moulin', 'monarchie', 'roi', 'louis', 'moyen âge', 'renaissance', 'débarquement', 'vichy', 'résistance', 'empire', 've république', 'reine', 'clovis', 'charlemagne', 'jeanne d\'arc', 'gaule', 'romains', 'esclavage', 'colonie', 'traité de verdun', 'bataille', 'histoire']):
            tag = 'Histoire'
            if 'révolution' in text or '1789' in text or 'bastille' in text: tag = 'Révolution'
            elif 'napoléon' in text or 'bonaparte' in text: tag = 'Empire'
            elif 'de gaulle' in text or 'résistance' in text or 'moulin' in text: tag = 'Résistance'
            elif 'guerre' in text or '1914' in text or '1939' in text: tag = 'Guerres Mondiales'
            elif 'roi' in text or 'monarchie' in text or 'louis' in text: tag = 'Monarchie'
            return 'Histoire', tag
        if any(k in text for k in ['principe de la france', 'gouvernement du peuple']):
            return 'Principes Républicains', 'Principes'
        if any(k in text for k in ['combien de pays compte l’ue', 'espace euro', 'commission européenne', 'parlement européen', 'union européenne', 'bruxelles', 'traité de maastricht', 'traité de rome']):
            return 'Institutions', 'Europe'
        if any(k in text for k in ['combien de personnes parlent le français', 'francophonie']):
            return 'Culture & Sciences', 'Francophonie'
        if any(k in text for k in ['spécialités gastronomiques', 'gastronomie', 'plat', 'fromage', 'vin']):
            return 'Culture & Sciences', 'Gastronomie'
        if any(k in text for k in ['fleuve', 'rivière', 'montagne', 'mont-blanc', 'mont blanc', 'alpes', 'pyrénées', 'jura', 'vosges', 'massif central', 'région', 'régions', 'departement', 'département', 'frontière', 'océan', 'mer ', 'mer,', 'mer.', 'mer\n', 'dom-tom', 'drom', 'outre-mer', 'capitale', 'climat', 'paris', 'strasbourg', 'territoire', 'point culminant', 'pays limitrophes', 'pays voisins', 'corse']):
            tag = 'Géographie'
            if 'fleuve' in text or 'rivière' in text: tag = 'Fleuves'
            elif 'montagne' in text or 'mont-blanc' in text: tag = 'Relief'
            elif 'région' in text: tag = 'Régions'
            elif 'département' in text or 'departement' in text: tag = 'Départements'
            elif 'frontière' in text or 'voisin' in text or 'limitrophe' in text: tag = 'Frontières'
            elif 'outre-mer' in text or 'dom-tom' in text or 'drom' in text: tag = 'Outre-mer'
            return 'Géographie', tag
        if any(k in text for k in ['symbole', 'devise', 'drapeau', 'marianne', 'marseillaise', 'coq', '14 juillet', 'fête nationale', 'hymne', 'bleu blanc rouge', 'fleur de lys', 'sceau', 'pantheon', 'panthéon']):
            tag = 'Symboles'
            if 'marianne' in text: tag = 'Marianne'
            elif 'devise' in text: tag = 'Devise'
            elif 'drapeau' in text: tag = 'Drapeau'
            elif 'marseillaise' in text or 'hymne' in text: tag = 'Hymne'
            elif '14 juillet' in text or 'fête' in text: tag = 'Fête Nationale'
            return 'Symboles & Valeurs', tag
        if any(k in text for k in ['laïcité', 'laicite', 'liberté', 'égalité', 'fraternité', 'droits et devoirs', 'devoir', 'droit', 'démocratie', 'démocratique', 'citoyen', 'solidarité', 'discrimination', 'suffrage universel', 'droit de vote', 'signes religieux', 'séparation des églises', 'loi de 1905', 'charte de la laïcité']):
            tag = 'Principes'
            if 'laïcité' in text or 'laicite' in text or '1905' in text or 'religieux' in text: tag = 'Laïcité'
            elif 'devoir' in text or 'droit' in text: tag = 'Droits & Devoirs'
            elif 'vote' in text or 'suffrage' in text or 'démocratie' in text: tag = 'Démocratie'
            return 'Principes Républicains', tag
        if any(k in text for k in ['président', 'premier ministre', 'ministre', 'parlement', 'assemblée nationale', 'sénat', 'député', 'sénateur', 'constitution', 'pouvoir exécutif', 'pouvoir législatif', 'pouvoir judiciaire', 'loi', 'maire', 'commune', 'élection', 'elysée', 'matignon', 'conseil constitutionnel', 'conseil d\'état', 'monnaie', 'euro', 'responsables de l’état', 'hôtel de ville', 'cohésion', 'dissolution', 'justice', 'magistrat']):
            tag = 'Institutions'
            if 'président' in text or 'elysée' in text: tag = 'Présidence'
            elif 'premier ministre' in text or 'matignon' in text: tag = 'Gouvernement'
            elif 'assemblée' in text or 'député' in text or 'sénat' in text: tag = 'Parlement'
            elif 'justice' in text or 'magistrat' in text: tag = 'Justice'
            elif 'commune' in text or 'maire' in text or 'ville' in text: tag = 'Collectivités'
            return 'Institutions', tag
        if any(k in text for k in ['peintre', 'peinture', 'lascaux', 'écrivain', 'auteur', 'musique', 'chanson', 'chanteur', 'acteur', 'cinéma', 'musée', 'monument', 'tour eiffel', 'arc de triomphe', 'versailles', 'louvre', 'mont-saint-michel', 'victor hugo', 'molière', 'pasteur', 'curie', 'sport', 'sportif', 'prix nobel', 'festival', 'littérature', 'philosoph', 'lumières', 'dumas', 'voltaire', 'rousseau', 'mousquetaires', 'château', 'cathédrale', 'académie']):
            tag = 'Culture'
            if 'musée' in text or 'monument' in text or 'tour eiffel' in text or 'versailles' in text or 'louvre' in text: tag = 'Patrimoine'
            elif 'écrivain' in text or 'auteur' in text or 'littérature' in text or 'victor hugo' in text: tag = 'Littérature'
            elif 'chanteur' in text or 'musique' in text or 'chanson' in text: tag = 'Musique'
            elif 'acteur' in text or 'cinéma' in text: tag = 'Cinéma'
            elif 'sport' in text or 'sportif' in text: tag = 'Sport'
            elif 'science' in text or 'pasteur' in text or 'curie' in text: tag = 'Sciences'
            return 'Culture & Sciences', tag
        if any(k in text for k in ['sécurité sociale', 'école', 'jules ferry', 'santé', 'impôt', 'travail', 'femme', 'femmes', 'féminine', 'ivg', 'peine de mort', 'majorité', 'mariage', 'quotidien', 'smic', 'caf', 'syndicat', 'grève', 'congés payés', '35 heures', 'retraite', 'remboursement', 'habitant', 'population', 'secteurs d’activité']):
            tag = 'Société'
            if 'sécurité sociale' in text or 'santé' in text: tag = 'Protection Sociale'
            elif 'école' in text or 'jules ferry' in text: tag = 'Éducation'
            elif 'femme' in text or 'ivg' in text: tag = 'Droits des Femmes'
            elif 'travail' in text or 'smic' in text or 'syndicat' in text: tag = 'Travail'
            elif 'impôt' in text: tag = 'Impôts'
            return 'Société & Quotidien', tag
        return 'Questions Entretien', 'Entretien'

    start_id = len(flashcards) + 1
    for i, (q, a) in enumerate(rows):
        cat, tag = extract_tag_and_category(q, a)
        card_id = f'fc-{start_id + i}'
        tip = "Question fréquente lors de l'entretien de naturalisation."
        if cat == 'Questions Entretien':
            tip = "Exprimez-vous avec clarté, sincérité et en démontrant votre attachement aux valeurs françaises."
        elif cat == 'Symboles & Valeurs':
            tip = "Connaissez la définition exacte inscrite dans la Constitution de 1958."
        elif cat == 'Principes Républicains':
            tip = "La laïcité et l'égalité femmes-hommes sont particulièrement testées lors de l'entretien."
        elif cat == 'Institutions':
            tip = "Maîtrisez la séparation des pouvoirs (exécutif, législatif, judiciaire)."
        elif cat == 'Histoire':
            tip = "Retenez les dates repères et les figures historiques majeures."
        elif cat == 'Géographie':
            tip = "Sachez situer les fleuves majeurs, les pays frontaliers et votre propre région."
        elif cat == 'Culture & Sciences':
            tip = "Citez au moins 2 à 3 personnalités célèbres dans ce domaine."
        elif cat == 'Société & Quotidien':
            tip = "Montrez votre bonne insertion sociale, professionnelle et civique."
        flashcards.append({
            'id': card_id,
            'category': cat,
            'tag': tag,
            'front': clean_html(q),
            'back': clean_html(a),
            'tip': tip
        })

categories = sorted(list(set(fc["category"] for fc in flashcards)))

flashcards_data = {
    "version": "2026.2",
    "totalCards": len(flashcards),
    "categories": categories,
    "cards": flashcards
}

with open('data/flashcards.json', 'w', encoding='utf-8') as f:
    json.dump(flashcards_data, f, ensure_ascii=False, indent=2)

if os.path.exists('dist/data'):
    with open('dist/data/flashcards.json', 'w', encoding='utf-8') as f:
        json.dump(output_data if 'output_data' in locals() else flashcards_data, f, ensure_ascii=False, indent=2)

print(f'Generated data/flashcards.json with {len(flashcards)} flashcards across {len(categories)} categories.')
