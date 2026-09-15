# -*- coding: utf-8 -*-
"""All the text and photos of the site. Edit this file, then run: python3 build.py"""

SITE = {
    "name": "Danse la Source",
    "tagline_fr": "Gîte de charme en Allier",
    "tagline_en": "A charming holiday cottage in the Allier",
    "phone_display": "+33 (0)6 84 22 92 38",
    "phone_tel": "+33684229238",
    "email": "mireille.jouanaud@gmail.com",
    "hosts": "Mireille et Etienne",
    "address": ["230 Rte de Floret", "03220 Trézelles", "France"],
    # The pin Mireille placed by hand on the old site. Geocoding the street
    # address lands ~175 m away on the road centroid, so keep this one.
    "lat": 46.3256272,
    "lng": 3.5850295,
    # Apex is canonical; GitHub Pages redirects www here automatically.
    "domain": "https://danselasource.fr",
}

# Booking pages on the Gîtes de France network. Checked and working on 2026-09-14.
BOOKING_FR = "https://www.gites-de-france-allier.com/location-vacances-Gite-Trezelles-03G4901.html"
BOOKING_EN = "https://www.gites-de-france.com/en/auvergne-rhone-alpes/allier/danse-la-source-03g4901"

HERO = "gite-facade"

# (file, caption fr, caption en)
GALLERY_HOUSE = [
    ("gite-entree-cour", "Entrée du gîte depuis la cour", "The cottage entrance from the courtyard"),
    ("gite-maison-vue-du-pre", "La maison vue du pré", "The house seen from the meadow"),
    ("gite-grande-table", "La grande table", "The long dining table"),
    ("gite-salle-a-manger", "Salle à manger", "Dining room"),
    ("gite-cuisine", "La cuisine", "The kitchen"),
    ("gite-salon-cheminee", "Le salon et sa cheminée", "The living room and its fireplace"),
    ("gite-mini-cinema", "Le mini-cinéma", "The mini-cinema"),
    ("gite-bibliotheque", "La bibliothèque", "The library"),
    ("gite-petit-salon", "Petit salon", "Small sitting room"),
    ("gite-chambre-ciels-de-lit", "Chambre aux ciels de lit", "Bedroom with canopied beds"),
    ("gite-chambre-maison-de-poupee", "Chambre et sa maison de poupée", "Bedroom with its doll's house"),
    ("gite-chambre-coquelicots", "Les Coquelicots", "Les Coquelicots"),
    ("gite-chambre-wagon-lit", "Le Wagon-lit", "Le Wagon-lit"),
    ("gite-chambre-village-vry-1", "Le village Vry", "Le village Vry"),
    ("gite-chambre-village-vry-2", "Le village Vry", "Le village Vry"),
    ("gite-chambre-tante-simone", "Chez Tante Simone", "Chez Tante Simone"),
    ("gite-nurserie", "La nurserie", "The nursery"),
    ("gite-salle-d-eau-1", "Salle d'eau", "Shower room"),
    ("gite-salle-d-eau-2", "Salle d'eau", "Shower room"),
    ("gite-salle-d-eau-3", "Salle d'eau", "Shower room"),
    ("gite-coursive", "Vue de la coursive", "View from the walkway"),
    ("gite-terrasse-glycine", "La terrasse sous la glycine", "The terrace under the wisteria"),
    ("gite-jardin", "Au jardin", "In the garden"),
    ("gite-terrain-de-boules", "Le terrain de boules", "The pétanque court"),

    # Added September 2026. The older outdoor photos above are due to be
    # replaced once Marion's new set arrives.
    ("gite-cuisine-ete", "La cuisine d'été", "The summer kitchen"),
    ("gite-coin-ombrage", "Le coin ombragé", "The shaded corner"),
    ("gite-escalier-fontaine", "L'escalier et la fontaine", "The steps and the fountain"),
    ("gite-transats-verger", "Les transats sous les arbres", "Loungers under the trees"),
    ("gite-balancoire-nid", "La balançoire nid", "The nest swing"),
    ("gite-piscine-a-balles", "La piscine à balles", "The ball pit"),
]

