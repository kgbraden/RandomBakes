from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class highlight(models.Model):
    title = models.CharField(max_length = 35, unique = True)
    story = models.CharField(max_length = 300)
    photo = models.CharField(max_length = 264)
    photo2 = models.ImageField(upload_to='highlight_images', default = '/media/photo-placeholder-icon.jpg')
    photo_alt = models.CharField(max_length = 25)
    button = models.CharField(max_length = 18)
    button_link = models.CharField(max_length = 264)
    def __str__(self):
        return self.title

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Ingredients(models.Model):
    ingredient = models.CharField(max_length = 264)
    ingred_amount = models.DecimalField(decimal_places=2, max_digits = 6)
    ingred_metric = models.CharField(max_length = 264)
    def __str__(self):
        return self.ingredient

class PreFerment(models.Model):
    ferm_ingredients = models.ManyToManyField('Ingredients')
    ferm_started =models.TimeField()
    ferm_started =models.TimeField()
    ferm_temp_start = models.DecimalField(decimal_places=1, max_digits = 4)
    ferm_temp_fermented = models.DecimalField(decimal_places=1, max_digits = 4)
    ferm_temp_after_retardation = models.DecimalField(decimal_places=1, max_digits = 4)
    ferm_final_weight =  models.DecimalField(decimal_places=2, max_digits = 6)
    ferm_notes = models.TextField(default="None")
    batch = models.ForeignKey('baking_batch', on_delete=models.CASCADE)
    def __str__(self):
        return "Preferment info for: " + self.batch
class Dough(models.Model):
    dough_ingredients = models.ManyToManyField('Ingredients')
    dough_mixed_minutes = models.DecimalField(decimal_places=1, max_digits = 4)
    dough_mixer_speed = models.PositiveIntegerField()
    dough_rest_time = models.DecimalField(decimal_places=1, max_digits = 4)
    dough_final_temp = models.DecimalField(decimal_places=1, max_digits = 4)
    knead_time = models.DecimalField(decimal_places=1, max_digits = 4)
    knead_mixer_spring = models.PositiveIntegerField()
    knead_start_temp = models.DecimalField(decimal_places=1, max_digits = 4)
    knead_finish_temp = models.DecimalField(decimal_places=1, max_digits = 4)
    dough_final_weight =  models.DecimalField(decimal_places=2, max_digits = 6)
    dough_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
    kneading_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
    dough_notes = models.TextField(default="None")
    batch = models.ForeignKey('baking_batch', on_delete=models.CASCADE)
    def __str__(self):
        return "Dough info for: " + self.batch

class ShapingFinishing(models.Model):
    weight_each_item =  models.DecimalField(decimal_places=2, max_digits = 6)
    items_produced = models.PositiveIntegerField()
    retard_started = models.TimeField()
    retard_finished = models.TimeField()
    shape_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
    preform_rest_time = models.DecimalField(decimal_places=1, max_digits = 4)
    postform_rest_time = models.DecimalField(decimal_places=1, max_digits = 4)
    boil_time = models.DecimalField(decimal_places=1, max_digits = 4)
    oven_first_temp = models.PositiveIntegerField()
    oven_first_time = models.PositiveIntegerField()
    oven_second_temp = models.PositiveIntegerField()
    oven_second_time = models.PositiveIntegerField()
    steam_used = models.BooleanField()
    steam_time = models.PositiveIntegerField()
    baked_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
    shaping_finishing_notes = models.TextField(default="None")

    batch = models.ForeignKey('baking_batch', on_delete=models.CASCADE)
    def __str__(self):
        return "Shaping/Finishing info for: " + self.batch


class baking_batch(models.Model):
    batch_id = models.CharField(max_length = 30, primary_key = True)
    batch_date = models.DateField()
    batch_type = models.CharField(max_length = 100)
    room_temp = models.DecimalField(decimal_places=1, max_digits = 4)
    room_humid = models.DecimalField(decimal_places=1, max_digits = 4)
    PreFerment =models.OneToOneField('PreFerment', on_delete=models.CASCADE)
    Dough = models.OneToOneField('Dough', on_delete=models.CASCADE)
    ShapingFinishing = models.OneToOneField('ShapingFinishing', on_delete=models.CASCADE)
    batch_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
    batch_final_notes = models.TextField(default="None")
    def __str__(self):
        return self.batch_id
