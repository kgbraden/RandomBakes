from django import template

register = template.Library()

@register.filter(name = 'chk_invt')
def chk_invt(value):
    """
    This function needs to be built to check the inventory available.
    """
    return (7)
@register.filter(name = 'TextManip')
def TextManip(value, arg):
    return value.replace(arg, 'Turnip')
