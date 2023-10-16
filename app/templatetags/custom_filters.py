from django import template

register = template.Library()

@register.filter(name='date_format')
def date_format(value):
    return value.strftime('%d-%m-%Y') if value else ''