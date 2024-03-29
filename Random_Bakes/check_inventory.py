# -*- coding: utf-8 -*-
"""
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
#                                 \\|||||//                                  #
#                                 (  o o  )                                  #
#                ------------Ooo-----(_)--------------------                 #
#                |                                         |                 #
#                |       Programmed by: Kale Braden        |                 #
#                |                Date: 09/11/2020         |                 #
#                |                                         |                 #
#                ------------------------------ooO----------                 #
#                                |___| |___|                                 #
#                                 | |   | |                                  #
#                                 ooO   Ooo                                  #
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
"""
import pygsheets, ast
from pathlib import Path
import os
import pandas as pd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Random_Bakes.settings")
import django
#django.setup()
from MainPage.models import (ActiveSales, Customer, Orders)
from django.db.models import Avg, Max, Min, Sum
import math
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
def ProcessSales():
    products =  {'Plain_sold':0,'Sesame_sold':0, 'Salt_sold':0, 'Onion_sold':0,
                'Poppy_sold':0,'Garlic_sold':0, 'Everything_sold':0,
                'RandomBake_sold':0, 'CreamCheese_sold':0, 'Dog_sold': 0, 
                'EvMix_sold':0, 'AButter_sold':0}
    try:
        invt = ActiveSales.objects.get(active ="True")
    except:
        print("No ActiveSales")
        products['totBagels']= 0
        return products
    totalSold = 0
    for product in products:
        unitsSold = Orders.objects.filter(batch=invt.id).aggregate(sum = Sum(product))['sum']
        if unitsSold is None:
            unitsSold = 0 
        products[product] = unitsSold
        if (
            (product !='RandomBake_sold') & 
            (product != 'CreamCheese_sold') &
            (product != 'Dog_sold') &
            (product != 'EvMix_sold') &
            (product != 'AButter_sold')
            ):
            totalSold += unitsSold
            
    products['totBagels']= totalSold
    invt.Plain_sold = products['Plain_sold']
    invt.Sesame_sold = products['Sesame_sold']
    invt.Salt_sold = products['Salt_sold']
    invt.Garlic_sold = products['Garlic_sold']
    invt.Onion_sold = products['Onion_sold']
    invt.Poppy_sold = products['Poppy_sold']
    invt.Everything_sold = products['Everything_sold']
    invt.RandomBake_sold = products['RandomBake_sold']
    invt.CreamCheese_sold = products['CreamCheese_sold']
    invt.Dog_sold = products['Dog_sold']
    invt.EvMix_sold = products['EvMix_sold']
    invt.AButter_sold = products['AButter_sold']
    if totalSold >= invt.units:
        invt.soldout = True
    invt.save()
    return products

def route(value):
    invt = ActiveSales.objects.get(active ="True")
    orders = Orders.objects.filter(batch=value)
    deliv = ''
    #rte = "https://www.google.com/maps/dir/"
    rte = ''
    for order in orders:
        v = order.deliveryinfo
        delivery =v.replace(" ", "+")
        delivery = delivery.replace('\n', '|').split('|')
        #print(delivery)
        length = len(delivery)
        x = 1
        for d in delivery:
            d = d.replace('\r', '')
            if (not 'Notes' in d) & (d!="") & (x !=length-1):
                deliv +="%s+" %d
                #print(deliv)
            #print (deliv)
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
        rte += "%s/" % deliv 
        deliv = ''
    
    #print("https://www.google.com/maps/dir/%s" %rte)    
    return "https://www.google.com/maps/dir/%s" %rte
#print(route(10))
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
# def importSales():
#     path = Path(__file__).resolve(strict=True).parent
#     path = os.path.join(path, 'creds.json')
#     gc = pygsheets.authorize(service_file=path)
#
#     sh = gc.open('Bagel Order Form')
#     wks = sh.sheet1
#     df = wks.get_as_df()
#
#     df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
#     df=df[df['Submission Date'] !=""]
#
#     # df.set_index(['Invoice ID'])
#
#     df.to_csv('orders.csv', index=False)
#     return(df)

