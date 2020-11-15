from django.shortcuts import render, get_object_or_404, redirect
from MainPage.models import (highlight,
                             ActiveSales,
                             Featurette,
                             Orders,
                             Customer)
from django.utils import timezone
from MainPage.forms import (UserForm,
                            UserProfileInfoForm,
                            ActiveSalesForm,
                            FeaturetteForm)
from check_inventory import ProcessSales
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (View,
                                  TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
from django.db.models.functions import Now
from config import sendtext
import ast, re
from django.core.mail import send_mail
import secret_key

# Create your views here.
@require_http_methods(["GET", "POST"])
def orderplaced(request):
    print(request.GET.get('id', None))
    print("Worked")
    return HttpResponse("Order Placed!")

def index(request):
    B_info = BatchInfo()
    today = date.today()
    cover_content2 = highlight.objects.filter(title = "Order Bagels")[0]
    feat = Featurette.objects.filter(type = 'index').order_by("order")
    sold = ProcessSales()
    totsold = sold['totBagels']
    story = cover_content2.story
    story = story.replace('[[units]]', str(B_info[0]))
    if B_info[1]: #this indicates that the batch is sold out
        buttonText = "Sold Out!"
        buttonLink = "#" #Eventially take to batch info for previous batch.
    elif not B_info[2]:
        buttonText = "Sales Not Open Yet"
        buttonLink = "#"
    else:
        buttonText = cover_content2.button
        buttonLink = cover_content2.button_link
    cover_content ={'CoverTitle': cover_content2.title,
           'CoverText': story,
           'CoverPhoto': cover_content2.photo2.url,
           'CoverAltText': cover_content2.photo_alt,
           'CoverButton': buttonText,
           'CoverButtonLink': buttonLink,
           'CoverButtonClass': cover_content2.button_class,
           'CoverScript': cover_content2.script,
           'Featurette': feat,
           'TotalSold': totsold}
    return render(request,'MainPage/index.html', context = cover_content)

  
def projects(request):
    return render(request,'MainPage/projects.html')

class AboutUsListView(ListView):
    template_name = 'MainPage/blank_content.html'
    queryset = Featurette.objects.filter(type='About Us')
    context_object_name = 'articles'
    ordering = ['order']

class SanitationListView(ListView):
    template_name = 'MainPage/blank_content.html'
    queryset = Featurette.objects.filter(type = 'Sanitation Protocols')
    context_object_name = 'articles'
    ordering = ['order']

class LicenseListView(ListView):
    template_name = 'MainPage/blank_content.html'
    queryset = Featurette.objects.filter(type='Licenses')
    context_object_name = 'articles'
    ordering = ['order']
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
class ProjectListView(ListView):
    template_name = 'MainPage/blank_content.html'
    queryset = Featurette.objects.filter(type='Projects')
    context_object_name = 'articles'
    ordering = ['order']

class FeaturetteListView(ListView):
    model = Featurette

class ActiveSalesListView(ListView):
    model = ActiveSales
    template_name = 'MainPage/batches.html'
    queryset = ActiveSales.objects.all()
    context_object_name = 'batches'
    ordering = ['-end_sales']

# class TicketListView(ListView):
#     template_name = 'MainPage/tickets.html'
#     acv_sales = ActiveSales.objects.get(active = "True")
#     queryset = Orders.objects.filter(batch = acv_sales.id)
#     context_object_name = 'tickets'
#     ordering= ['customer']

def TicketListView(request):
    batches = ActiveSales.objects.all().order_by("-batch")
    if request.GET.get('batch'):
        acv_sales = ActiveSales.objects.get(batch = request.GET.get('batch'))
    else:
        acv_sales = ActiveSales.objects.get(active = "True")    
    tickets = Orders.objects.filter(batch = acv_sales.id).order_by('customer')
    # ordered = []
    # if tickets.Plain_sold > 0:
    #     ordered.append('Plain: %s' % tickets.Plain_sold)
    # if ticket.Sesame_sold > 0:
    #     ordered.append('Sesame: %s' % ticket.Sesame_sold)            
    # if ticket.Salt_sold > 0:
    #     ordered.append('Salt: %s' % ticket.Salt_sold)
    # if ticket.Onion_sold > 0:
    #     ordered.append('Onion: %s' % ticket.Onion_sold)
    # if ticket.Poppy_sold > 0:
    #     ordered.append('Poppy: %s' % ticket.Poppy_sold)
    # if ticket.Garlic_sold > 0:
    #     ordered.append('Garlic: %s' % ticket.Garlic_sold)
    # if ticket.Everything_sold > 0:
    #     ordered.append('Every: %s' % ticket.Everything_sold)
    # if ticket.RandomBake_sold > 0:
    #     ordered.append('R_Bake: %s' % ticket.RandomBake_sold)
    # if ticket.CreamCheese_sold > 0:
    #     ordered.append('C_Cheese: %s' % ticket.CreamCheese_sold)              
    return render(request,'MainPage/tickets.html', {'tickets': tickets, 
                                                    'batches': batches,
                                                    
                                                     })
    

class OrdersListView(ListView):
    
    model = Orders
    ordering= ['-batch']

#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
class FeaturetteDetailView(DetailView):
    model = Featurette

def send_text(request):
    if request.method =="POST":
        OrdId = request.POST['OrderID']
        phone = request.POST['phone']
        #deliverorder = request.POST['deliverorder']
        text = "Your Bagel order is at your front door! Thank you and enjoy! (This is an automated text!)"
        now = Now()
        # send_mail('test', 'body of the message', 'info@RandomBakes.com', ['kale@ebraden.com'])
        if len(phone)==11:
            status = sendtext(phone, text)
        else:
            status = "Number not correct length, text not sent. "
        # try:
        #     subj = "%s Order placed!" %NewOrder.batch
        #     msg = "HUZZAH! %s %s has ordered %s" % {DjangoCustomer.Fname, DjangoCustomer.Lname, NewOrder.cart}
        #     send_mail('Order Placed', 'body of the message', 'info@RandomBakes.com', [config.KB, config.TT])
        # except:
        #     print("Email Didn't work")
        try:
            status += "%s Delivery recorded" %(OrdId)
            OrderTracing = Orders.objects.get(id=OrdId)
            OrderTracing.delivered = now
            OrderTracing.delivery_notes = status
            OrderTracing.delivery_completed ==True
            OrderTracing.save()
            
        except:
            status += "Delivery Not recorded"
    
        
    return redirect("../orders/")

class DeliveryView(ListView):
    acv_sales = ActiveSales.objects.get(active = "True")    
    queryset = Orders.objects.filter(batch = acv_sales.id).order_by('delivorder')
    template_name = "MainPage/orders_list.html"
class OrdersDetailView(DetailView):
    # slug_field='Customer.Lname'
    # slug_url_kwarg='batch'
    # send_mail('test', 'body of the message', 'info@RandomBakes.com', ['kale@ebraden.com'])
    model = Orders

class ActiveSalesDetailView(DetailView):
    model = ActiveSales
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
class FeaturetteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    # redirect_field_name = '/MainPage/featurette_update'
    success_url = '/Baking/success/'
    form_class = FeaturetteForm
    model = Featurette

class ActiveSalesCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    # redirect_field_name = '/MainPage/featurette_update'
    success_url = '/Baking/success/'
    form_class = ActiveSalesForm
    model = ActiveSales
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
class FeaturetteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    # redirect_field_name = '#'
    success_url = '/Baking/success/'
    form_class = FeaturetteForm
    model = Featurette

class ActiveSalesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    # redirect_field_name = '#'
    template_name = 'MainPage/ActiveSales_update.html'
    success_url = '/Baking/success/'
    form_class = ActiveSalesForm
    model = ActiveSales

#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
class FeaturetteDeleteView(LoginRequiredMixin, DeleteView):
    success_url = '/Baking/success/'
    model = Featurette

class ActiveSalesDeleteView(LoginRequiredMixin, DeleteView):
    success_url = '/Baking/success/'
    model = ActiveSales
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
def contact(request):
    return render(request,'MainPage/contact.html')

def license(request):
    return render(request,'MainPage/license.html')

class SanitationView(TemplateView):
    template_name = 'MainPage/sanitation.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_injection']= 'This is only a test'
        return context