# The grid crops to 4:3; these portrait photos keep their subject low in the
# frame, so a centred crop would cut it off. Values are CSS object-position.
PHOTO_FOCUS = {
    "gite-cuisine-ete":      "center 72%",
    "gite-balancoire-nid":   "center 70%",
    "gite-transats-verger":  "center 66%",
    "gite-piscine-a-balles": "center 64%",
    "gite-escalier-fontaine": "center 56%",
}

GALLERY_STUDIO = [
    ("studio-lit", "Le lit du Studio", "The Studio's bed"),
    ("studio-chambre", "Le Studio", "The Studio"),
    ("studio-salle-d-eau", "La salle d'eau du Studio", "The Studio's shower room"),
]

# --- Home / welcome -------------------------------------------------------

HOME = {
    "fr": {
        "title": "Bienvenue",
        "meta": "Gîte de charme dans une maison bourbonnaise du 18e siècle, à Trézelles dans "
                "l'Allier. 14 personnes, à 20 min du PAL et de Vichy.",
        "h1": "Une maison bourbonnaise du 18<sup>e</sup> siècle",
        "lede": "Tout au long de l'année, Mireille et Etienne vous accueillent dans une ancienne "
                "maison bourbonnaise du 18<sup>e</sup> siècle, aménagée en gîte de 14 places.",
        "body": [
            "Décorée avec soin, confortable et accueillante, la demeure se situe dans le hameau "
            "de Floret, sur la commune de Trézelles (au bord de la départementale 480, entre "
            "Lapalisse et Jaligny-sur-Besbre) dans l'Allier (Auvergne).",
            "Le gîte accueille 14 personnes, réparties sur 6 chambres.",
        ],
        "cta": "Découvrir le gîte",
        "cta_href": "/fr/le-gite",
        "facts_title": "En bref",
        "facts": [
            ("14", "personnes"),
            ("6", "chambres"),
            ("3 épis", "Gîtes de France"),
            ("170 m²", "de maison"),
        ],
        "access_title": "Venir chez nous",
        "access": "Le gîte se situe à environ 2 heures au nord-ouest de Lyon. Rejoindre Lapalisse "
                  "par la nationale 7, puis suivre la D480 sur 12 km en direction du parc "
                  "d'attraction Le PAL.",
        "map_link": "Voir sur la carte",
    },
    "en": {
        "title": "Welcome",
        "meta": "A charming 18th-century house in the Allier, France, sleeping 14. "
                "20 minutes from Le PAL theme park and Vichy.",
        "h1": "An 18<sup>th</sup>-century Bourbonnais house",
        "lede": "Throughout the year, Mireille and Etienne welcome you to an old 18<sup>th</sup>-century "
                "Bourbonnais house, converted into a cottage sleeping 14.",
        "body": [
            "Decorated with care, comfortable and welcoming, the house stands in the hamlet of "
            "Floret, in the commune of Trézelles (on the D480 road, between Lapalisse and "
            "Jaligny-sur-Besbre) in the Allier, Auvergne.",
            "The cottage sleeps 14, across 6 bedrooms.",
        ],
        "cta": "Discover the cottage",
        "cta_href": "/en/cottage",
        "facts_title": "At a glance",
        "facts": [
            ("14", "guests"),
            ("6", "bedrooms"),
            ("3 épis", "Gîtes de France"),
            ("170 m²", "of house"),
        ],
        "access_title": "Getting here",
        "access": "The cottage is about 2 hours north-west of Lyon. Take the N7 to Lapalisse, then "
                  "follow the D480 for 12 km towards the Le PAL theme park.",
        "map_link": "See it on the map",
    },
}

# --- The cottage ----------------------------------------------------------

