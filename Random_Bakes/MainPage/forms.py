from django import forms
from django.contrib.auth.models import User
from MainPage.models import (UserProfileInfo,
                             highlight,
                             baking_batch,
                             Ingredients,
                             PreFerment,
                             Dough,
                             ShapingFinishing,
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
