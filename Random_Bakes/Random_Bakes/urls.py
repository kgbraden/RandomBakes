"""Random_Bakes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from MainPage import views
from django.conf import settings
from django.conf.urls.static import static

# from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),
    path('projects/', views.projects, name = 'projects'),
    path('admin/', admin.site.urls),
    url(r'^logout/$', views.user_logout, name = 'logout'),
    url(r'^user_login/$', views.user_login, name = 'user_login' ),
    url(r'^Baking/', include('MainPage.urls')),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
