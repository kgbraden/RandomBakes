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
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#

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
