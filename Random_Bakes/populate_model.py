# -*- coding: utf-8 -*-
"""
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
#                                 \\|||||//                                  #
#                                 (  o o  )                                  #
#                ------------Ooo-----(_)--------------------                 #
#                |                                         |                 #
#                |       Programmed by: Kale Braden        |                 #
#                |                Date: 08/31/2020         |                 #
#                |                                         |                 #
#                ------------------------------ooO----------                 #
#                                |___| |___|                                 #
#                                 | |   | |                                  #
#                                 ooO   Ooo                                  #
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Random_Bakes.settings')

import django
django.setup()

##Fake Pop Script
from MainPage.models import highlight

def add_highlight(cT, cTXT, cP, caTXT, cB, cBL):
    u = highlight.objects.get_or_create(title = cT,
                                        story = cTXT,
                                        photo = cP,
                                        photo_alt = caTXT,
                                        button = cB,
                                        button_link = cBL)[0]
    u.save()
    print("Success!")
add_highlight("Order Bagels",
       "We produce 48 kettle-boiled, hand-rolled bagels every other week and deliver them to the Sacramento region on Sunday mornings. Sold in batches of four with the option of adding cream cheese to your order. You choose the toppings. Once we're sold out, that's it for the week!",
       'static\MainApp\Media\Bagels-two.jpg',
       'Two Bagelss',
       'Order Now',
       '\order_bagels'
)
