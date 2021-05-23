from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime


def home_page_view(request):
    return render(request, 'website/home.html', {
        'data': datetime.date.today()
    })


def base_page_view(request):
    return render(request, 'website/base.html', {
        'data': datetime.date.today()
    })


def segundo_page_view(request):
    return render(request, 'website/segundo.html', {
        'data': datetime.date.today()
    })


def terceiro_page_view(request):
    return render(request, 'website/terceiro.html', {
        'data': datetime.date.today()
    })
