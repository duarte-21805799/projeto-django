#  website/urls.py

from django.shortcuts import render
from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('segundo', views.segundo_page_view, name='segundo'),
    path('terceiro', views.terceiro_page_view, name='terceiro'),
    path('layouts', views.layouts_page_view, name='layouts'),
    path('multimedia', views.multimedia_page_view, name='multimedia'),
    path('inventario', views.inventario_page_view, name='inventario'),
    path('tecnicas', views.tecnicas_page_view, name='tecnicas')

]