from django.shortcuts import render
from seller.models import Entrepreneur
from products.models import Product
from django.contrib.auth.models import User
from misc.funcart import getcartc
from customer import forms

# Create your views here.

def landing(request):
    if( request.user.is_authenticated ):
        cart_count = getcartc(request.user)
    else:
        cart_count = 0

    context = {
        'cartc': cart_count,
    }
    return render(request, 'customer/home.html', context)

def catalog(request):
    if( request.user.is_authenticated ):
        cart_count = getcartc(request.user)
    else:
        cart_count = 0

    products = Product.objects.all()
    context = {
        'products': products,
        'cartc': cart_count,
    }
    return render(request, 'customer/catalog.html', context)

def contactus(request):
    if( request.user.is_authenticated ):
        cart_count = getcartc(request.user)
    else:
        cart_count = 0
    if( request.method == 'POST'):
        form = forms.ContactUsForm(request.POST)
        if( form.is_valid() ):
            if( request.user.is_authenticated ):
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
            else:
                form.save()
            context = {
                'cartc': cart_count,
                'flag': 1,
                'form': forms.ContactUsForm(),
            }
            return render(request, 'customer/contactus.html', context)
    else:
        form = forms.ContactUsForm()
    context = {
        'cartc': cart_count,
        'form': form,

    }
    return render(request, 'customer/contactus.html', context)


def about(request):
    if( request.user.is_authenticated ):
        cart_count = getcartc(request.user)
    else:
        cart_count = 0
    context = {
        'cartc': cart_count,
    }
    return render(request, 'customer/about.html', context)


def collection(request):
    if( request.user.is_authenticated ):
        cart_count = getcartc(request.user)
    else:
        cart_count = 0
    if( request.method == 'POST'):
        form = forms.CollectionForm(request.POST)
        if( form.is_valid() ):
            if( request.user.is_authenticated ):
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
            else:
                form.save()
            context = {
                'cartc': cart_count,
                'flag': 1,
                'form': forms.CollectionForm(),
            }
            return render(request, 'customer/collection.html', context)
    else:
        form = forms.CollectionForm()
    context = {
        'cartc': cart_count,
        'form': form,

    }
    return render(request, 'customer/collection.html', context)