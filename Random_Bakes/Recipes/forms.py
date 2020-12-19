from django import forms
from django.contrib.auth.models import User
# from Recipes.models import (
#                             #  ingredient,
                             
#                              )
# class IngredientForm(forms.ModelForm):
#     class Meta():
#         model = ingredient
#         fields = ('__all__')
#         widgets = {
#                     'ingredient': forms.TextInput(attrs={'class': 'form-control col', }),
#                     'pref_brand': forms.TextInput(attrs={'class': 'form-control col', }),
#                     'ingredient_long': forms.Textarea(attrs={'class': 'editable medium-editor-textarea feature-content'}),
#         }

# class fermIngredientForm(forms.ModelForm):
#     class Meta():
#         model = fermIngredients
#         fields = ('__all__')
#         widgets = {
#                     'ferm_ingrd_amount':forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#                     'ferm_ingred_metric': forms.Select(attrs= {'class': 'textinputclass-sm'}),
#                     'ferm_ingredient': forms.SelectMultiple(),

#         }
# #
# class doughIngredientForm(forms.ModelForm):
#     class Meta():
#         model = doughIngredients
#         fields = ('__all__')
#         widgets = {
#                     'dough_ingrd_amount':forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#                     'dough_ingred_metric': forms.Select(attrs= {'class': 'textinputclass-sm'}),
#                     'dough_ingredient': forms.SelectMultiple(),
#         }
# #
# class BakingBatchForm(forms.ModelForm):
#     class Meta():
#         model = baking_batch
#         fields = ('__all__')
#         widgets = {
#             'batch_id': forms.TextInput(attrs={'class': 'form-control col', }),
#             'batch_date': forms.TextInput(attrs={ 'size':10, 'class': 'form-control col'}),
#             'batch_type': forms.TextInput(attrs={'class': 'form-control ', }),
#             'room_temp': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#             'room_humid': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#             'preFerment': forms.Select(), 
#             'batch_photo': forms.FileInput(attrs={'class': 'form-control ', }),
#             'batch_final_notes': forms.Textarea(attrs={'class': 'editable medium-editor-textarea feature-content'}),
#         }
# #
# class PreFermentForm(forms.ModelForm):
#     class Meta():
#         model = PreFerment
#         fields = ('__all__')
#         widgets = {
#                     'ferm_ingredients': forms.SelectMultiple(),
#                     'ferm_started': forms.TimeInput(attrs= {'class': 'time_form'}),
#                     'ferm_started': forms.TimeInput(attrs= {'class': 'time_form'}),
#                     'ferm_temp_start': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#                     'ferm_temp_fermented': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#                     'ferm_temp_after_retardation': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#                     'ferm_final_weight': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#                     'ferm_notes': forms.Textarea(attrs={'class': 'editable medium-editor-textarea feature-content'}),
#         }
# class ShapingFinisihingForm(forms.ModelForm):
#     class Meta():
#         model = ShapingFinishing
#         fields = ('__all__')
#         widgets = { 'weight_each_item': forms.NumberInput(attrs= {'class': 'textinputclass-sm weight_form'}),
#                     'items_produced': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#                     'retard_started': forms.TimeInput(attrs= {'class': 'time_form'}),
#                     'retard_finished': forms.TimeInput(attrs= {'class': 'time_form'}),
#                     'shape_photo': forms.ImageField(),
#                     'preform_rest_time': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#                     'postform_rest_time': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#                     'boil_time': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#                     'oven_first_temp': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#                     'oven_first_time': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#                     'oven_second_temp': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#                     'oven_second_time': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#                     'steam_used': forms.NullBooleanSelect(attrs= {'class': ''}),
#                     'steam_time': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#                     'baked_photo': forms.ImageField(),
#                     'shaping_finishing_notes':  forms.Textarea(attrs= {'class': 'editable medium-editor-textarea feature-content'}),
#         }
# class DoughForm(forms.ModelForm):
#     class Meta():
#         model = Dough
#         fields = ('__all__')
#         widgets = {
#             'dough_ingredients': forms.SelectMultiple(attrs= {'class': ''}),
#             'dough_mixed_minutes': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#             'dough_mixer_speed':forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#             'dough_rest_time':forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#             'dough_final_temp': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#             'knead_time': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#             'knead_mixer_spring': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#             'knead_start_temp': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#             'knead_finish_temp': forms.NumberInput(attrs= {'class': 'textinputclass-sm temp_form'}),
#             'dough_final_weight':  forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
#             'dough_photo':forms.ImageField(),
#             'kneading_photo': forms.ImageField(),
#             'dough_notes': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea feature-content'}),
#         }
