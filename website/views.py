# Create your views here.
from django.shortcuts import render
from . import views
import datetime

app_name = "website"


def home_page_view(request):
    return render(request, 'website/home.html')


def segundo_page_view(request):
    return render(request, 'website/segundo.html')


def terceiro_page_view(request):
    return render(request, 'website/terceiro.html')