COTTAGE = {
    "fr": {
        "title": "Le gîte",
        "meta": "Le gîte de Danse la Source : 170 m², 14 places en 6 chambres, salon avec "
                "mini-cinéma et poêle à bois, grand jardin clos.",
        "h1": "Le gîte",
        "lede": "Situé au cœur de l'Allier, anciennement nommé pays du Bourbonnais, le gîte de "
                "Danse la Source (3 épis) vous accueille tout au long de l'année. Ancien centre "
                "de stage pour jeunes danseurs, le gîte possède une superficie de près de 170 m² "
                "et accueille 14 personnes.",
        "spec_title": "La maison",
        "specs": [
            ("14 places réparties sur 6 chambres", [
                "2 chambres avec lit double",
                "1 chambre avec 2 lits simples côte à côte",
                "1 chambre avec 2 lits superposés",
                "1 chambre avec 1 lit double et 2 lits superposés",
                "le Studio, en rez-de-chaussée (voir plus bas)",
            ]),
            ("4 salles d'eau dans la maison", [
                "au rez-de-chaussée : 1 salle d'eau avec WC",
                "à l'étage : 1 salle d'eau avec WC et 2 salles d'eau sans WC",
            ]),
            ("1 WC indépendant à l'étage", []),
            ("Salle à manger — cuisine", []),
            ("Salon avec mini-cinéma, bibliothèque et poêle à bois", []),
            ("Nurserie", []),
        ],
        "comfort_title": "Confort",
        # Ordered by what guests actually ask about; the old site led with
        # double-glazing and buried the air conditioning at the end.
        "comfort": ["Climatisation", "Chauffage", "Internet", "TV", "Lave-linge",
                    "Lave-vaisselle", "Réfrigérateur", "Micro-ondes", "Double-vitrage"],
        "garden_title": "Le jardin",
        "garden": "Derrière la maison se trouve un grand jardin entouré d'arbres, fermé par une "
                  "clôture de pré (attention aux chiens fugueurs). Vous y trouverez des "
                  "balançoires, un terrain de pétanque, un barbecue, des tables et chaises de "
                  "jardin, une table de ping-pong, un babyfoot, un filet de volley, un jeu d'eau "
                  "et des éclairages d'été. Un cadre idéal en famille ou entre amis.",
        "gallery_title": "En images",
        "studio_h": "Le Studio",
        "studio_body": "La sixième chambre se trouve en rez-de-chaussée : le Studio, aménagé dans "
                       "un ancien atelier, offre une ambiance de petit village avec son décor de "
                       "tuiles et sa hauteur sous toit conservée. Il est compris dans la location "
                       "du gîte.",
        "studio_specs": [
            "Une chambre (2 lits simples côte à côte ou 1 lit double)",
            "Douche et lavabo dans une alcôve de la chambre",
            "WC indépendant, derrière sa porte",
            "TV, internet",
        ],
        "book_title": "Réserver",
        "book": 'Pour plus d\'information et pour réserver, rendez-vous sur <a href="{booking}">'
                'notre page des Gîtes de France</a>, ou contactez Mireille au '
                '<a href="tel:{tel}">{phone}</a>.',
    },
    "en": {
        "title": "The cottage",
        "meta": "The Danse la Source cottage: 170 m², sleeps 14 in 6 bedrooms, living room with "
                "mini-cinema and wood stove, large enclosed garden.",
        "h1": "The cottage",
        "lede": "In the heart of the Allier — historically the Bourbonnais country — the Danse la "
                "Source cottage (rated 3 épis) welcomes you all year round. A former training "
                "centre for young dancers, the house offers nearly 170 m² and sleeps 14.",
        "spec_title": "The house",
        "specs": [
            ("Sleeps 14 across 6 bedrooms", [
                "2 bedrooms with a double bed",
                "1 bedroom with 2 single beds side by side",
                "1 bedroom with 2 bunk beds",
                "1 bedroom with 1 double bed and 2 bunk beds",
                "the Studio, on the ground floor (see below)",
            ]),
            ("4 shower rooms in the house", [
                "ground floor: 1 shower room with WC",
                "upstairs: 1 shower room with WC and 2 shower rooms without",
            ]),
            ("1 separate WC upstairs", []),
            ("Dining room — kitchen", []),
            ("Living room with mini-cinema, library and wood-burning stove", []),
            ("Nursery", []),
        ],
        "comfort_title": "Comfort",
        "comfort": ["Air conditioning", "Heating", "Internet", "TV", "Washing machine",
                    "Dishwasher", "Fridge", "Microwave", "Double glazing"],
        "garden_title": "The garden",
        "garden": "Behind the house lies a large garden ringed by trees and closed off by a "
                  "pasture fence (mind escape-artist dogs). You will find swings, a pétanque "
                  "court, a barbecue, garden tables and chairs, a ping-pong table, table "
                  "football, a volleyball net, a water game and summer lighting. An ideal "
                  "setting for family or friends.",
        "gallery_title": "In pictures",
        "studio_h": "The Studio",
        "studio_body": "The sixth bedroom is on the ground floor: the Studio, converted from a "
                       "former workshop, with the feel of a little village thanks to its tiled "
                       "decor and its preserved height under the roof. It is included when you "
                       "book the cottage.",
        "studio_specs": [
            "One bedroom (2 single beds side by side, or 1 double bed)",
            "Shower and basin in an alcove off the bedroom",
            "Separate WC, behind its own door",
            "TV, internet",
        ],
        "book_title": "Booking",
        "book": 'For more information and to book, visit <a href="{booking}">our Gîtes de France '
                'page</a>, or contact Mireille on <a href="tel:{tel}">{phone}</a> (in French).',
    },
}

