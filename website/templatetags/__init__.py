from django import template

register = template.Library()


@register.simple_tag
def company_name():
    return "Kalsi Global Links"


@register.simple_tag
def company_email():
    return "info@kalsiglobal.com"


@register.simple_tag
def company_phone():
    return "+54 9 249 467336"


@register.simple_tag
def current_year():
    return 2023