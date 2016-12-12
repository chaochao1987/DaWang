from django import template
t = template.Template('My name is {{name}}')
c = template.context({{'name': 'Adrian'}})
print t.render(c)
