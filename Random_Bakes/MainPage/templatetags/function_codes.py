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
def route(value):
    invt = ActiveSales.objects.get(active ="True")
    orders = Orders.objects.filter(batch=value).order_by('delivorder')
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