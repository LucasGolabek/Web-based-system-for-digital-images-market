from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

@login_required(login_url='login')
def mainpage(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'marketplace/mainpage.html', context)


@login_required(login_url='login')
def buy(request):
    context = {}
    return render(request, 'marketplace/buy.html', context)


@login_required(login_url='login')
def active(request):
    context = {}
    return render(request, 'marketplace/active_offers.html', context)


@login_required(login_url='login')
def create(request):
    context = {}
    return render(request, 'marketplace/createoffer.html', context)


@login_required(login_url='login')
def product(request):
    context = {}
    return render(request, 'marketplace/product_site.html', context)


@login_required(login_url='login')
def messages(request):
    context = {}
    return render(request, 'marketplace/messages.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('mainpage')
            else:
                messages.info(request, "Niepoprawne dane")

        context = {}
        return render(request, 'marketplace/login_page.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Konto zostało stworzone dla " + user)
                return redirect('login')
            else:
                messages.info(request, "Nie udało się stworzyć konta")
        context = {'form': form}
        return render(request, 'marketplace/register.html', context)


def logout_page(request):
    logout(request)
    return redirect('mainpage')
