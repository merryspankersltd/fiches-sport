#%%

# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
from selenium import webdriver
import json

def my_finalize(thing):
    return thing if thing is not None else 'NC'

# jinja settings
loader = FileSystemLoader('templates')
env = Environment(loader=loader, finalize=my_finalize)

# selenium settings
chrome_options = webdriver.ChromeOptions()
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False,
        "isCssBackgroundEnabled": True}
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': r'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\jinja\pdf'}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

# get views
with open(r'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\fiches_json_rhone_202109230112.txt', 'r', encoding='utf-8') as f:
    json_views = f.readlines()

# loop on views
for view in json_views[:100]:

    # render json view
    v = json.loads(view)
    template = env.get_template('index_tpl.html')
    result = template.render(v=v)

    # write rendered html
    with open(rf'rendered\fiche_{v["depcom"]}_{v["EquipementId"]}.html', 'wb') as index:
        index.write(result.encode('utf-8'))

    # export pdf
    driver.get(rf'rendered\fiche_{v["depcom"]}_{v["EquipementId"]}.html')
    driver.execute_script('window.print();')
    driver.implicitly_wait(5)
    
    # log on console
    print(v["EquipementId"] + ' done')

driver.quit()
# %%
