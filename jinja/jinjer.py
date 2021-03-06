#%%

# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
from selenium import webdriver
import json
import base64
import time

def my_finalize(thing):
    return thing if thing is not None else 'NC'

# jinja settings
loader = FileSystemLoader(r'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\jinja\templates')
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
    'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5000)

# get views
with open(r'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\fiches_json_metro_part1_202111261640.txt', 'r', encoding='utf-8') as f:
    json_views = f.readlines()

# loop on views
for view in json_views:

    # render json view
    v = json.loads(view)
    template = env.get_template('index_tpl.html')
    result = template.render(v=v)

    html_path = rf'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\jinja\rendered\fiche_{v["depcom"]}_{v["N° équipement"]}.html'
    pdf_path = rf'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\jinja\pdf\fiche_{v["depcom"]}_{v["N° équipement"]}.pdf'
    # write rendered html
    with open(html_path, 'wb') as index:
        index.write(result.encode('utf-8'))

    # export pdf
    driver.get(html_path)
    time.sleep(5)
    # driver.execute_script('window.print();')
    pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
    with open(pdf_path, "wb") as f:
        f.write(base64.b64decode(pdf['data']))
        
    # log on console
    print(v["N° équipement"] + ' done')

driver.quit()
# %%