# def sanitation(request):
#     return render(request,'MainPage/sanitation.html')

def next_batch(batch):
    b = batch.split("_")
    b[1] = str(int(b[1])+1)
    sep = "_"
    return sep.join(b)

def BatchInfo():
    acv_sales = ActiveSales.objects.filter(active ="True")[0]
    today = date.today()
    activeBatch = acv_sales.batch
    nextbatch = next_batch(activeBatch)
    DeliveryInfo = ""
    available = acv_sales.units
    if (acv_sales.soldout == "True"):
        DeliveryInfo = "We're sorry, %s is sold out. We are producing %s bagels to be delivered on %s." %(activeBatch, available, deliverydate)
        out = True
    else:
        out = False
    sales_open = False
    if (acv_sales.start_sales <= today) & (today <= acv_sales.end_sales):
        # In sales period
        sales_open = True
        deliverydate = acv_sales.deliverydate.strftime('%A, %B %e, %Y')
        storedate = acv_sales.start_sales.strftime('%A, %B %e, %Y')
        deliverytime = acv_sales.bakingtime.strftime('%I:%M %p')
        # sales = importSales()
        sold = ProcessSales()
        totsold = sold['totBagels']
        DeliveryInfo = "%s is scheduled to be baked and delivered on %s. Deliveries will begin after %s when the bagels have cooled enough for packaging. We anticipate deliveries to be completed by 12:00 noon. We will deliver within 10 miles of Tahoe Park and provide contact-less delivery." %(acv_sales.batch, deliverydate, deliverytime)
        # out = False
        batch = '<ul class="lead text-justify">'
        if acv_sales.Plain_sold>0: batch += '<li>%s Plain Bagels</li>' % (acv_sales.Plain_sold)
        if acv_sales.Sesame_sold>0: batch += '<li>%s Sesame Bagels</li>' %(acv_sales.Sesame_sold)
        if acv_sales.Salt_sold>0: batch += '<li>%s Salt Bagels</li>' %(acv_sales.Salt_sold)
        if acv_sales.Garlic_sold>0: batch += '<li>%s Garlic Bagels</li>' %(acv_sales.Garlic_sold)
        if acv_sales.Onion_sold>0: batch += '<li>%s Onion Bagels</li>' %(acv_sales.Onion_sold)
        if acv_sales.Poppy_sold>0: batch += '<li>%s Poppy Seed Bagels</li>' %(acv_sales.Poppy_sold)
        if acv_sales.Everything_sold>0: batch += '<li>%s Everything Bagels</li>' %(acv_sales.Everything_sold)
        if acv_sales.RandomBake_sold>0: batch += '<li>%s RandomBakes</li>' %(acv_sales.RandomBake_sold)
        if acv_sales.CreamCheese_sold>0: batch += '<li>%s Tubs of Cream Cheese</li>' %(acv_sales.CreamCheese_sold)
        batch += '</ul>'
        
        DeliveryInfo += ' For this batch we are scheduled to produce:' + batch
        
    else:
        if ActiveSales.objects.filter(batch =nextbatch).count()==1:
            #Checks to see if the next batch has been scheduled
            nBatch = ActiveSales.objects.get(batch =nextbatch)
            nxtdateopen =  nBatch.start_sales.strftime('%A, %B %e, %Y')
            nxtdatedelivery = nBatch.deliverydate.strftime('%A, %B %e, %Y')
            DeliveryInfo = "Our next scheduled production run, %s, of %s bagels, will be on %s. Sales will open for this batch on %s." %(nextbatch, nBatch.units,  nxtdatedelivery, nxtdateopen)
        else:
            DeliveryInfo = "We have not scheduled our next scheduled production run. Please check back soon!"
    feature = Featurette.objects.get(title ='Current Batch')
    feature.description = DeliveryInfo
    feature.save()
    return available, out, sales_open

