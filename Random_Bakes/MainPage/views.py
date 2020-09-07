from django.shortcuts import render
from MainPage.models import highlight
from MainPage.forms import UserForm, UserProfileInfoForm
# Create your views here.
def index(request):
    cover_content2 = highlight.objects.filter(title = "Order Bagels")[0]

    # cover_content ={'CoverTitle': "Order Bagels",
    #        'CoverText': "We produce 48 kettle-boiled, hand-rolled bagels every other week and deliver them to the Sacramento region on Sunday mornings. Sold in batches of four with the option of adding Sonoma Clover cream cheese to your order. You choose the toppings. Once we're sold out, that's it for the week!",
    #        'CoverPhoto': 'static\MainApp\Media\Bagels-two.jpg',
    #        'CoverAltText': 'Two Bagelss',
    #        'CoverButton': 'Order Now',
    #        'CoverButtonLink': 'order_bagels'
    #        }
    cover_content ={'CoverTitle': cover_content2.title,
           'CoverText': cover_content2.story,
           'CoverPhoto': cover_content2,
           'CoverAltText': cover_content2.photo_alt,
           'CoverButton': cover_content2.button,
           'CoverButtonLink': cover_content2.button_link
           }
    return render(request,'MainApp/index.html', context = cover_content)

def projects(request):
    return render(request,'MainApp/projects.html')

def batch(request):
    return render(request,'MainApp/batch.html')

def about(request):
    return render(request,'MainApp/about.html')

def contact(request):
    return render(request,'MainApp/contact.html')

def license(request):
    return render(request,'MainApp/license.html')

def sanitation(request):
    return render(request,'MainApp/sanitation.html')

def order(request):
    return render(request,'MainApp/order.html')

def registration(request):
    registered = False

    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'MainApp/registration.html',
                    {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered':  registered})
