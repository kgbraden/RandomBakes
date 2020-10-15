from django import template
import ast
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

@register.simple_tag(name='DeliveryInfo')
def DeliveryInfo(value):
    try:
        items = ast.literal_eval(value)
    except:
            return value
    ticket = "<table><tr>"
    for item in items:
        item = item.replace(' (', ', ')
        item = item.replace(': ', ', ')
        item = item.replace(')','')
        item = item.split(', ')
        x = 0
        for part in item:
            x +=1
            if x ==1:
                ticket += '<th>' + part + '</th></tr><tr>'
            elif (not 'Amount' in part) & (not 'USD' in part) & ('Bagel' not in part):
                ticket += '<td>'+ part + '</td>'
        ticket += '</tr>'
    ticket += '</table>'
    return ticket