def order(request):
    acv_sales = ActiveSales.objects.filter(active =True)[0]
    today = date.today()
    deliverydate = acv_sales.deliverydate.strftime('%A, %B %e, %Y')
    storedate = acv_sales.start_sales.strftime('%A, %B %e, %Y')
    deliverytime = acv_sales.bakingtime.strftime('%I:%M %p')
    activeBatch = acv_sales.batch
    nextbatch = next_batch(activeBatch)
    if ActiveSales.objects.filter(batch =nextbatch).count()==1:
        #Checks to see if the next batch has been scheduled
        nBatch = ActiveSales.objects.get(batch =nextbatch)
        NxtSched = True
        nxtdateopen =  nBatch.start_sales.strftime('%A, %B %e, %Y')
        nxtdatedelivery = nBatch.deliverydate.strftime('%A, %B %e, %Y')
    else:
        NxtSched = False
    if (acv_sales.start_sales < today) & (today < acv_sales.end_sales):
        # In sales period

        sold = ProcessSales()
        totsold = sold['totBagels']
        if acv_sales.RandomBake:
            DeliveryInfo = "<h3>This week's Random Bake!</h3>" + acv_sales.RandomBake + "<br>"
            DeliveryInfo += "<h3>Delivery Info</h3>%s is scheduled to be baked and delivered on %s. Deliveries will begin after %s when the bagels have cooled enough for packaging. We anticipate deliveries to be completed by 12:00 noon. We will deliver within 10 miles of Tahoe Park and provide contact-less delivery." %(acv_sales.batch, deliverydate, deliverytime)
        else:
            DeliveryInfo = "%s is scheduled to be baked and delivered on %s. Deliveries will begin after %s when the bagels have cooled enough for packaging. We anticipate deliveries to be completed by 12:00 noon. We will deliver within 10 miles of Tahoe Park and provide contact-less delivery." %(acv_sales.batch, deliverydate, deliverytime)
        available = acv_sales.units
        if acv_sales.soldout =='True':
            cover_content2 = highlight.objects.filter(title = "Sold Out!")[0]
        else:
            cover_content2 = highlight.objects.filter(title = "Buy Now")[0]
    else:
        sold = 'N/A'
        available = 'N/A'
        cover_content2 = highlight.objects.filter(title = "Sales Closed")[0]
        if NxtSched:
            DeliveryInfo = "Our next scheduled production run, %s, will be on %s. Sales open for this batch will open on %s." %(nextbatch, nxtdatedelivery, nxtdateopen)
        else:
            DeliveryInfo = "We have not scheduled our next scheduled production run. Please check back soon!"
    ##{'plain': 7, 'sesame': 10, 'salt': 4, 'garlic': 5, 'onion': 4, 'everything': 6, 'creamcheese': 6, 'randombake': 0, 'totBagels': 42}

    cover_content ={'CoverTitle': cover_content2.title,
           'CoverText': cover_content2.story,
           'CoverPhoto': cover_content2.photo2.url,
           'CoverAltText': cover_content2.photo_alt,
           'CoverButton': cover_content2.button,
           'CoverButtonClass': cover_content2.button_class,
           'CoverButtonLink': cover_content2.button_link,
           'DeliveryInfo': DeliveryInfo,
           'BagelsSold': str(totsold),
           'BagelsAvailable':  str(available)}
    return render(request,'MainPage/order.html', context = cover_content)

