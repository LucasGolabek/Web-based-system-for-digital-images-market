from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, AddImageForm, BuyoutProposalForm, EditForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

@login_required(login_url='login')
def mainpage(request):
    username = request.user.username
    products = Product.objects.all()
    recived_offers = len(Messages.objects.filter(user_to=username))
    sended_offers = len(Messages.objects.filter(user_from=username))
    active_number = len(products)
    context = {'products': products,
               'page_name': 'mainpage',
               'recived_offers': recived_offers,
               'sended_offers': sended_offers,
               'active_number': active_number}
    return render(request, 'marketplace/mainpage.html', context)


@login_required(login_url='login')
def active(request):
    username = request.user.username
    recived_offers = len(Messages.objects.filter(user_to=username))
    sended_offers = len(Messages.objects.filter(user_from=username))
    actives = Product.objects.filter(username=username)
    active_number = len(actives)

    context = {'actives': actives,
               'page_name': 'active',
               'recived_offers': recived_offers,
               'sended_offers': sended_offers,
               'active_number': active_number}
    return render(request, 'marketplace/active_offers.html', context)


@login_required(login_url='login')
def message_page(request):
    username = request.user.username
    recived_offers = len(Messages.objects.filter(user_to=username))
    sended_offers = len(Messages.objects.filter(user_from=username))
    offers = Messages.objects.filter(user_to=username)
    context = {'offers': offers,
               'page_name': 'messages',
               'recived_offers': recived_offers,
               'sended_offers': sended_offers}
    return render(request, 'marketplace/messages.html', context)


@login_required(login_url='login')
def made_offers(request):
    username = request.user.username
    recived_offers = len(Messages.objects.filter(user_to=username))
    sended_offers = len(Messages.objects.filter(user_from=username))
    username = request.user.username
    offers = Messages.objects.filter(user_from=username)
    context = {'offers': offers,
               'page_name': 'madeoffers',
               'recived_offers': recived_offers,
               'sended_offers': sended_offers}
    return render(request, 'marketplace/made_offers.html', context)


@login_required(login_url='login')
def delete_photo(request, id):
    photo = get_object_or_404(Product, pk=id)
    photo_name = photo.name
    if request.method == "POST":
        photo.delete()
        return redirect('mainpage')
    context = {
        'object': photo_name,
        'page_name': 'delete'
    }
    return render(request, 'marketplace/delete.html', context)


@login_required(login_url='login')
def delete_message(request, id):
    message = get_object_or_404(Messages, pk=id)
    message_id = message.message_id
    if request.method == "POST":
        message.delete()
        return redirect('mainpage')
    context = {
        'object': message_id,
        'page_name': 'delete_message'
    }
    return render(request, 'marketplace/delete.html', context)


@login_required(login_url='login')
def decline_message(request, id):
    message = get_object_or_404(Messages, pk=id)
    if request.method == "POST":
        message.negotiation_status = 'Odrzucona'
        message.save()
        return redirect('active')
    context = {
        'page_name': 'decline',
        'message': message
    }
    return render(request, 'marketplace/decline.html', context)


@login_required(login_url='login')
def edit(request, id):
    photo = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        edit_form = EditForm(request.POST, instance=photo)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Twoja oferta została edytowane')
        else:
            messages.error(request, 'Nie udało się edytować oferty')
    initial = {'name': photo.name, 'price': photo.price, 'usage': photo.usage, 'description': photo.description}
    edit_form = EditForm(initial=initial)
    context = {'edit_form': edit_form}
    return render(request, 'marketplace/editphoto.html', context)


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
    username = request.user.username
    recived_offers = len(Messages.objects.filter(user_to=username))
    sended_offers = len(Messages.objects.filter(user_from=username))
    if request.method == "POST":
        image_form = AddImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
            messages.success(request, 'Twoje zdjęcie zostało dodane')
        else:
            messages.error(request, 'Nie udało się dodać zdjęcia')
    initial = {'username': request.user.username}
    image_form = AddImageForm(initial=initial)
    context = {'image_form': image_form,
               'page_name': 'create',
               'recived_offers': recived_offers,
               'sended_offers': sended_offers}
    return render(request, 'marketplace/createoffer.html', context)


@login_required(login_url='login')
def buy(request, id):
    product = get_object_or_404(Product, pk=id)

    photo_id = product.photo_id
    photo_owner = product.username

    initial = {'user_from': request.user.username,
               'user_to': photo_owner,
               'photo_id': photo_id}
    message_form = BuyoutProposalForm(initial=initial)

    context = {'message_form': message_form,
               'product': product,
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
def counteroffer(request, id):
    offer = get_object_or_404(Messages, pk=id)

    message_to = offer.user_from
    photo_id = offer.photo_id.photo_id
    print(offer.photo_id)

    initial = {'user_from': request.user.username,
               'user_to': message_to,
               'photo_id': photo_id}
    message_form = BuyoutProposalForm(initial=initial)

    context = {'message_form': message_form,
               'offer': offer,
               'photo_id': photo_id}
    if request.method == "POST":
        message_form = BuyoutProposalForm(request.POST, request.FILES)
        if message_form.is_valid():
            offer.negotiation_status = 'Kontroferta'
            offer.delete()
            message_form.save()
            messages.success(request, 'Wysłano wiadomość')
        else:
            messages.error(request, 'Nie udało się wysłac wiadomości')

    return render(request, 'marketplace/counteroffer.html', context)


@login_required(login_url='login')
def product_site(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {'product': product}
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