# --- Things to do ---------------------------------------------------------

ATTRACTIONS_INTRO = {
    "fr": {
        "title": "Loisirs",
        "meta": "Une sélection d'activités et de loisirs autour du gîte : Le PAL, Vulcania, "
                "le château de La Palice, la Montagne bourbonnaise, Vichy.",
        "h1": "Loisirs à proximité",
        "lede": 'Vous trouverez ci-dessous une sélection d\'activités et loisirs à proximité. '
                'Pour découvrir d\'autres options, n\'hésitez pas à demander à votre hôte '
                'Mireille, ou à visiter les sites '
                '<a href="https://www.allier-auvergne-tourisme.com/">Allier Auvergne '
                'Tourisme</a> et <a href="https://www.auvergnerhonealpes-tourisme.com/">'
                'Auvergne-Rhône-Alpes Tourisme</a>.',
    },
    "en": {
        "title": "Nearby attractions",
        "meta": "A selection of things to do around the cottage: Le PAL, Vulcania, the castle of "
                "La Palice, the Montagne bourbonnaise, Vichy.",
        "h1": "Nearby attractions",
        "lede": 'Here is a selection of nearby activities. To discover other options do not '
                'hesitate to ask your host Mireille, or to visit '
                '<a href="https://www.auvergnerhonealpes-tourisme.com/en/">Auvergne-Rhône-Alpes '
                'Tourism</a> and <a href="https://www.allier-auvergne-tourisme.com/">Allier '
                'Tourism</a> (in French).',
    },
}

# Photos that carry a licence requiring credit. Keyed by image filename; the
# credit is rendered at the foot of whichever page uses the photo.
# CC BY-SA obliges us to name the author, state the licence and link both.
PHOTO_CREDITS = {}

CREDITS_LABEL = {"fr": "Crédits photo", "en": "Photo credits"}

