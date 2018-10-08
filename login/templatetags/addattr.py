"""
From https://gist.github.com/TimFletcher/034e799c19eb763fa859
Related post: http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/
Django template filter to add attributes to form fields
"""

from django import template
register = template.Library()

@register.filter(name='addattr')
def addattr(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            t, v = d.split(':')
            attrs[t] = v

    return field.as_widget(attrs=attrs)
