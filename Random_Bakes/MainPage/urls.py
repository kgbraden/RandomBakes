from django.conf.urls import url
from django.urls import path
from MainPage import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('project/', views.projects, name = 'projects'),
    path('batch/', views.batch, name = 'batch'),
    path('about', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('license/', views.license, name = 'license'),
    path('sanitation/', views.sanitation, name = 'sanitation'),
    path('order/', views.order, name = 'order'),
    path('registration/', views.registration, name = 'registration'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TEMPLATE TAGGING
app_name = 'Baking'
