"""telrate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.admin import site

from android import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('android/login', views.login),
    path('android/logout', views.logout),
    path('android/sign', views.sign),
    path('android/getdou', views.getdou),
    path('android/saveinfo', views.getdou),
    path('android/getcell', views.getcell),
    path('android/duicell', views.duicell),
    path('android/cookies', views.cookiestest),
    url(r'^accounts/login/', site.login),


]
