#  website/urls.py

from django.shortcuts import render
from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('', views.base_page_view, name='base'),
    path('', views.segundo_page_view, name='segundo'),
    path('', views.terceiro_page_view, name='terceiro')

]