# fiches sport

Un projet de templates html à exporter en pdf

### template html

Utilisation de pages.js dans les css pour assurer une impression fidèle à la mise en page.

https://www.pagedjs.org/

### population des templates par des vues json

Utilisation de jinja2:
- template minilanguage pour transformer la maquette html en template
- jinja pour exporter les pages html

https://jinja.palletsprojects.com

### impression des pages html en pdf avec le webdriver chrome et selenium

https://www.selenium.dev/

https://chromedriver.chromium.org

A noter:
- les versions de chrome et de chromedriver.exe doivent correspondre. Chromedriver.exe doit être accessible dans le PATH (emplacement classique: `C:\Program Files (x86)\chromedriver\chromedriver.exe`)
- le dossier template est référencé par jinja dans l'option `loader = FileSystemLoader('path\to\templates')`. Ensuite, le template html est simplement appelé par son nom de fichier dans `template = env.get_template('index_tpl.html')`

La solution ultime pour imprimer un pdf avec selenium :
```python
import base64

# ...insert selenium init code here...

driver.get(html_path)
time.sleep(5) # chromedrive needs some time to fully load html

pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})

with open(pdf_path, "wb") as f:
    f.write(base64.b64decode(pdf['data']))
```
https://github.com/merryspankersltd/fiches-sport/blob/52978fa0de4308a21bf75e70dd2cd84f68aa9b11/jinja/jinjer.py