def registration(request):
    registered = False
    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'MainPage/registration.html',
                    {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered':  registered})
@csrf_exempt
def thankyou(request):
    def parseOrder(orders):
        products = {'Plain':0, 'Sesame':0, 'Salt':0, 'Poppy':0, 'Garlic':0,
                    'Onion':0, 'Everything':0, 'Cream':0, 'RandomBake':0}
        print(orders)
        for order in range(0, len(orders)):
            # if "Additional Bagels" in orders[order]:
            #     quant = int(re.findall('Quantity: .+?,',orders[order])[0].replace(",", "").replace("Quantity: ", ""))
            #     print (quant)
            #     for product in products:
            #         if (product !='Cream') & (product !='RandomBake') & (product in orders[order]):
            #             products[product] += quant
            if ("Pack" in orders[order]):
                for product in products:
                    products[product] += orders[order].count(product)
            elif (orders[order].count("Cream")!=0):
                products["Cream"] += int(orders[order][-2])
            elif (orders[order].count("RandomBake")!=0):
                products["RandomBake"] += int(orders[order][-2])
        return products
    if request.method=='POST':
        BATCH_ID = request.POST.get('batchid76')
        Batch_Info = ActiveSales.objects.get(batch=BATCH_ID)
        FormCustomer = request.POST.getlist('name[]')  #0-firstname  | 1-lastname
        FormEmail = request.POST.get('email')
        phone = request.POST.getlist('phonenumber[]')  #0-area code | 1-phone number
        phone = "%s %s" %(phone[0], phone[1])
        deliveryaddress = request.POST.getlist('deliveryaddress[]')  #0-address line 1
                                                                         #1-address line 2
                                                                         #2-city
                                                                         #3-State
                                                                         #4-Zip
        try:
            DjangoCustomer = Customer.objects.get(email=FormEmail)
        except:
            DjangoCustomer = Customer(Fname =  FormCustomer[0],
                                      Lname =  FormCustomer[1],
                                      email =  FormEmail,
                                      dStreet1 = deliveryaddress[0],
                                      dStreet2 = deliveryaddress[1],
                                      dCity =  deliveryaddress[2],
                                      dState =  deliveryaddress[3],
                                      dZip =  deliveryaddress[4],
                                      Phone = phone)
            try:
                DjangoCustomer.save()
            except:
                DjangoCustomer = Customer.objects.get(email="info@RandomBakes.com")
        PayPalData = request.POST.getlist('myproducts[]') #0-products ordered
                                                       #1-Currency type
                                                       #2-AMount charged
                                                       #3-Paypal record
                                                       #4-Fees charged
                                                       #5-??????
                                                       #6-Name of Payer
                                                       #7-email of Payer
                                                       #12-Billing st
                                                       #13-billing City
                                                       #14-billing State
                                                       #15-billing Zip
        if type(PayPalData[4]) == float:
            fees = PayPalData[4]
        elif type(PayPalData[5]) == float:
            fees = PayPalData[5]
        else:
            fees = 0
        try:
            deliverynotes = '%s\n%s\n%s, %s %s\n%s\nDelivery Notes: %s' %(deliveryaddress[0], deliveryaddress[1],
                             deliveryaddress[2],deliveryaddress[3],
                             deliveryaddress[4], phone,
                             request.POST.get('deliverynotes'))
        except:
            deliverynotes = '%s\n%s\n%s, %s %s\n%s' %(deliveryaddress[0], deliveryaddress[1],
                             deliveryaddress[2],deliveryaddress[3],
                             deliveryaddress[4], phone)
        ticket = ast.literal_eval(PayPalData[0])
        cart= parseOrder(ast.literal_eval(PayPalData[0]))
        print(cart)
        products = parseOrder(ticket)
        invoice = request.POST.get('invoiceid')
        delivered = Batch_Info.deliverydate
        cart = ""
        for t in ticket:
            cart +='%s\n' %t
        cart.replace(', Bagel ', ', B')
        
        NewOrder = Orders(invoiceid = invoice,
                            batch = Batch_Info,
                            customer = DjangoCustomer,
                            Plain_sold = products['Plain'],
                            Sesame_sold = products['Sesame'],
                            Salt_sold = products['Salt'],
                            Onion_sold = products['Onion'],
                            Poppy_sold = products['Poppy'],
                            Garlic_sold = products['Garlic'],
                            Everything_sold = products['Everything'],
                            RandomBake_sold = products['RandomBake'],
                            CreamCheese_sold = products['Cream'],
                            deliveryinfo = deliverynotes,
                            cart = cart,
                            total = PayPalData[2],
                            fees = fees
                        )
        try:
            NewOrder.save()
        except:
            print("Order Already Saved!") 
        
    else:
        BATCH_ID = "Didn't"
        Cust = ['work',""]
    try:
        subj = "%s Order placed!" %NewOrder.batch
        msg = "HUZZAH! %s %s has ordered %s" % {DjangoCustomer.Fname, DjangoCustomer.Lname, NewOrder.cart}
        send_mail('Order Placed', 'body of the message', 'info@RandomBakes.com', [config.KB, config.TT])
    except:
        print("Email Didn't work")
    return render(request, 'MainPage/thankyou.html',
                 {'BATCH_ID':NewOrder.batch,
                  'fName': DjangoCustomer.Fname,
                  'lName': DjangoCustomer.Lname,
                  'ticket': ticket,
                  'delivered': delivered,
                 })
def success(request):
    return render(request,'MainPage/sucess.html')

def shopping(request):
    return render(request,'MainPage/shopping.html')
def enterbatch(request):
    formfilled = False

    if request.method =='POST':
        batch_form = baking_batch_form(data=request.POST)
        if batch_form.is_valid():
            batch = batch_form.save()
            formfilled = True
        else:
            print(batch_form.errors )
    else:
        batch_form = baking_batch_form()
    return render(request, 'MainPage/enter_batch.html',
                  {'batch_form': batch_form,
                  'formfilled': formfilled})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login")
            return HttpResponse("Invalid login.")
    else:
        return render(request,'MainPage/user_login.html', {})
