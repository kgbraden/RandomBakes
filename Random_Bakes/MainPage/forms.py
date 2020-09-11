from django import forms
from django.contrib.auth.models import User
from MainPage.models import (UserProfileInfo,
                             highlight,
                             baking_batch,
                             Ingredients,
                             PreFerment,
                             Dough,
                             ShapingFinishing)

class UserForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

class baking_batch_form(forms.ModelForm):
    class Meta():
        model = baking_batch
        widgets = {
            'batch_id': forms.TextInput(attrs={'class': 'form-control col', }),
            'batch_date': forms.TextInput(attrs={ 'size':10, 'class': 'form-control col'}),
            'batch_type': forms.TextInput(attrs={'class': 'form-control ', }),
            'room_temp': forms.TextInput(attrs={'class': 'form-control ', }),
            'room_humid': forms.TextInput(attrs={'class': 'form-control ', }),
            'batch_photo': forms.FileInput(attrs={'class': 'form-control ', }),
            'batch_final_notes': forms.Textarea(attrs={'class': 'form-control ', }),
        }
        fields = ('batch_id',
                  'batch_date',
                  'batch_type',
                  'room_temp',
                  'room_humid',
                  'PreFerment',
                  'Dough',
                  'ShapingFinishing',
                  'batch_photo',
                  'batch_final_notes')