# def ReturnTicket(invoice, df2):
#
#     order = df2.loc[(df2['Invoice ID']==invoice), 'My Products: Products'].values[0]
#
#     fname =  df2.loc[(df2['Invoice ID']==invoice), 'First Name'].values[0]
#     lname = df2.loc[(df2['Invoice ID']==invoice), 'Last Name'].values[0]
#     straddress = df2.loc[(df2['Invoice ID']==invoice), 'Street Address'].values[0]
#     straddress2 =  df2.loc[(df2['Invoice ID']==invoice), 'Street Address Line 2'].values[0]
#     if not type(straddress2) is str: straddress2 = ' '
#     city = df2.loc[(df2['Invoice ID']==invoice), 'City'].values[0]
#     state = df2.loc[(df2['Invoice ID']==invoice), 'State / Province'].values[0]
#     zip = df2.loc[(df2['Invoice ID']==invoice), 'Postal / Zip Code'].values[0]
#     if type(zip) is float: zip = int(zip)
#     email = df2.loc[(df2['Invoice ID']==invoice), 'Email'].values[0]
#     phone = df2.loc[(df2['Invoice ID']==invoice), 'Phone Number'].values[0]
#     notes = df2.loc[(df2['Invoice ID']==invoice), 'Delivery notes:'].values[0]
#     if not type(notes) is str: notes = 'None.'
#     customer = {
#                 'First Name': fname,
#                 'Last Name': lname,
#                 'Street Address': straddress,
#                 'Street Address 2': straddress2,
#                 'City': city,
#                 'State': state,
#                 'Zip': zip,
#                 'Email': email,
#                 'Phone Number': phone,
#                 'Delivery Notes': notes,
#                 }
#     customer_clean = {k: customer[k] for k in customer if type(k) is str}
#
#     # deliveree = [df2.loc[(df2['Invoice ID']==invoice), 'My Products: Payer Address'].values[0]]
#     # deliveree = deliveree.replace('\r', "")
#     order = order.replace('  ', ' ')
#     order = order.replace('\r', '')
#     order = order.split('\n')
#     toDel = []
#     for part in range(len(order)):
#         order[part] = "{'" + order[part]
#         order[part] = order[part].replace(": ", "': '")
#         order[part] = order[part].replace(" (", "': {'")
#         order[part] = order[part].replace(", ", "', '")
#         order[part] = order[part].replace(")", "'}}")
#         order[part] = order[part].replace("_ORDER", "_ORDER'}")
#
#         if 'Total' in order[part]:
#             order[part] = order[part] + "'}"
#         if ("Subtotal" in order[part]) | ("Tax" in order[part]) | (order[part] =="{'") :
#             toDel.append(order[part])
#         else:
#             order[part] = ast.literal_eval(order[part])
#     ticket = ""
#     for z in toDel:
#         order.remove(z)
#     # ticket = 'Invoice: %s\n%s\n' %(invoice,customer)
#     for b in range(1,5):
#         b_info = order[0]['Bagel Four Pack']['Bagel '+str(b)]
#         ticket += 'Bagel %s: %s\n' %(str(b), b_info)
#     noCheese = True
#     noRandom = True
#     amt = 0
#     RndAmt = 0
#
#     for item in range(1, len(order)):
#
#         if "Cream Cheese" in order[item]:
#             noCheese = False
#             amt = int(order[item]['Cream Cheese']['Quantity'])
#             if amt >1:
#                 ticket += 'Cream Cheese: %s tubs\n' %(amt)
#             else:
#                 ticket += 'Cream Cheese: 1 tub\n'
#         if "Bagel Four Pack 2" in order[item]:
#             for b in range(5,9):
#                 b_info = order[item]['Bagel Four Pack 2']['Bagel '+str(b)]
#                 ticket += 'Bagel %s: %s\n' %(str(b), b_info)
#         if "Random Bake" in order[item]:
#             noRandom = False
#             RndAmt = int(order[item]['Random Bake']['Quantity'])
#             if RndAmt >1:
#                 ticket += 'Random Bake: %s orders\n' %(RndAmt)
#             else:
#                 ticket += 'Random Bake: 1 order\n'
#     if noCheese:
#         ticket += "No Cream Cheese"
#     if noRandom:
#         ticket += "No Random Bake"
#
#     inventory = {'plain': ticket.count("Plain"),
#                  'sesame': ticket.count("Sesame"),
#                  'salt': ticket.count("Salt"),
#                  'garlic': ticket.count("Garlic"),
#                  'onion': ticket.count("Onion"),
#                  'poppy': ticket.count("Poppy"),
#                  'everything': ticket.count("Everything"),
#                  'creamcheese': amt,
#                  'randombake': RndAmt}
#
#     ticket = {'Customer Info':customer_clean, 'Order': ticket.split('\n')}
#     return ticket, inventory

# def WeeksSales(batch, df):
#     subdf = df.loc[df["Batch ID"]==batch, "Invoice ID"].values
#     inventory = {'plain': 0,
#                  'sesame': 0,
#                  'salt':0,
#                  'garlic':0,
#                  'onion':0,
#                  'poppy':0,
#                  'everything': 0,
#                  'creamcheese': 0,
#                  'randombake': 0,
#                  'totBagels': 0}
#
#     tickets = {}
#     for orders in subdf:
#         rtrn = ReturnTicket(orders,df)
#
#         tickets[orders] =rtrn[0]
#         invt = rtrn[1]
#         for cat in inventory:
#             if cat != 'totBagels':
#                 inventory[cat] +=invt[cat]
#                 inventory['totBagels'] +=invt[cat]
#     invt = ActiveSales.objects.get(active ="True")
#     invt.Plain_sold = inventory['plain']
#     invt.Sesame_sold = inventory['sesame']
#     invt.Salt_sold = inventory['salt']
#     invt.Garlic_sold = inventory['garlic']
#     invt.Onion_sold = inventory['onion']
#     invt.Poppy_sold = inventory['poppy']
#     invt.Everything_sold = inventory['everything']
#     invt.RandomBake_sold = inventory['randombake']
#     invt.CreamCheese_sold = inventory['creamcheese']
#     if inventory['totBagels'] >= invt.units:
#         invt.soldout = 'True'
#     invt.save()
#     return tickets, inventory

#df2 = pd.read_csv('orders.csv')
#
# # invoice = '# INV-X0NY64'
# invoice = '# INV-GGLOW6'
# # batch = "BATCH_21"
#importSales()
#print (WeeksSales('BATCH_22',df2)[1])

# print(ProcessSales('BATCH_27'))
# print(WeeksSales("BATCH_27", df2)[1])
