from django.shortcuts import render, get_object_or_404, redirect
from MainPage.models import (highlight,
                             ActiveSales,
                             Featurette,
                             Orders,
                             Customer, 
                             Subscription, 
                             Notices)
from django.utils import timezone
from MainPage.forms import (UserForm,
                            UserProfileInfoForm,
                            ActiveSalesForm,
                            AS_Create_Form,
                            FeaturetteForm, 
                            OrdersForm,
                            CustomerForm)
from check_inventory import ProcessSales
from check_inventory import route 
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
from datetime import date, datetime,timedelta
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
    notice = Notices.objects.filter(type = 'index', active = "True")
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
           'TotalSold': totsold, 
           'NextSaleOpen':B_info[3], 
           'Notices': notice,
           'RB': B_info[4], 
           'LastBaked': B_info[5]}
    return render(request,'MainPage/index.html', context = cover_content)


def setRoute(request):
    try:
        invt = ActiveSales.objects.get(delivery ="True")
        return redirect(route(invt.id))
    except: 
        web = 'MainPage/index.html'
    return render(request, web)

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

class RBsListView(ListView):
    template_name = 'MainPage/blank_content.html'
    queryset = Featurette.objects.filter(type = 'Projects')
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
def BuildTicket(tickets):
    for ticket in tickets:
        ordered = {}
        if ticket.Plain_sold > 0:
            ordered['Plain'] = int(ticket.Plain_sold)
        if ticket.Sesame_sold > 0:
            ordered['Sesame'] = ticket.Sesame_sold            
        if ticket.Salt_sold > 0:
            ordered['Salt'] = ticket.Salt_sold
        if ticket.Onion_sold > 0:
            ordered['Onion'] = ticket.Onion_sold
        if ticket.Poppy_sold > 0:
            ordered['Poppy'] = ticket.Poppy_sold
        if ticket.Garlic_sold > 0:
            ordered['Garlic'] = ticket.Garlic_sold
        if ticket.Everything_sold > 0:
            ordered['Every'] = ticket.Everything_sold
        if ticket.RandomBake_sold > 0:
            ordered['R_Bake']= ticket.RandomBake_sold
        if ticket.CreamCheese_sold > 0:
            ordered['C_Cheese'] =  ticket.CreamCheese_sold
        if ticket.Dog_sold >0:
            ordered['Dog_T']= ticket.Dog_sold
        if ticket.EvMix_sold >0:
            ordered['Ev_Mix'] = ticket.EvMix_sold
        if ticket.AButter_sold >0:
            ordered['A_Butter'] = ticket.AButter_sold
        built = "<div><table >"
        if ticket.recipient:
            built+= '<tr><td colspan="2"><div class = "name">%s</div></td></tr>' % ticket.recipient
        else:
            built +='<tr><td colspan="2"><div class = "name">%s %s</div></td></tr>' %(ticket.customer.Fname, ticket.customer.Lname)
        built += '<tr><td colspan="2">%s</td></tr>' %ticket.deliveryinfo.replace('\n', '<br>').replace('<br><br>', '<br>').replace('Delivery Notes: None', "")[:100]
        col = 1
        for order in ordered:
            if not (col %2 )==0:
                built +="<tr><td>%s: %s </td>" %(order, ordered[order])
            else:
                built += "<td>%s: %s </td></tr>" %(order, ordered[order])
            col+=1
        if not (col %2 )==0:
            built += "<td></td></tr></table> </div>"
        else:
            built += "</table> </div>"
        ticket.ticket_text =built
        try:
                ticket.save()
        except:
            print(built)

def TicketListView(request):
    batches = ActiveSales.objects.all().order_by("-batch")
    if request.GET.get('batch'):
        acv_sales = ActiveSales.objects.get(batch = request.GET.get('batch'))
    else:
        acv_sales = ActiveSales.objects.get(active = "True")    
    tickets = Orders.objects.filter(batch = acv_sales.id).order_by('customer')
    BuildTicket(tickets)   
    return render(request,'MainPage/tickets.html', {'tickets': tickets, 
                                                    'batches': batches,
                                                    
                                                     })
