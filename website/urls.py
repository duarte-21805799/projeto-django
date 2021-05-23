#  website/urls.py

from django.shortcuts import render
from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('segundo', views.segundo_page_view, name='segundo'),
    path('terceiro', views.terceiro_page_view, name='terceiro')
]