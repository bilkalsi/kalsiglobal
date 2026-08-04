from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def current_year():
    return datetime.now().year


@register.filter
def company(value):
    return f"{value} | Kalsi Global Links"