#%%

# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import json

with open(r'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\fiches_json_lyon_202109222333.txt', 'r', encoding='utf-8') as f:
    json_views = f.readlines()

for view in json_views:

    v = json.loads(view)

    loader = FileSystemLoader('templates')
    env = Environment(loader=loader)
    template = env.get_template('index_tpl.html')

    result = template.render(v=v)

    with open(rf'rendered\fiche_{v["depcom"]}_{v["EquipementId"]}.html', 'wb') as index:
        index.write(result.encode('utf-8'))

# %%
