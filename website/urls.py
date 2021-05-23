#  hello/urls.py

from django.shortcuts import render
from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path('base', views.home_page_view, name='base'),
    path('home', views.home_page_view, name='home'),
    path('segundo', views.home_page_view, name='segundo'),
    path('terceiro', views.home_page_view, name='terceiro')

]