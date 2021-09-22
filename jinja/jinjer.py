#%%
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
#%%
v = {
  "EquipementId": "E004I384570001",
  "depcode": "38",
  "depcom": "38457",
  "coordx": 5.26674,
  "coordy": 45.32896,
  "installation": {
    "n° installation": "n° I384570001",
    "nom": "Ensemble Sportif",
    "adresse": "rue du stade Le Pré Neuf 38870 Saint-Siméon-de-Bressieux",
    "installation particulière": "Complexe sportif",
    "multicommune": "non",
    "hébergement": "non",
    "nb lits": 0,
    "nb places de parking": "50",
    "dont handicapé": 1,
    "emprise foncière": "52215 m²",
    "desserte": ""
  },
  "équipement": {
    "administration": {
      "propriétaire principal": "Commune",
      "gestionnaire principal": "Commune",
      "propriétaire secondaire": None,
      "gestionnaire secondaire": None,
      "gestion DSP": "non"
    },
    "mise en service": {
      "année de mise en service": None,
      "tranche d'année de service": "Avant 1945",
      "places en tribune": 0
    },
    "ERP": {
      "catégorie ERP": 3
    },
    "présence de": {
      "vestaire/douche": "non",
      "éclairage": "oui"
    },
    "fiche technique": {
      "nature du sol": "Béton",
      "nature de l'équipement": "Intérieur",
      "hauteur de l'aire d'évolution": 7,
      "longueur de l'aire d'évolution": 40,
      "largeur de l'aire d'évolution": 18,
      "aire de la surface d'évolution": 720,
      "nombre de vestiaires sportifs": 0,
      "sanitaires": "oui",
      "nombre de couloirs/pistes": None,
      "vestiaires chauffés": "non",
      "nombre de vestiaires arbitres": 0
    },
    "usages": {
      "types d'utilisateurs": "utilisation scolaire, utilisation clubs, autres",
      "types d'usages": "performance, formation, récréation"
    },
    "travaux": {
      "derniers travaux: tranche de dates": None,
      "date des derniers travaux": None,
      "motif des derniers travaux": ""
    },
    "accès handicapé": {
      "accès handicap mobile à l'aire d'activité": "Oui",
      "accès handicap mobile aux tribunes": "Non concerné",
      "accès handicap mobile aux vestiaires": "Non concerné",
      "accès handicap mobile aux sanitaires": "Oui",
      "accès handicap sensoriel à l'aire d'activité": "Non",
      "accès handicap sensoriel aux tribunes": "Non concerné",
      "accès handicap sensoriel aux vestiaires": "Non concerné",
      "accès handicap sensoriel aux sanitaires": "Oui"
    },
    "locaux complémentaires": {
      "locaux complémentaires": "accueil réception"
    },
    "chauffage/source d'énergie": {
      "type de chauffage": "aucun"
    },
    "aménagements de confort": {
      "aménagements de confort": "aucun"
    },
    "SAE (structure artificielle d'escalade": {
      "nombre de couloirs": None,
      "hauteur du mur": None,
      "surface du mur": None
    },
    "accès à l'équipement": {
      "signalétique de sécurité": "non",
      "moyens d'alerte": "non",
      "accès public": "",
      "accès secours": ""
    },
    "locaux": {
      "démarche HQE": "non",
      "locaux techniques": "non",
      "locaux pédagogiques": "non",
      "PDESI/PDIPR": "non"
    },
    "piscine": {
      "forme du bassin": None,
      "longueur du bassin": None,
      "largeur du bassin": None,
      "surface du bassin": None,
      "profondeur minimale du bassin": None,
      "profondeur maximale du bassin": None,
      "nombre de couloirs": None,
      "surface des plages": None,
      "nombre total de tremplins": None,
      "nombre de tremplins de 1 m": None,
      "nombre de tremplins de 3 m": None,
      "nombre total de plateformes": None,
      "nombre de plateformes de 3 m": None,
      "nombre de plateformes de 5 m": None,
      "nombre de plateformes de 7 m": None,
      "nombre de plateformes de 10 m": None,
      "présence d'une pataugeoire": "non",
      "types d'aménagements complémentaires": ""
    },
    "athlétisme": {
      "développement de la piste": None,
      "longueur de la ligne droite": None,
      "nombre de couloirs en ligne droite": None,
      "nombre de couloirs en virage": None,
      "rivière de steeple": "non",
      "nombre total d'aires de saut": None,
      "nombre d'aires de saut en hauteur": None,
      "nombre d'aires de saut en lonhueur": None,
      "nombre d'aires de triple saut": None,
      "nombre d'aires de saut à la perche": None,
      "nombre total d'aires de lancer": None,
      "nombre d'aires de lancer de poids": None,
      "nombre d'aires de lancer de disque": None,
      "nombre d'aires de lancer de javelot": None,
      "nombre d'aires de lancer de marteau": None,
      "nombre d'aires de lancer mixte": None
    },
    "tir": {
      "type de pas de tir": ""
    },
    "équipements de nature": {
      "tour d'arrivée": "non",
      "treuil": "non"
    }
  },
  "activités": {
    "nombre d'activités": 4,
    "liste des activités": [
      {
        "index": 190333,
        "ActLib": "Handball / Mini hand / Handball de plage",
        "ComLib": "Saint-Siméon-de-Bressieux",
        "DepLib": "Isère",
        "ActCode": 3701,
        "DepCode": "38",
        "ComInsee": "38457",
        "ActNivLib": "Scolaire",
        "EquipementId": "E004I384570001",
        "ActDiscipline": "Handball",
        "EquActivitePratique": 1,
        "EquActiviteSalleSpe": 0,
        "EquActivitePraticable": 1
      },
      {
        "index": 190332,
        "ActLib": "Football / Football en salle (Futsal)",
        "ComLib": "Saint-Siméon-de-Bressieux",
        "DepLib": "Isère",
        "ActCode": 2901,
        "DepCode": "38",
        "ComInsee": "38457",
        "ActNivLib": "Entrainement",
        "EquipementId": "E004I384570001",
        "ActDiscipline": "Football",
        "EquActivitePratique": 1,
        "EquActiviteSalleSpe": 0,
        "EquActivitePraticable": 1
      },
      {
        "index": 190335,
        "ActLib": "Tennis",
        "ComLib": "Saint-Siméon-de-Bressieux",
        "DepLib": "Isère",
        "ActCode": 7901,
        "DepCode": "38",
        "ComInsee": "38457",
        "ActNivLib": "Entrainement",
        "EquipementId": "E004I384570001",
        "ActDiscipline": "Tennis",
        "EquActivitePratique": 1,
        "EquActiviteSalleSpe": 0,
        "EquActivitePraticable": 1
      },
      {
        "index": 190334,
        "ActLib": "Escalade",
        "ComLib": "Saint-Siméon-de-Bressieux",
        "DepLib": "Isère",
        "ActCode": 4802,
        "DepCode": "38",
        "ComInsee": "38457",
        "ActNivLib": "Loisir - Entretien - Remise en forme",
        "EquipementId": "E004I384570001",
        "ActDiscipline": "Montagne et escalade",
        "EquActivitePratique": 1,
        "EquActiviteSalleSpe": 0,
        "EquActivitePraticable": 1
      }
    ]
  }
}
#%%
loader = FileSystemLoader('templates')
env = Environment(loader=loader)
print(env.list_templates())
#%%
template = env.get_template('index_tpl.html')
#%%
result = template.render(json_view)
#%%
with open(r'rendered\index_rendered.html', 'wb') as index:
    index.write(result.encode('utf-8'))

# %%
