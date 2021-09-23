#%%
from selenium import webdriver
import base64
import json

#source: https://stackoverflow.com/questions/56897041/how-to-save-opened-page-as-pdf-in-selenium-python

#chromedriver must be installed and in the PATH
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
        "isCssBackgroundEnabled": True
    }

prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument("--headless")

#%%
# todo: run the following headless
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

#%%
driver.get(r'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\jinja\rendered\fiche_69096_E001I690960002.html')

#%%
# todo: option to print with background ?
#driver.execute_script('window.print();')
pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
driver.implicitly_wait(5)
with open(r'C:\Users\marcl\Documents\pro\fiches_sport_github\fiches-sport\jinja\pdf\selenium_test.pdf', "wb") as f:
  f.write(base64.b64decode(pdf['data']))
#%%
driver.quit()
# %%
