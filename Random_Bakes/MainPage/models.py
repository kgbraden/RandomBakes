from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
import random
# Create your models here.
class highlight(models.Model):
    title = models.CharField(max_length = 35, unique = True)
    story = models.TextField()
    script = models.TextField(default="None")
    photo2 = models.ImageField(upload_to='highlight_images', default = '/media/photo-placeholder-icon.jpg')
    photo_alt = models.CharField(max_length = 25)
    button = models.CharField(max_length = 18)
    button_link = models.CharField(max_length = 264)
    button_class =models.CharField(max_length = 264, default = "index")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def get_absolute_url(self):
        return reverse("featurette_detail",kwargs={'pk':self.pk})
    def __str__(self):
        return self.title

class Featurette(models.Model):
    ind = 'index'
    abt = 'About Us'
    Snt = 'Sanitation Protocols'
    Lic = 'Licenses'
    proj = 'Projects'
    type_choices = [
                    (ind, 'index'),
                    (abt, 'About Us'),
                    (Snt, 'Sanitation'),
                    (Lic, 'Licenses'),
                    (proj, 'Projects')
    ]
    title = models.CharField(max_length = 80, unique = True)
    type = models.CharField(max_length = 35,
                            choices=type_choices)
    order =  models.PositiveIntegerField(default = 1)
    subtitle = models.CharField(max_length = 40,  blank=True)
    description = models.TextField(default="Description goes here.", blank=True)
    Story = models.TextField(blank=True)
    photo = models.ImageField(upload_to='highlight_images', blank=True)
    photo_alt = models.CharField(max_length = 25, blank=True)
    button = models.CharField(max_length = 18, blank=True)
    button_link = models.CharField(max_length = 264, default = "#")
    button_class =models.CharField(max_length = 264, default = "btn btn-sm btn-outline-secondary")
    def __str__(self):
        return '%s (%s)' %(self.title, self.type)
    
class RandomBakeItem(models.Model):
    title = models.CharField(max_length = 80, unique = True)
    description = models.TextField(blank=True)
    story = models.TextField(blank=True)
    photo = models.ImageField(upload_to='RandomBake_images', blank=True)
    amount = models.CharField(max_length = 80)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default = 5.00)
    def __str__(self):
        return '%s ($%s)' %(self.title, self.cost)

