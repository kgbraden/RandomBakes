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
django.setup()
from MainPage.models import (ActiveSales, Customer, Orders)
from django.db.models import Avg, Max, Min, Sum
import math
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
def ProcessSales():
    products =  {'Plain_sold':0,'Sesame_sold':0, 'Salt_sold':0, 'Onion_sold':0,
                'Poppy_sold':0,'Garlic_sold':0, 'Everything_sold':0,
                'RandomBake_sold':0, 'CreamCheese_sold':0}
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
        if (product !='RandomBake_sold') & (product != 'CreamCheese_sold'):
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
    if totalSold >= invt.units:
        invt.soldout = True
    invt.save()
    return products
if __name__ == '__main__':
    rslt = ProcessSales()
    