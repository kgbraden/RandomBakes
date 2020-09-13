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
import pandas as pd

def importSales():
    gc = pygsheets.authorize(service_file='creds.json')

    sh = gc.open('Bagel Order Form')
    wks = sh.sheet1
    df = wks.get_as_df()

    df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
    df=df[df['Submission Date'] !=""]
    print(len(df))
    # df.set_index(['Invoice ID'])

    df.to_csv('orders.csv', index=False)


def ReturnTicket(invoice, df2):

    order = df2.loc[(df2['Invoice ID']==invoice), 'My Products: Products'].values[0]
    deliveree = df2.loc[(df2['Invoice ID']==invoice), 'My Products: Payer Address'].values[0]
    deliveree = deliveree.replace('\r', "")
    order = order.replace('  ', ' ')
    order = order.replace('\r', '')
    order = order.split('\n')
    toDel = []
    for part in range(len(order)):
        order[part] = "{'" + order[part]
        order[part] = order[part].replace(": ", "': '")
        order[part] = order[part].replace(" (", "': {'")
        order[part] = order[part].replace(", ", "', '")
        order[part] = order[part].replace(")", "'}}")

        if 'Total' in order[part]:
            order[part] = order[part] + "'}"
        if ("Subtotal" in order[part]) | ("Tax" in order[part]) | (order[part] =="{'"):
            toDel.append(order[part])
        else:
            order[part] = ast.literal_eval(order[part])
    for z in toDel:
        order.remove(z)
    ticket = 'Invoice: %s\n%s\n' %(invoice,deliveree)
    for b in range(1,5):
        b_info = order[0]['Bagel Four Pack']['Bagel '+str(b)]
        ticket += 'Bagel %s: %s\n' %(str(b), b_info)
    noCheese = True
    noRandom = True
    amt = 0
    RndAmt = 0
    for item in range(1, len(order)):

        if "Cream Cheese" in order[item]:
            noCheese = False
            amt = int(order[item]['Cream Cheese']['Quantity'])
            if amt >1:
                ticket += 'Cream Cheese: %s tubs\n' %(amt)
            else:
                ticket += 'Cream Cheese: 1 tub\n'
        if "Bagel Four Pack 2" in order[item]:
            for b in range(5,9):
                b_info = order[item]['Bagel Four Pack 2']['Bagel '+str(b)]
                ticket += 'Bagel %s: %s\n' %(str(b), b_info)
        if "Random Bake" in order[item]:
            noRandom = False
            RndAmt = int(order[item]['Random Bake']['Quantity'])
            if RndAmt >1:
                ticket += 'Random Bake: %s orders\n' %(RndAmt)
            else:
                ticket += 'Random Bake: 1 order\n'
    if noCheese:
        ticket += "No Cream Cheese"
    if noRandom:
        ticket += "No Random Bake"
    ticket = ticket.replace("Country: United States\n", "")
    ticket = ticket.replace("/Postal", "")
    ticket = ticket.replace("/Region", "")
    inventory = {'plain': ticket.count("Plain"),
                 'sesame': ticket.count("Sesame"),
                 'salt': ticket.count("Salt"),
                 'garlic': ticket.count("Garlic"),
                 'onion': ticket.count("Onion"),
                 'everything': ticket.count("Everything"),
                 'creamcheese': amt,
                 'randombake': RndAmt}
    return ticket, inventory

def WeeksSales(batch, df):
    subdf = df.loc[df["Batch ID"]==batch, "Invoice ID"].values
    inventory = {'plain': 0,
                 'sesame': 0,
                 'salt':0,
                 'garlic':0,
                 'onion':0,
                 'everything': 0,
                 'creamcheese': 0,
                 'randombake': 0,
                 'totBagels': 0}
    tickets = []
    for orders in subdf:
        print('#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#')
        rtrn = ReturnTicket(orders,df)
        tickets.append(rtrn[0].split('\n'))
        invt = rtrn[1]
        for cat in inventory:
            if cat != 'totBagels':
                inventory[cat] +=invt[cat]
                inventory['totBagels'] +=invt[cat]
    return tickets, inventory

df2 = pd.read_csv('orders.csv')

invoice = '# INV-X0NY64'
invoice = '# INV-N34Z2Q'
batch = "BATCH_21"
# print (ReturnTicket(invoice,df2)[1])
# importSales()

print(WeeksSales(batch, df2)[1])
