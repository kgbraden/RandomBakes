from django.conf.urls import url
from django.urls import path
from MainPage import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('project/', views.projects, name = 'projects'),
    path('batch/', views.batch, name = 'batch'),
    path('about', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('license/', views.license, name = 'license'),
    path('sanitation/', views.SanitationView.as_view(), name = 'sanitation'),
    path('order/', views.order, name = 'order'),
    path('registration/', views.registration, name = 'registration'),
    url(r'^user_login/$', views.user_login, name = 'user_login' ),
    url(r'^enter_batch/$', views.enterbatch, name = 'enter_batch' ),
    url(r'^thankyou/$', views.thankyou, name = 'thankyou' ),
    ] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TEMPLATE TAGGING
app_name = 'Baking'
