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
import os, time, schedule
from datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Random_Bakes.settings")
import django
django.setup()
from MainPage.models import (ActiveSales, Customer, Orders)
from django.db.models import Avg, Max, Min, Sum
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
def ProcessSales():
    if datetime.now().weekday()==0: #0 is the wekday code for Mondays. This'll only check inventory on Mondays
       #print("checking inventory")
        products =  {'Plain_sold':0,'Sesame_sold':0, 'Salt_sold':0, 'Onion_sold':0,
                    'Poppy_sold':0,'Garlic_sold':0, 'Everything_sold':0,
                    'RandomBake_sold':0, 'CreamCheese_sold':0}
        invt = ActiveSales.objects.get(active ="True")
        totalSold = 0
        for product in products:
            unitsSold = Orders.objects.filter(batch=invt.id).aggregate(sum = Sum(product))['sum']
            if unitsSold is None:
                unitsSold = 0 
            products[product] = unitsSold
            if (product !='RandomBake_sold') & (product != 'CreamCheese_sold'):
                totalSold += unitsSold
                
        if totalSold >= invt.units:
            invt.soldout = True
        invt.save()
        return totalSold
    else:
        #print ("Not in day range, not checking")
        return 0
if __name__ == '__main__':
    schedule.every(1).minutes.do(ProcessSales)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    