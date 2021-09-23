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

La solution ultime pour imprimer un pdf avec selenium :
```python
pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
```