def TrayListView(request):    
        
    acv_sales = ActiveSales.objects.filter(active =True)[0]
    print (acv_sales.Plain_sold)
    return render(request,'MainPage/trays.html', {'sold': acv_sales,
                                                    'plainrange': range(acv_sales.Plain_sold),
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
        text = request.POST['message']
        # text = "Your Bagel order is at your front door! Thank you and enjoy! (This is an automated text!)"
        now = Now()
        # send_mail('test', 'body of the message', 'info@RandomBakes.com', ['kale@ebraden.com'])
        if (request.POST['sendText']=="Delivered"):
            if (len(phone)==11):
                status = sendtext(phone, text)
            else:
                status = "%s Number not correct length, text not sent. " %phone
        else:
            status = "Order delivered, no text notification sent."
        # try:
        #     subj = "%s Order placed!" %NewOrder.batch
        #     msg = "HUZZAH! %s %s has ordered %s" % {DjangoCustomer.Fname, DjangoCustomer.Lname, NewOrder.cart}
        #     send_mail('Order Placed', 'body of the message', 'info@RandomBakes.com', [config.KB, config.TT])
        # except:
        #     print("Email Didn't work")
        try:
            OrderTracing = Orders.objects.get(id=OrdId)
            status += " %s Delivery recorded" %(OrderTracing.batch)
            
            OrderTracing.delivered = now
            OrderTracing.delivorder= OrderTracing.delivorder+20
            OrderTracing.delivery_notes = status
            OrderTracing.delivery_completed ==True
            OrderTracing.text_sent == text
            OrderTracing.save()
            
        except:
            status += "Delivery Not recorded"
    
        
    return redirect("../orders/")

# class DeliveryView(ListView):
#     acv_sales = ActiveSales.objects.get(active = "True")    
#     queryset = Orders.objects.filter(batch = acv_sales.id).order_by('delivorder')
#     template_name = "MainPage/orders_list.html"

class DeliveryView(ListView):
       
    model = Orders
    template_name = "MainPage/orders_list.html"
    def get_context_data(self, **kwargs):
        try:
            acv_sales = ActiveSales.objects.get(delivery = "True") 
        except:
            acv_sales = ActiveSales.objects.get(active = "True") 
        context = super(DeliveryView, self).get_context_data(**kwargs)
        context.update({
            'orders_list': Orders.objects.filter(batch = acv_sales.id).order_by('delivorder'),
            'batch': ActiveSales.objects.all(),
        })
        return context

    def get_queryset(self):
        try:
            acv_sales = ActiveSales.objects.get(delivery = "True") 
        except:
            acv_sales = ActiveSales.objects.get(active = "True") 
        return Orders.objects.filter(batch = acv_sales.id).order_by('delivorder')

class OrdersDetailView(DetailView):
    # slug_field='Customer.Lname'
    # slug_url_kwarg='batch'
    # send_mail('test', 'body of the message', 'info@RandomBakes.com', ['kale@ebraden.com'])
    model = Orders
class CustomersListView(ListView):
    model = Customer
    template_name = "MainPage/Customer_list.html"
    paginate_by = 10
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
    template_name = 'MainPage/ActiveSales_new.html'
    # redirect_field_name = '/MainPage/featurette_update'
    success_url = '/Baking/ACsuccess/'
    form_class = AS_Create_Form
    model = ActiveSales
    
class CustomersCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    # redirect_field_name = '/MainPage/featurette_update'
    success_url = '/Baking/success/'
    form_class = CustomerForm
    model = Customer       
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
    success_url = '/Baking/ACsuccess/'
    form_class = ActiveSalesForm
    model = ActiveSales

class OrdersUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'MainPage/order_form.html'
    success_url = '/Baking/orders/'
    form_class = OrdersForm
    model = Orders

class CustomersUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'MainPage/Customer_form.html'
    success_url = '/Baking/success/'
    form_class = CustomerForm
    model = Customer
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
    deliverydate = acv_sales.bakingdate.strftime('%A, %B %e, %Y')
    DeliveryInfo = ""
    nxtdateopen = "Not Set"
    rb = ""
    LastBaked = []
    if acv_sales.rbItem:
        prev = ActiveSales.objects.filter(rbItem = acv_sales.rbItem)
        for x in prev:
            if x !=acv_sales: LastBaked.append(x.bakingdate.strftime('%B %d, %Y'))
    available = acv_sales.units
    if (acv_sales.soldout == True):
        DeliveryInfo = "We're sorry, %s is sold out. We are producing %s bagels to be delivered on %s." %(activeBatch, available, deliverydate)
        out = True
        try:
            nBatch = ActiveSales.objects.get(batch =nextbatch)
            nxtdateopen =  nBatch.start_sales.strftime('%A, %B %e, %Y')
        except:
            nxtdateopen = "Not Set"
    else:
        out = False
    sales_open = False
    if (acv_sales.start_sales <= today) & (today <= acv_sales.end_sales):
        # In sales period
        sales_open = True
        rb = acv_sales.rbItem
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
    elif (acv_sales.start_sales > today):
        sales_open = False
        deliverytime = acv_sales.bakingtime.strftime('%I:%M %p')
        storeopen = acv_sales.start_sales.strftime('%A, %B %e, %Y')
        DeliveryInfo = "Sales are not open yet for %s. Sales will open on %s. " %(acv_sales.batch, storeopen)
        DeliveryInfo += "%s is scheduled to be baked and delivered on %s. Deliveries will begin after %s when the bagels have cooled enough for packaging. We anticipate deliveries to be completed by 12:00 noon. We will deliver within 10 miles of Tahoe Park and provide contact-less delivery." %(acv_sales.batch, deliverydate, deliverytime)
        rb = acv_sales.rbItem
    else:
        if ActiveSales.objects.filter(batch =nextbatch).count()==1:
            #Checks to see if the next batch has been scheduled
            nBatch = ActiveSales.objects.get(batch =nextbatch)
            rb = nBatch.rbItem
            nxtdateopen =  nBatch.start_sales.strftime('%A, %B %e, %Y')
            nxtdatedelivery = nBatch.bakingdate.strftime('%A, %B %e, %Y')
            DeliveryInfo = "Our next scheduled production run, %s, of %s bagels, will be on %s. Sales will open for this batch on %s." %(nextbatch, nBatch.units,  nxtdatedelivery, nxtdateopen)
        else:
            DeliveryInfo = "We have not scheduled our next scheduled production run. Please check back soon!"
    feature = Featurette.objects.get(title ='Current Batch')
    feature.description = DeliveryInfo
    feature.save()
    return available, out, sales_open, nxtdateopen, rb, LastBaked

def order(request):
    acv_sales = ActiveSales.objects.filter(active =True)[0]
    today = date.today()
    deliverydate = acv_sales.bakingdate.strftime('%A, %B %e, %Y')
    storedate = acv_sales.start_sales.strftime('%A, %B %e, %Y')
    deliverytime = acv_sales.bakingtime.strftime('%I:%M %p')
    activeBatch = acv_sales.batch
    nextbatch = next_batch(activeBatch)
    if ActiveSales.objects.filter(batch =nextbatch).count()==1:
        #Checks to see if the next batch has been scheduled
        nBatch = ActiveSales.objects.get(batch =nextbatch)
        NxtSched = True
        nxtdateopen =  nBatch.start_sales.strftime('%A, %B %e, %Y')
        nxtdatedelivery = nBatch.bakingdate.strftime('%A, %B %e, %Y')
    else:
        NxtSched = False
    if ((acv_sales.start_sales - timedelta(days=1)) <= today) & (today < acv_sales.end_sales):
        # In sales period

        sold = ProcessSales()
        totsold = sold['totBagels']
        if acv_sales.RandomBake:
            DeliveryInfo = "<h3>This week's Random Bake!</h3>" + acv_sales.RandomBake + "<br>"
            DeliveryInfo += "<h3>Delivery Info</h3>%s is scheduled to be baked and delivered on %s. Deliveries will begin after %s when the bagels have cooled enough for packaging. We anticipate deliveries to be completed by 12:00 noon. We will deliver within 10 miles of Tahoe Park and provide contact-less delivery." %(acv_sales.batch, deliverydate, deliverytime)
        else:
            DeliveryInfo = "%s is scheduled to be baked and delivered on %s. Deliveries will begin after %s when the bagels have cooled enough for packaging. We anticipate deliveries to be completed by 12:00 noon. We will deliver within 10 miles of Tahoe Park and provide contact-less delivery." %(acv_sales.batch, deliverydate, deliverytime)
        available = acv_sales.units
        if acv_sales.soldout ==True:
            cover_content2 = highlight.objects.filter(title = "Sold Out!")[0]
        else:
            cover_content2 = highlight.objects.filter(title = "Buy Now")[0]
    elif (acv_sales.start_sales > today):
        ## THIS IS NOT WORKING
        sold = 'N/A'
        totsold = "N/A"
        available = 'N/A'
        cover_content2 = highlight.objects.filter(title = "Sales Closed")[0]
        DeliveryInfo = "%s is scheduled to be baked and delivered on %s. Deliveries will begin after %s when the bagels have cooled enough for packaging. We anticipate deliveries to be completed by 12:00 noon. We will deliver within 10 miles of Tahoe Park and provide contact-less delivery." %(acv_sales.batch, deliverydate, deliverytime)
    else:
        sold = 'N/A'
        totsold = "N/A"
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

def special_order(request):
    return render(request,'MainPage/special_order.html')

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
            print("The answer you are looking for is: %s" %products)
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
        delivered = Batch_Info.bakingdate
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
@csrf_exempt
def TYnew(request):
    def parseOrder(orders):
        products = {'Plain':0, 'Sesame':0, 'Salt':0, 'Poppy':0, 'Garlic':0,
                    'Onion':0, 'Everything':0, 'Cream':0, 'RandomBake':0, 'DogTreats': 0, 'EvMix':0,'AButter':0 }
        #print(orders)
        for order in range(0, len(orders)):
            # if "Additional Bagels" in orders[order]:
            #     quant = int(re.findall('Quantity: .+?,',orders[order])[0].replace(",", "").replace("Quantity: ", ""))
            #     print (quant)
            #     for product in products:
            #         if (product !='Cream') & (product !='RandomBake') & (product in orders[order]):
            #             products[product] += quant
            #print(order)
            ord = orders[order]
            #print(ord)
            if ("Pack" in ord):
                bTYPE = ord[(ord.find("Bagels: ")):(ord.find(", Q"))].replace("Bagels: ", "")
                bTYPE = bTYPE.replace(" seed", "")
                products[bTYPE] += int(ord[(ord.find("Quantity: ")):-1].replace("Quantity: ", ""))
                
                #print(bTYPE,products)
            elif (orders[order].count("Cream")!=0):
                products["Cream"] += int(orders[order][-2])
            elif (orders[order].count("RandomBake")!=0):
                products["RandomBake"] += int(orders[order][-2])
            elif (orders[order].count("Dog")!=0):
                products["DogTreats"] += int(orders[order][-2])
            elif (orders[order].count("Mix")!=0):
                products["EvMix"] += int(orders[order][-2])
            elif (orders[order].count("Butter")!=0):
                products["AButter"] += int(orders[order][-2])
            #print("The answer you are looking for is: %s" %products)
            
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
                                                       #2-Delivery
                                                       #3-total
                                                       #4-total + delivery
                                                       
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
        #print(cart)
        products = parseOrder(ticket)
        invoice = request.POST.get('invoiceid')
        delivered = Batch_Info.bakingdate
        cart = ""
        tkts = []
        for p in products:
            if products[p]>0:
                cart += "%s: %s\n" %(p.replace("Cream", "Cream Cheese").replace("DogTreats", "Dog Treats").replace("EvMix", "Everything Mix").replace("AButter", "Apple Butter"), products[p])
                tkts.append("%s: %s" %(p.replace("Cream", "Cream Cheese").replace("DogTreats", "Dog Treats").replace("EvMix", "Everything Mix").replace("AButter", "Apple Butter"), products[p]))
        #for t in ticket:
        #    cart +='%s\n' %t
        #cart.replace(', Bagel ', ', B')
        #tkts.append("Delivery: $%s" %PayPalData[2])
        #tkts.append("Total: $%s") %PayPalData[3]
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
                            Dog_sold = products['DogTreats'],
                            EvMix_sold = products['EvMix'],
                            AButter_sold = products['AButter'],
                            deliveryinfo = deliverynotes,
                            cart = cart,
                            total = PayPalData[4],
                            fees = fees
                        )
        #print("0: %s, 1: %s, 2: %s, 3: %s, 4: %s" %(PayPalData[0], PayPalData[1], PayPalData[2], PayPalData[3], PayPalData[4]))
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
                  'ticket': tkts,
                  'delivered': delivered,
                 })
    """
    return render(request, 'MainPage/thankyou.html',
                 {'BATCH_ID':"BATCH_test",
                  'fName': "Kale",
                  'lName': "Braden",
                  'ticket': "ticket",
                  'delivered': "delivered",
                 })
    """             
