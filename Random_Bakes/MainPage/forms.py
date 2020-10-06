from django import forms
from django.contrib.auth.models import User
from MainPage.models import (UserProfileInfo,
                             highlight,
                             ActiveSales,
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
        fields = ('__all__')
#'Fname', 'Lname', 'd_Street1', 'd_Street2', 'd_City', 'd_State', 'd_Zip', 'Phone',
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
class ActiveSalesForm(forms.ModelForm):
    class Meta():
        model = ActiveSales
        fields = ('__all__')
        widgets = {
                    'batch':forms.TextInput(attrs= {'class': 'textinputclass'}),
                    # 'active': forms.BooleanField(),
                    # 'start_sales':forms.DateField(),
                    # 'end_sales': forms.DateField(),
                    'units': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    # 'soldout': forms.BooleanField(),
                    # 'bakingdate': forms.DateField(),
                    # 'deliverydate': forms.DateField(),
                    # 'bakingtime': forms.TimeField(),
                    'Plain_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'Sesame_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'Salt_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'Onion_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'Poppy_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'Garlic_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'Everything_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'RandomBake': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea feature-content'}),
                    'RandomBake_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'CreamCheese_sold': forms.NumberInput(attrs= {'class': 'textinputclass-sm'}),
                    'Batch_Notes': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea feature-content'})
        }
