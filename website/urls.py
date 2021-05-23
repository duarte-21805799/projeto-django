#  hello/urls.py

from django.shortcuts import render
from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('base', views.base_page_view, name='base'),
    path('segundo', views.segundo_page_view, name='segundo'),
    path('terceiro', views.terceiro_page_view, name='terceiro')

]