from django.conf.urls import url
from django.urls import path
from Recipes import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [

    # path('batch_enter/', views.BatchCreateView.as_view(), name = 'batch_enter'),
    # path('batch/', views.batch_enter, name = 'batch'),
    # path('contact/', views.contact, name = 'contact'),
    # path('license/', views.LicenseListView.as_view(), name = 'license'),
    # path('Recipe/success/', views.recipe_success, name = 'recipe_success'),
    # # path('sanitation/', views.SanitationListView.as_view(), name = 'sanitation'),
    # path('order/', views.order, name = 'order'),
    # path('registration/', views.registration, name = 'registration'),
    # url(r'^user_login/$', views.user_login, name = 'user_login' ),
    # url(r'^enter_batch/$', views.enterbatch, name = 'enter_batch' ),
    # url(r'^thankyou/$', views.thankyou, name = 'thankyou' ),
    # url(r'^about/$', views.AboutUsListView.as_view(), name ='about'),
    # url(r'^featurette/(?P<pk>\d+)$', views.FeaturetteDetailView.as_view(), name = 'featurette_detail'),
    # url(r'^featurette/list/$', views.FeaturetteListView.as_view(), name='featurette_list'),
    # url(r'^featurette/new/$', views.FeaturetteCreateView.as_view(), name='featurette_new'),
    # url(r'^featurette/(?P<pk>\d+)/edit/$', views.FeaturetteUpdateView.as_view(), name='featurette_update'),
    # url(r'^featurette/(?P<pk>\d+)/remove/$', views.FeaturetteDeleteView.as_view(), name='featurette_remove'),
    ] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TEMPLATE TAGGING
app_name = 'Recipes'
