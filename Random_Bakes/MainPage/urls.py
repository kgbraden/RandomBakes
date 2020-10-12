from django.urls import path
from django.conf.urls import url, include
from MainPage import views
# from Recipes import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('project/', views.ProjectListView.as_view(), name = 'projects'),
    path('shopping/', views.shopping, name = 'shopping'),
    # path('batch/', views.batch, name = 'batch'),
    path('contact/', views.contact, name = 'contact'),
    path('license/', views.LicenseListView.as_view(), name = 'license'),
    path('success/', views.success, name = 'success'),
    path('sanitation/', views.SanitationListView.as_view(), name = 'sanitation'),
    path('order/', views.order, name = 'order'),
    path('tickets/', views.OrdersListView.as_view(), name = 'tickets'),
    path('registration/', views.registration, name = 'registration'),
    path('orderplaced/', views.orderplaced, name = 'orderplaced'),
    url(r'^user_login/$', views.user_login, name = 'user_login' ),
    url(r'^enter_batch/$', views.enterbatch, name = 'enter_batch' ),
    url(r'^thankyou/$', views.thankyou, name = 'thankyou' ),
    url(r'^about/$', views.AboutUsListView.as_view(), name ='about'),
    url(r'^featurette/(?P<pk>\d+)$', views.FeaturetteDetailView.as_view(), name = 'featurette_detail'),
    url(r'^featurette/list/$', views.FeaturetteListView.as_view(), name='featurette_list'),
    url(r'^featurette/new/$', views.FeaturetteCreateView.as_view(), name='featurette_new'),
    url(r'^featurette/(?P<pk>\d+)/edit/$', views.FeaturetteUpdateView.as_view(), name='featurette_update'),
    url(r'^featurette/(?P<pk>\d+)/remove/$', views.FeaturetteDeleteView.as_view(), name='featurette_remove'),
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
    # url(r'^ActiveSales/(?P<batch>\d+)$', views.ActiveSalesDetailView.as_view(), name = 'ActiveSales_detail'),
    url(r'^ActiveSales/list/$', views.ActiveSalesListView.as_view(), name='ActiveSales_list'),
    url(r'^ActiveSales/new/$', views.ActiveSalesCreateView.as_view(), name='ActiveSales_new'),
    url(r'^ActiveSales/(?P<pk>\d+)/edit/$', views.ActiveSalesUpdateView.as_view(), name='ActiveSales_update'),
    url(r'^ActiveSales/(?P<pk>\d+)/remove/$', views.ActiveSalesDeleteView.as_view(), name='ActiveSales_remove'),
    # url(r'^Recipes/', include('Recipes.urls')),
    ] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TEMPLATE TAGGING
app_name = 'Baking'
