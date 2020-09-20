from django import forms
from django.contrib.auth.models import User
from MainPage.models import (UserProfileInfo,
                             highlight,
                             # baking_batch,
                             # Ingredient,
                             # PreFerment,
                             # Dough,
                             # ShapingFinishing,
                             Featurette,)

class UserForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
#
# class baking_batch_form(forms.ModelForm):
#     class Meta():
#         model = baking_batch
#         widgets = {
#             'batch_id': forms.TextInput(attrs={'class': 'form-control col', }),
#             'batch_date': forms.TextInput(attrs={ 'size':10, 'class': 'form-control col'}),
#             'batch_type': forms.TextInput(attrs={'class': 'form-control ', }),
#             'room_temp': forms.TextInput(attrs={'class': 'form-control ', }),
#             'room_humid': forms.TextInput(attrs={'class': 'form-control ', }),
#             'batch_photo': forms.FileInput(attrs={'class': 'form-control ', }),
#             'batch_final_notes': forms.Textarea(attrs={'class': 'form-control ', }),
#         }
#         fields = ('batch_id',
#                   'batch_date',
#                   'batch_type',
#                   'room_temp',
#                   'room_humid',
#                   'PreFerment',
#                   'Dough',
#                   'ShapingFinishing',
#                   'batch_photo',
#                   'batch_final_notes')
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

class FeaturetteForm(forms.ModelForm):
    class Meta():
        model = Featurette
        # fields = ('title', 'type', 'order','subtitle', 'description','Story','photo','photo_alt','button', 'button_link, ''button_class')
        fields = ('__all__')
        # forms.ImageField(label=_('Company Logo'),required=False, error_messages = {'invalid':_("Image files only")}, widget=forms.FileInput)
        photo = forms.ImageField()
        widgets = {
                   'title': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea feature-content'}),
                   # 'type': forms.TextInput(attrs= {'class': 'textinputclass'}),
                   'order': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                   'subtitle': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea feature-content'}),
                   'description':forms.Textarea(attrs= {'class': 'editable medium-editor-textarea feature-content'}) ,
                   'Story': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea feature-content'}),
                   # 'photo': forms.ClearableFileInput,
                   'photo_alt': forms.TextInput(attrs= {'class': 'textinputclass'}),
                   'button': forms.TextInput(attrs= {'class': 'textinputclass'}),
                   'button_link': forms.TextInput(attrs= {'class': 'textinputclass'}),
                   'button_class':forms.TextInput(attrs= {'class': 'textinputclass'})
        }
