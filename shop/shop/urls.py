"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from views import index,logout,register,login
from restaurants.views import manage_information,manage_menu,manage_menu_data,new_menu,delete_menu
from trade.views import buyer_data,search,shop_info,menu

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^index/(\d{1,5})/$',index),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),

    url(r'^manage_info/$',manage_information),
    url(r'^manage_menu/$',manage_menu),
    url(r'^new_menu/$',new_menu),
    url(r'^manage_menu_data/(\d{1,5})/$',manage_menu_data),
    url(r'^delete_menu/(\d{1,5})/$',delete_menu),
    url(r'^buyer_data/$',buyer_data),
    url(r'^search/$',search),
    url(r'^shop_info/(\d{1,5})/$',shop_info),
    url(r'^menu/(\d{1,5})/$',menu),
]
