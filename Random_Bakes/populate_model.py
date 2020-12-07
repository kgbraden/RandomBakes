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
from MainPage.models import highlight, Orders, Customer, ActiveSales, Subscription

def add_highlight(cT, cTXT, cP, caTXT, cB, cBL):
    u = highlight.objects.get_or_create(title = cT,
                                        story = cTXT,
                                        photo = cP,
                                        photo_alt = caTXT,
                                        button = cB,
                                        button_link = cBL)[0]
    u.save()
    print("Success!")
# add_highlight("Order Bagels",
#        "We produce 48 kettle-boiled, hand-rolled bagels every other week and deliver them to the Sacramento region on Sunday mornings. Sold in batches of four with the option of adding cream cheese to your order. You choose the toppings. Once we're sold out, that's it for the week!",
#        'static\MainApp\Media\Bagels-two.jpg',
#        'Two Bagelss',
#        'Order Now',
#        '\order_bagels'
# )
def dupOrder(cust_email, old_batch, new_Batch, invoice_id):
    Cust = Customer.objects.get(email=cust_email)
    bat = ActiveSales.objects.get(batch = old_batch)
    new_bat = ActiveSales.objects.get(batch = new_Batch)
    order = Orders.objects.get(customer=Cust, batch= bat)
    o = Orders.objects.get_or_create(
                                    invoiceid = invoice_id,
                                    batch = new_bat,
                                    customer = Cust,
                                    Plain_sold = order.Plain_sold,
                                    Sesame_sold = order.Sesame_sold,
                                    Salt_sold = order.Salt_sold,
                                    Onion_sold = order.Onion_sold,
                                    Poppy_sold = order.Poppy_sold,
                                    Garlic_sold = order.Garlic_sold,
                                    Everything_sold = order.Everything_sold,
                                    RandomBake_sold = order.RandomBake_sold,
                                    CreamCheese_sold = order.CreamCheese_sold,
                                    deliveryinfo = order.deliveryinfo,
                                    cart = order.cart
    )
    try:
        o.save()
    except:
        print("already saved!")

bat = ActiveSales.objects.filter().order_by('-id')[0]
print(bat.batch)