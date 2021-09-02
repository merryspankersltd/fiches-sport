from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('templates')

env = Environment(loader=loader)

template = env.get_template('index.tpl')

result = template.render(some_json)

with open(r'rendered\index_rendered.html', 'w') as index:
    index.write(result)