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

@register.filter(name='DeliveryInfo')
def DeliveryInfo(value):
    delivery = value.replace('\n', '|').split('|')
    length = len(delivery)
    x = 0
    deliv = ''
    for d in delivery:
        if (not 'None' in d) & (d!="") & (x !=length):
            deliv +=d + '\n'
        elif x==length:
            deliv +=d
        x+=1
    return deliv

@register.filter(name='TicClean')
def TicketClean(value):
    items = value.replace(" (",",").replace(')', ',').replace('Additional Bagel Pack', '').replace("Bagel ", "B").replace(', ', ',').replace('Cream Cheese', 'Cream Cheese: ').split(',')
    ticket =''
    for item in items:
        if not ('Amount'in item) | ('Four' in item):
            if ('B1' in item) | ('B3' in item) | ('B5' in item) | ('B7' in item):
                ticket += item + " | "
            elif ('B2' in item) | ('B4' in item) | ('B6' in item) | ('B8' in item) | ('Quantity' in item):
                ticket += item + "\n"
            else:
                ticket += item
    return ticket
@register.filter(name='phone_nmbr')
def PhoneNumber(value):
    delivery = value.replace('\n', '|').split('|')
    phone = delivery[3].replace(" ", "")
    if phone[:1] !='1':
        phone = '1'+phone
    return phone
@register.filter(name='gMap')
def gMap(value):
    delivery = value.replace('\n', '|').split('|')
    length = len(delivery)
    x = 1
    deliv = ''
    for d in delivery:
        if (not 'Notes' in d) & (d!="") & (x !=length-1):
            deliv +=d + '+'
        print (deliv)
        x+=1
    urlEncodings = {" ": '%20',
                    '"': '%22',
                    '<': '%3C', 
                    '>': '%3E',
                    '#': '%23', 
                    '%': '%25',
                    '|': ' 	%7C'}
    for urlc in urlEncodings:
        deliv.replace(urlc, urlEncodings[urlc])
    map = 'https://www.google.com/maps/search/?api=1&query='+ deliv
    directions = 'https://www.google.com/maps/dir/?api=1&destination='+ deliv+"&travelmode=driving"
    return directions