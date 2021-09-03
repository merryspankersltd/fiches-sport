#%%
from selenium import webdriver
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
driver.get("https://merryspankersltd.github.io/fiches-sport/")

#%%
# todo: option to print with background ?
driver.execute_script('window.print();')
driver.implicitly_wait(5)

#%%
driver.quit()