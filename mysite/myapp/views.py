from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, AddImageForm, BuyoutProposalForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q


# Create your views here.

@login_required(login_url='login')
def mainpage(request):
    products = Product.objects.all()
    context = {'products': products,
               'page_name': 'mainpage'}
    return render(request, 'marketplace/mainpage.html', context)


@login_required(login_url='login')
def active(request):
    username = request.user.username
    actives = Product.objects.filter(username=username)

    if len(actives) < 3:
        context = {'actives': actives,
                   'page_name': 'active'}
        return render(request, 'marketplace/active_offers2.html', context)
    else:
        context = {'actives': actives,
                   'page_name': 'active'}
        return render(request, 'marketplace/active_offers.html', context)


@login_required(login_url='login')
def message_page(request, id):
    username = request.user.username
    photo = get_object_or_404(Product, pk=id)
    offers = Messages.objects.filter(user_to=username, photo_id=photo, negotiation_status='Oczekująca')
    photo_usage = photo.usage
    context = {'offers': offers,
               'usage':photo_usage}
    return render(request, 'marketplace/messages.html', context)

@login_required(login_url='login')
def made_offers(request):
    username = request.user.username
    offers = Messages.objects.filter(user_from=username)

    context = {'offers': offers}
    return render(request, 'marketplace/made_offers.html', context)


@login_required(login_url='login')
def delete_photo(request, id):
    photo = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        photo.delete()
        return redirect('mainpage')
    context = {
        'photo': photo,
        'page_name': 'delete'
    }
    return render(request, 'marketplace/delete.html', context)


@login_required(login_url='login')
def decline_message(request, id):
    message = get_object_or_404(Messages, pk=id)
    if request.method == "POST":
        print('poscik')
        message.negotiation_status = 'Odrzucona'
        message.save()
        return redirect('active')
    context = {
        'page_name': 'decline',
        'message': message
    }
    return render(request, 'marketplace/decline.html', context)



@login_required(login_url='login')
def accept_message(request, id):
    message = get_object_or_404(Messages, pk=id)
    if request.method == "POST":
        print('poscik')
        message.negotiation_status = 'Zaakceptowana'
        message.save()
        return redirect('active')
    context = {
        'page_name': 'accepted',
        'message': message
    }
    return render(request, 'marketplace/accept.html', context)


@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        image_form = AddImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
            messages.success(request, 'Twoje zdjęcie zostało dodane')
        else:
            messages.error(request, 'Nie udało się dodać zdjęcia')
    initial = {'username': request.user.username}
    image_form = AddImageForm(initial=initial)
    context = {'image_form': image_form}
    return render(request, 'marketplace/createoffer.html', context)


@login_required(login_url='login')
def buy(request, id):
    product = get_object_or_404(Product, pk=id)

    photo_id = product.photo_id
    photo_owner = product.username
    photo_usage = product.usage

    if photo_usage == 'K':
        usage = 'Komercyjne'
    elif photo_usage == 'P':
        usage = 'Prywatne'
    else:
        usage = 'Komercyjne ograniczone'

    initial = {'user_from': request.user.username,
               'user_to': photo_owner,
               'photo_id': photo_id}
    message_form = BuyoutProposalForm(initial=initial)

    context = {'message_form': message_form,
               'product': product,
               'usage': usage,
               'photo_id': photo_id}
    if request.method == "POST":
        message_form = BuyoutProposalForm(request.POST, request.FILES)
        if message_form.is_valid():
            message_form.save()
            messages.success(request, 'Wysłano wiadomość')
        else:
            messages.error(request, 'Nie udało się wysłac wiadomości')

    return render(request, 'marketplace/buy.html', context)


@login_required(login_url='login')
def product_site(request, id):
    product = get_object_or_404(Product, pk=id)
    photo_usage = product.usage
    if photo_usage == 'K':
        usage = 'Komercyjne'
    elif photo_usage == 'P':
        usage = 'Prywatne'
    else:
        usage = 'Komercyjne ograniczone'

    context = {'product': product,
               'usage': usage}
    return render(request, 'marketplace/product_site.html', context)


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
