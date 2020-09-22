from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from Recipes.models import baking_batch
from Recipes.forms import (BakingBatchForm, IngredientForm)
                                # , ShapingFinisihingForm,
#                             DoughForm, , fermIngredientForm, doughIngredientForm
#                             )
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse, reverse_lazy
# from django.contrib.auth.decorators import login_required
from django.views.generic import (View,
                                  TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
# from django.contrib.auth.mixins import LoginRequiredMixin
# from datetime import date, datetime
# Create your views here.
def recipe_success(request):
    return render(request,'MainPage/sucess.html')

class BatchCreateView(CreateView):
    form_class = BakingBatchForm
    model = baking_batch

# def batch_enter(request):
#     registered = False
#
#     if request.method =='POST':
#         Batch_form = BakingBatchForm(data=request.POST)
#         # Shaping_form = ShapingFinisihingForm(data=request.POST)
#         # Dough_form = DoughForm(data=request.POST)
#         # Ingredient_form = IngredientForm(data=request.POST)
#         # fIngred_form = fermIngredientForm(data=request.POST)
#         # dIngred_form = doughIngredientForm(data=request.POST)
#         # profile_form = UserProfileInfoForm(data=request.POST)
#
#         if Batch_form.is_valid() and Shaping_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             if 'profile_pic' in request.FILES:
#                 profile.profile_pic = request.FILES['profile_pic']
#             profile.save()
#             registered = True
#         else:
#             print(user_form.errors,profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileInfoForm()
#
#     return render(request,'Recipes/baking_batch_form.html', context =
#                     {'user_form': user_form,
#                     'profile_form': profile_form,
#                     'registered':  registered})
