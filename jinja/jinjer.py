#%%
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
#%%
json_view = {
    'ref': 391,
    'depcom': '69046',
    'eq_name': 'Charly'
}
#%%
loader = FileSystemLoader('templates')
env = Environment(loader=loader)
print(env.list_templates())
#%%
template = env.get_template('index.html')
#%%
result = template.render(json_view)
#%%
with open(r'rendered\index_rendered.html', 'wb') as index:
    index.write(result.encode('utf-8'))

# %%
