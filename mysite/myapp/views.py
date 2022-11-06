from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def mainpage(request):
    context = {}
    return render(request, 'marketplace/mainpage.html', context)


def cart(request):
    context = {}
    return render(request, 'marketplace/buy.html', context)


def checkout(request):
    context = {}
    return render(request, 'marketplace/checkout.html', context)


def product(request):
    context = {}
    return render(request, 'marketplace/product_site.html', context)
