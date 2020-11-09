from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
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
    description = models.TextField(max_length = 430, default="Description goes here.", blank=True)
    Story = models.TextField(blank=True)
    photo = models.ImageField(upload_to='highlight_images', blank=True)
    photo_alt = models.CharField(max_length = 25, blank=True)
    button = models.CharField(max_length = 18, blank=True)
    button_link = models.CharField(max_length = 264, default = "#")
    button_class =models.CharField(max_length = 264, default = "btn btn-sm btn-outline-secondary")


    def __str__(self):
        return '%s (%s)' %(self.title, self.type)

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
class Customer(models.Model):
    Fname = models.CharField(max_length = 50,  blank=True)
    Lname = models.CharField(max_length = 50, blank = True)
    pref_name = models.CharField(max_length = 50, blank = True)
    email = models.EmailField(max_length=254,  blank=True, unique=True)
    dStreet1 =models.CharField(max_length = 100,  blank=True)
    dStreet2 =models.CharField(max_length = 100,  blank=True)
    dCity = models.CharField(max_length = 100,  blank=True)
    dState = models.CharField(max_length = 3,  blank=True)
    dZip = models.CharField(max_length = 10,  blank=True)
    Phone =models.CharField(max_length = 20,  blank=True)
    customer_Notes =  models.TextField(blank = True)
    mailing_list = models.BooleanField(default = False)
    rando = models.BooleanField(default = False)
    def __str__(self):
        return '%s %s' %(self.Fname, self.Lname)

class ActiveSales(models.Model):
    id = models.AutoField(primary_key=True)
    batch = models.CharField(max_length =10, unique = True)
    active = models.BooleanField(default = False)
    start_sales = models.DateField(blank=True)
    end_sales = models.DateField(blank=True)
    units = models.PositiveIntegerField()
    soldout = models.BooleanField(default = False)
    bakingdate = models.DateField(default=datetime.now, blank=True)
    deliverydate = models.DateField(default=datetime.now, blank=True)
    bakingtime = models.TimeField(default=datetime.now, blank=True)
    Plain_sold = models.PositiveIntegerField(default = 0)
    Sesame_sold = models.PositiveIntegerField(default = 0)
    Salt_sold = models.PositiveIntegerField(default = 0)
    Onion_sold = models.PositiveIntegerField(default = 0)
    Poppy_sold = models.PositiveIntegerField(default = 0)
    Garlic_sold = models.PositiveIntegerField(default = 0)
    Everything_sold = models.PositiveIntegerField(default = 0)
    RandomBake =  models.TextField(blank = True)
    RandomBake_sold = models.PositiveIntegerField(default = 0)
    CreamCheese_sold = models.PositiveIntegerField(default = 0)
    Batch_Notes =  models.TextField(blank = True)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "ActiveSales"
    def get_absolute_url(self):
        return reverse('batch', kwargs={'pk': self.pk})
    def __str__(self):
        return self.batch

class Orders(models.Model):
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
    delivorder = models.PositiveIntegerField(default = 0)
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
# class fermIngredients(models.Model):
#     ferm_ingrd_amount = models.DecimalField(decimal_places=2, max_digits = 6)
#     ferm_ingred_metric = models.TextField(max_length = 40, choices=metric_choices)
#     ingredients =models.ForeignKey(Ingredient, on_delete=models.CASCADE )
# class baking_batch(models.Model):
#     batch_id = models.CharField(max_length = 30, primary_key = True)
#     batch_date = models.DateField()
#     batch_type = models.CharField(max_length = 100)
#     room_temp = models.DecimalField(decimal_places=1, max_digits = 4)
#     room_humid = models.DecimalField(decimal_places=1, max_digits = 4)
#     batch_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
#     batch_final_notes = models.TextField(default="None")
#     def __str__(self):
#         return self.batch_id
#
# class PreFerment(models.Model):
#     ferm_ingredients = models.ManyToManyField(fermIngredients)
#     ferm_started =models.TimeField()
#     ferm_started =models.TimeField()
#     ferm_temp_start = models.DecimalField(decimal_places=1, max_digits = 4)
#     ferm_temp_fermented = models.DecimalField(decimal_places=1, max_digits = 4)
#     ferm_temp_after_retardation = models.DecimalField(decimal_places=1, max_digits = 4)
#     ferm_final_weight =  models.DecimalField(decimal_places=2, max_digits = 6)
#     ferm_notes = models.TextField(default="None")
#     batch = models.ForeignKey(baking_batch, on_delete=models.CASCADE)
#     def __str__(self):
#         return "Preferment info for: " + self.batch
#
# class doughIngredients(models.Model):
#     dough_ingrd_amount = models.DecimalField(decimal_places=2, max_digits = 6)
#     dough_ingred_metric = models.TextField(max_length = 40, choices=metric_choices)
#     ingredients =models.ForeignKey(Ingredient, on_delete=models.CASCADE )
#
# class Dough(models.Model):
#     dough_ingredients = models.ManyToManyField(doughIngredients)
#     dough_mixed_minutes = models.DecimalField(decimal_places=1, max_digits = 4)
#     dough_mixer_speed = models.PositiveIntegerField()
#     dough_rest_time = models.DecimalField(decimal_places=1, max_digits = 4)
#     dough_final_temp = models.DecimalField(decimal_places=1, max_digits = 4)
#     knead_time = models.DecimalField(decimal_places=1, max_digits = 4)
#     knead_mixer_spring = models.PositiveIntegerField()
#     knead_start_temp = models.DecimalField(decimal_places=1, max_digits = 4)
#     knead_finish_temp = models.DecimalField(decimal_places=1, max_digits = 4)
#     dough_final_weight =  models.DecimalField(decimal_places=2, max_digits = 6)
#     dough_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
#     kneading_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
#     dough_notes = models.TextField(default="None")
#     batch = models.ForeignKey(baking_batch, on_delete=models.CASCADE)
#     def __str__(self):
#         return "Dough info for: " + self.batch
#
# class ShapingFinishing(models.Model):
#     weight_each_item = models.DecimalField(decimal_places=2, max_digits = 6)
#     items_produced = models.PositiveIntegerField()
#     retard_started = models.TimeField()
#     retard_finished = models.TimeField()
#     shape_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
#     preform_rest_time = models.DecimalField(decimal_places=1, max_digits = 4)
#     postform_rest_time = models.DecimalField(decimal_places=1, max_digits = 4)
#     boil_time = models.DecimalField(decimal_places=1, max_digits = 4)
#     oven_first_temp = models.PositiveIntegerField()
#     oven_first_time = models.PositiveIntegerField()
#     oven_second_temp = models.PositiveIntegerField()
#     oven_second_time = models.PositiveIntegerField()
#     steam_used = models.BooleanField()
#     steam_time = models.PositiveIntegerField()
#     baked_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
#     shaping_finishing_notes = models.TextField(default="None")
#     batch = models.ForeignKey(baking_batch, on_delete=models.CASCADE)
#     def __str__(self):
#         return "Shaping/Finishing info for: " + self.batch
