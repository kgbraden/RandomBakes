from django.db import models

# Create your models here.
# class baking_batch(models.Model):
#     batch_id = models.CharField(max_length = 30, primary_key = True)
#     batch_date = models.DateField()
#     batch_type = models.CharField(max_length = 100)
#     room_temp = models.DecimalField(decimal_places=1, max_digits = 4, default = 75.0)
#     room_humid = models.DecimalField(decimal_places=1, max_digits = 4, default = 50)
#     #preFerment = models.OneToOneField('PreFerment', on_delete=models.CASCADE, blank=True)
#     batch_photo = models.ImageField(upload_to='batch_images', default = '/media/photo-placeholder-icon.jpg')
#     batch_final_notes = models.TextField(blank=True)
#     def __str__(self):
#         return self.batch_id
metric_choices = [
                ('g', 'Grams'),
                ('Kg', 'Kilogram'),
                ('mL', 'milliliters'),
                ('Oz', 'Ounces'),
                ('Lb', 'Pounds'),
                ('Tbs', 'Tablespoon'),
                ('Tsp', 'Teaspoon'),
                ('Cup', 'Cup')
    ]
# class ingredient(models.Model):
#     ingredient = models.CharField(max_length = 264)
#     ingrd_amount = models.DecimalField(decimal_places=2, max_digits = 6, default = 1)
#     ingrd_metric = models.TextField(max_length = 40, choices = metric_choices, default = 'g')
#     ingrd_photo = models.ImageField(upload_to='recipe_images', blank=True, null=True)
#     def __str__(self):
#         return self.ingredient

# class recipe_step(models.Model):
#     step_title = models.CharField(max_length = 40)
#     step_descrip = models.TextField()
#     step_order = models.PositiveIntegerField(default = 1)
#     step_photo = models.ImageField(upload_to='recipe_images', blank=True, null=True)
#     def __str__(self):
#         return "%s) %s" %(self.step_order, self.step_title)
# class recipe_type(models.Model):
#     rec_type = models.CharField(max_length = 40)
#     class Meta:
#         ordering = ['rec_type']
#     def __str__(self):
#         return self.rec.type
# class mise_en_place(models.Model):
#     mise_title = models.CharField(max_length = 40)
#     mise_order = models.PositiveIntegerField(default = 1)
#     mise_ingrds = models.ManyToManyField(ingredient, related_name="ingredients") 
#     mise_steps = models.ManyToManyField(recipe_step, related_name='steps')
#     class Meta:
#         ordering = ['mise_order']
#     def __str__(self):
#         return self.mise_title
# class recipe(models.Model):
#     recipe_title = models.TextField(max_length = 255)
#     recipe_type = models.ManyToManyField(recipe_type, related_name = "rec_types")
#     recipe_source = models.TextField(max_length = 255, blank=True, null=True)
#     recipe_mise = models.ManyToManyField(mise_en_place, related_name='mise')
#     recipe_notes = models.TextField( blank=True, null=True)
#     recipe_photo = models.ImageField(upload_to='recipe_images', blank=True, null=True)
#     class Meta:
#         ordering = ['recipe_title']
#     def __str__(self):
#         return self.recipe_title


#------------------------------------------------------------------------------------------------------------------#
# class fermIngredients(models.Model):
#     ferm_ingrd_amount = models.DecimalField(decimal_places=2, max_digits = 6)
#     ferm_ingred_metric = models.TextField(max_length = 40, choices = metric_choices)
#     ferm_ingredient =models.ForeignKey(Ingredient, on_delete=models.CASCADE )
#     def __str__(self):
#         return "%s (%s)--%s" %(self.ferm_ingrd_amount, self.ferm_ingred_metric, self.ingredient.ingredient)
# #
# class PreFerment(models.Model):
#     ferm_ingredients = models.ManyToManyField(fermIngredients)
#     ferm_started = models.TimeField()
#     ferm_started = models.TimeField()
#     ferm_temp_start = models.DecimalField(decimal_places=1, max_digits = 4)
#     ferm_temp_fermented = models.DecimalField(decimal_places=1, max_digits = 4)
#     ferm_temp_after_retardation = models.DecimalField(decimal_places=1, max_digits = 4)
#     ferm_final_weight =  models.DecimalField(decimal_places=2, max_digits = 6)
#     ferm_notes = models.TextField(default="None")
#     batch = models.ForeignKey(baking_batch, on_delete=models.CASCADE)
#     def __str__(self):
#         return "Preferment info for: " + self.batch.batch_id

# class doughIngredients(models.Model):
#     dough_ingrd_amount = models.DecimalField(decimal_places=2, max_digits = 6)
#     dough_ingred_metric = models.TextField(max_length = 40, choices = metric_choices)
#     dough_ingredient =models.ForeignKey(Ingredient, on_delete=models.CASCADE )
#     def __str__(self):
#         return "%s (%s)--%s" %(self.dough_ingrd_amount, self.dough_ingred_metric, self.ingredient.ingredient)

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
#         return "Dough info for: " + self.batch.batch_id

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
#         return "Shaping/Finishing info for: " + self.batch.batch_id