# (image, time, fr: (name, url, text), en: (name, url, text))
ATTRACTIONS = [
    ("le-pal", "20 min",
     ("Le PAL", "https://www.lepal.com/",
      "Le PAL (Parc Animalier et de Loisirs) s'étend sur 23 hectares, dont 17 pour le parc "
      "zoologique. Il propose plus de 25 attractions et près de 500 animaux en semi-liberté, "
      "ainsi que plusieurs spectacles animaliers (otaries, rapaces, perroquets)."),
     ("Le PAL", "https://en.lepal.com/",
      "Le PAL covers 23 hectares, including 17 for the zoo. It offers more than 25 attractions "
      "and nearly 500 animals in semi-freedom, as well as several animal shows (sea lions, "
      "raptors, parrots).")),

    ("chateau-de-lapalisse", "15 min",
     ("Château de La Palice",
      "https://www.allier-auvergne-tourisme.com/chateau-de-la-palice-PCUAUV000FS001SA-695-1.html",
      "Jadis résidence de « Monsieur de La Palice », ce château des XII<sup>e</sup>, "
      "XV<sup>e</sup> et XVI<sup>e</sup> siècles est habité par la 30<sup>e</sup> génération de "
      "la même famille. Il présente de nombreux souvenirs historiques et des plafonds à caissons "
      "Renaissance italienne uniques en Europe."),
     ("Castle of La Palice",
      "https://www.allier-auvergne-tourisme.com/chateau-de-la-palice-PCUAUV000FS001SA-695-1.html",
      "Former residence of \"Monsieur de La Palice\", this castle of the 12th, 15th and 16th "
      "centuries is inhabited by the 30th generation of the same family. It holds many historical "
      "mementoes and Italian Renaissance coffered ceilings unique in Europe.")),

    ("plan-deau-de-saint-clement", "40 min",
     ("Plan d'eau de Saint-Clément",
      "https://www.allier-auvergne-tourisme.com/activites/parcs-et-bases-de-loisirs/base-de-loisirs-saint-clement-6622-1.html",
      "Tables de pique-nique, locations de canoë, paddle et pédalos, un parc accrobranche et ses "
      "tyroliennes, des circuits de randonnée, des parcours d'orientation, un sentier découverte, "
      "des zones de pêche, une aire de jeux : il y en a pour tous les goûts, pour les grands "
      "comme pour les petits."),
     ("Lake Saint-Clément",
      "https://www.allier-auvergne-tourisme.com/activites/parcs-et-bases-de-loisirs/base-de-loisirs-saint-clement-6622-1.html",
      "Picnic tables, canoe, paddleboard and pedalo hire, a treetop adventure park with zip "
      "lines, hiking trails, orienteering courses, a discovery trail, fishing areas and a "
      "playground: there is something for everyone, young and old.")),

    ("chatel-montagne", "30 min",
     ("Église Notre-Dame de Châtel-Montagne",
      "https://www.allier-auvergne-tourisme.com/monument-historique-classe/site-clunisien/roman/chatel-montagne/eglise-notre-dame/4685146",
      "Superbe exemple de roman auvergnat, cette église présente une nef et des bas-côtés étroits "
      "du début du XII<sup>e</sup> siècle, tandis que son déambulatoire, ses chapelles rayonnantes "
      "et son porche à deux étages datent de la fin du même siècle. Elle possède également des "
      "chapiteaux originaux et des traces de peinture murale dans la tribune, datés des "
      "XII<sup>e</sup> et XIII<sup>e</sup> siècles. Son clocher carré à deux étages est du début "
      "du XIII<sup>e</sup> siècle."),
     ("Church of Notre-Dame de Châtel-Montagne",
      "https://www.allier-auvergne-tourisme.com/monument-historique-classe/site-clunisien/roman/chatel-montagne/eglise-notre-dame/4685146",
      "Built between 1100 and 1250, Notre-Dame de Châtel-Montagne is Romanesque architecture at "
      "its artistic and technical peak. Its unique style — a mixture of Auvergne and Burgundy — "
      "and its position in neither region, isolated and hard to reach, mean that no school claims "
      "it and that it remains too little known for its interest.")),

    ("piscine-varennes", "15 min",
     ("Piscine communautaire à Varennes-sur-Allier",
      "https://www.allier-auvergne-tourisme.com/piscine-communautaire-LOIAUV000FS000CP-612-1.html",
      "Dans le cadre verdoyant du parc du Valençon, le site compte des bassins ludiques avec jets "
      "d'eau, des toboggans et un « poisson arroseur » pour les plus petits, des bassins "
      "découverts chauffés et accessibles aux personnes à mobilité réduite, une buvette, un "
      "terrain de volley-ball, une pelouse ombragée et une plage de repos."),
     ("Community pool in Varennes-sur-Allier",
      "https://www.allier-auvergne-tourisme.com/piscine-communautaire-LOIAUV000FS000CP-612-1.html",
      "Set in the green surroundings of the Valençon park, the site has fun pools with water "
      "jets, slides and a \"sprinkler fish\" for little ones, heated open-air pools accessible to "
      "people with reduced mobility, a bar, a volleyball court, a shaded lawn and a rest area.")),

    ("vulcania", "1 h 30",
     ("Vulcania", "https://www.vulcania.com/",
      "Découvrez l'histoire, la beauté et la force des volcans d'Auvergne grâce au musée et au "
      "parc d'attraction Vulcania, situé à 950 m d'altitude sur 57 hectares, avec plus de 30 "
      "animations et projections."),
     ("Vulcania", "https://www.vulcania.com/en/",
      "Discover the history, beauty and strength of the Auvergne volcanoes at the Vulcania museum "
      "and theme park, at 950 m above sea level and across 57 hectares, with more than 30 shows "
      "and screenings.")),

    ("ponton-tourbiere", "50 min",
     ("Les tourbières de Saint-Nicolas-des-Biefs",
      "https://www.allier-auvergne-tourisme.com/equipement/saint-nicolas-des-biefs/sentier-de-decouverte-amenage/4839957",
      "Un milieu naturel à part entière, dont la flore sauvage se cache dans ce marécage de 20 "
      "hectares. C'est un lieu qui résulte de l'accumulation de nombreuses espèces végétales "
      "depuis plusieurs millénaires. Un sentier de découverte et un ponton de bois permettent de "
      "le parcourir."),
     ("The peat bogs of Saint-Nicolas-des-Biefs",
      "https://www.allier-auvergne-tourisme.com/equipement/saint-nicolas-des-biefs/sentier-de-decouverte-amenage/4839957",
      "A natural environment in its own right, its wild flora hidden in this 20-hectare marsh. It "
      "is a place formed by the accumulation of many plant species over several millennia. A "
      "discovery trail and a wooden boardwalk let you cross it.")),

    ("cascade-pisserotte", "35 min",
     ("Cascade de la Pisserotte à Arfeuilles",
      "https://www.allier-auvergne-tourisme.com/equipement/arfeuilles/autour-de-la-cascade-de-la-pisserotte/4889168",
      "« La Pisserotte » est un opéra sauvage d'éléments naturels : eaux vives, blocs rocheux, "
      "ensemble de cascades (dont la plus haute fait environ 4 mètres), gours et marmites. Un "
      "endroit idéal pour une randonnée suivie d'une baignade."),
     ("Cascade of the Pisserotte in Arfeuilles",
      "https://www.allier-auvergne-tourisme.com/equipement/arfeuilles/autour-de-la-cascade-de-la-pisserotte/4889168",
      "\"La Pisserotte\" is a wild opera of natural elements: white water, boulders and a set of "
      "waterfalls, the highest about 4 metres. An ideal place for a hike followed by a swim.")),

    ("vichy-les-thermes", "30 min",
     ("Thermes de Vichy", "https://vichymonamour.fr/",
      "À Vichy, les curistes ont le choix entre les Thermes Callou (standard) et les Thermes des "
      "Dômes (confort), tous deux situés à proximité des berges de l'Allier, pour effectuer leur "
      "cure thermale."),
     ("Vichy thermal baths", "https://vichymonamour.com/",
      "In Vichy, spa guests have the choice between the Thermes Callou (standard) and the Thermes "
      "des Dômes (comfort), both near the banks of the Allier, for their water cure.")),
]