def success(request):
    return render(request,'MainPage/sucess.html')

def ACsuccess(request):
    bat = ActiveSales.objects.filter().order_by('-id')[0]
    subscribers(bat.batch)
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

def subscribers(newBatch):
    AC = newBatch.split("_")[1]
    new_bat = ActiveSales.objects.get(batch = newBatch)
    subscribers = Customer.objects.filter(subscription = True)
    for s in subscribers:
        order = Subscription.objects.get(order_descrip = s.base_order)
        invoice_id = "%s%s" %(order.order_descrip, AC)
        o = Orders.objects.get_or_create(
                                    invoiceid = invoice_id,
                                    batch = new_bat,
                                    customer = s,
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
                                    cart = order.cart, 
                                    total = order.total
        )
        try:
            o.save()
        except:
            print("already saved!")

@login_required
def email(request):
    acv_sales = ActiveSales.objects.filter(active ="True")[0]
    
    subscribed = Customer.objects.filter(mailing_list = True)
    today = date.today()
    activeBatch = acv_sales.batch
    nextbatch = next_batch(activeBatch)
    deliverydate = acv_sales.bakingdate.strftime('%A, %B %e')
    salesopen = acv_sales.start_sales.strftime('%A, %B %e')
    rBake = acv_sales.RandomBake
    context = {"Batch": acv_sales.batch.replace("_", " "), 
               "SalesStart": acv_sales.start_sales.strftime('%A, %B %e'), 
               "DeliveryDate": acv_sales.bakingdate.strftime('%A, %B %e'), 
               "RandomBake": acv_sales.RandomBake, 
               "rbitem": acv_sales.rbItem,
               "list":subscribed}
    return render(request, 'MainPage/email.html', context = context)