class AboutUs(models.Model):
    content = models.ManyToManyField('Featurette', related_name='features')
    # type = models.CharField(max_length = 35)
    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural ="About Us"

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username
class Subscription(models.Model):
    order_descrip = models.CharField(max_length = 50,  blank=True)
    Plain_sold = models.PositiveIntegerField(default = 0)
    Sesame_sold = models.PositiveIntegerField(default = 0)
    Salt_sold = models.PositiveIntegerField(default = 0)
    Onion_sold = models.PositiveIntegerField(default = 0)
    Poppy_sold = models.PositiveIntegerField(default = 0)
    Garlic_sold = models.PositiveIntegerField(default = 0)
    Everything_sold = models.PositiveIntegerField(default = 0)
    RandomBake_sold = models.PositiveIntegerField(default = 0)
    CreamCheese_sold = models.PositiveIntegerField(default = 0)
    deliveryinfo = models.TextField(blank = True)
    cart = models.TextField(blank = True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
    def __str__(self):
        return self.order_descrip
        
class Customer(models.Model):
    Fname = models.CharField(max_length = 50,  blank=True)
    Lname = models.CharField(max_length = 50, blank = True)
    pref_name = models.CharField(max_length = 50, blank = True)
    email = models.EmailField(max_length=254,  blank=True, unique=True)
    dStreet1 =models.CharField(max_length = 100,  blank=True)
    dStreet2 =models.CharField(max_length = 100,  blank=True)
    dCity = models.CharField(max_length = 100,  blank=True)
    dState = models.CharField(max_length = 20,  blank=True)
    dZip = models.CharField(max_length = 10,  blank=True)
    Phone =models.CharField(max_length = 20,  blank=True)
    customer_Notes =  models.TextField(blank = True)
    mailing_list = models.BooleanField(default = True)
    friend = models.BooleanField(default = False)
    subscription = models.BooleanField(default = False)
    invoice = models.CharField(max_length = 11, blank = True, null = True )
    base_order = models.ForeignKey(Subscription, on_delete = models.PROTECT, blank = True, null = True, related_name="subscription_order") 
    class Meta:
        ordering = ['Lname']
    def __str__(self):
        return '%s %s (%s)' %(self.Fname, self.Lname, self.email)

class ActiveSales(models.Model):
    d = datetime.now()
    t = timedelta((12 - d.weekday()) % 14)
    nextSat = d+t
    mon = nextSat +timedelta(days = -5)
    thurs = nextSat +timedelta(days = -2)
    deliv = datetime.strptime('10:00:00', '%I:%M:%S') 
    id = models.AutoField(primary_key=True)
    batch = models.CharField(max_length =10, unique = True, default = "BATCH_")
    active = models.BooleanField(default = False)
    start_sales = models.DateField(blank=True)
    end_sales = models.DateField(blank=True)
    units = models.PositiveIntegerField(default = 60)
    soldout = models.BooleanField(default = False)
    delivery = models.BooleanField(default = False)
    bakingdate = models.DateField(default = nextSat)
    bakingtime = models.TimeField(default = deliv)
    Plain_sold = models.PositiveIntegerField(default = 0)
    Sesame_sold = models.PositiveIntegerField(default = 0)
    Salt_sold = models.PositiveIntegerField(default = 0)
    Onion_sold = models.PositiveIntegerField(default = 0)
    Poppy_sold = models.PositiveIntegerField(default = 0)
    Garlic_sold = models.PositiveIntegerField(default = 0)
    Everything_sold = models.PositiveIntegerField(default = 0)
    RandomBake =  models.TextField(blank = True)
    rbItem = models.ForeignKey(RandomBakeItem, on_delete = models.PROTECT, blank = True, null = True, related_name="RB_Item")
    RandomBake_sold = models.PositiveIntegerField(default = 0)
    CreamCheese_sold = models.PositiveIntegerField(default = 0)
    Batch_Notes = models.TextField(blank = True)
    
    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "ActiveSales"
    def get_absolute_url(self):
        return reverse('batch', kwargs={'pk': self.pk})
    def __str__(self):
        return "%s--(%s)" %(self.batch, self.bakingdate)

class Orders(models.Model):
    randomdeliv = random.randrange(15)
    id = models.AutoField(primary_key=True)
    invoiceid = models.CharField(max_length =14, unique = True)
    batch = models.ForeignKey(ActiveSales, on_delete = models.PROTECT, related_name="order_batch")
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name='order_customer')
    Plain_sold = models.PositiveIntegerField(default = 0)
    Sesame_sold = models.PositiveIntegerField(default = 0)
    Salt_sold = models.PositiveIntegerField(default = 0)
    Onion_sold = models.PositiveIntegerField(default = 0)
    Poppy_sold = models.PositiveIntegerField(default = 0)
    Garlic_sold = models.PositiveIntegerField(default = 0)
    Everything_sold = models.PositiveIntegerField(default = 0)
    RandomBake_sold = models.PositiveIntegerField(default = 0)
    CreamCheese_sold = models.PositiveIntegerField(default = 0)
    deliveryinfo = models.TextField(blank = True)
    cart = models.TextField(blank = True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
    fees = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
    delivorder = models.PositiveIntegerField(default = randomdeliv )
    delivered = models.DateTimeField(null = True, blank=True)
    delivery_notes = models.TextField(blank = True)
    delivery_text = models.TextField(blank = True, max_length=255)
    delivery_completed = models.BooleanField(default = False)
    text_sent = models.BooleanField(default = False)
    emil_sent = models.BooleanField(default = False)
    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Orders"
    def __str__(self):
        return "%s--%s_%s (%s)" %(self.batch, self.customer.Fname, self.customer.Lname, self.invoiceid)
class Notices(models.Model):
    ind = 'index'
    abt = 'About Us'
    Snt = 'Sanitation Protocols'
    Lic = 'Licenses'
    proj = 'Projects'
    type_choices = [
                    (ind, 'index'),
                    (abt, 'About Us'),
                    (Snt, 'Sanitation'),
                    (Lic, 'Licenses'),
                    (proj, 'Projects')
    ]
    title = models.CharField(max_length = 80, unique = True)
    type = models.CharField(max_length = 35,
                            choices=type_choices)
    subtitle = models.CharField(max_length = 40,  blank=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default = False)
    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Notices"
    def __str__(self):
        return "%s (%s)" %(self.title, self.type)