# --- Chrome ---------------------------------------------------------------

NAV = {
    "fr": [("/", "Bienvenue"), ("/fr/le-gite", "Le gîte"), ("/fr/loisirs", "Loisirs")],
    "en": [("/en/", "Welcome"), ("/en/cottage", "The cottage"), ("/en/nearby-attractions", "Nearby")],
}

UI = {
    "fr": {
        "lang_other": "English", "lang_other_code": "en",
        "call": "Appeler", "email": "Écrire", "menu": "Menu",
        "footer_contact": "Nous contacter", "footer_where": "Où nous trouver",
        "footer_book": "Réserver",
        "footer_book_text": "Réservation et disponibilités sur Gîtes de France",
        "directions": "Itinéraire",
        "rights": "Tous droits réservés",
        "close": "Fermer", "prev": "Précédent", "next": "Suivant",
        "skip": "Aller au contenu",
    },
    "en": {
        "lang_other": "Français", "lang_other_code": "fr",
        "call": "Call", "email": "Email", "menu": "Menu",
        "footer_contact": "Contact us", "footer_where": "Where we are",
        "footer_book": "Book",
        "footer_book_text": "Availability and booking on Gîtes de France",
        "directions": "Directions",
        "rights": "All rights reserved",
        "close": "Close", "prev": "Previous", "next": "Next",
        "skip": "Skip to content",
    },
}

# Which page in the other language each page maps to, for the language switch.
ALTERNATES = {
    "/": "/en/",
    "/en/": "/",
    "/fr/le-gite": "/en/cottage",
    "/en/cottage": "/fr/le-gite",
    "/fr/loisirs": "/en/nearby-attractions",
    "/en/nearby-attractions": "/fr/loisirs",
}
