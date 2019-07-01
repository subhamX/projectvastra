from django.shortcuts import render
from misc.funcart import getcartc
from seller import models
from misc.funcart import getcartc
from seller import forms
# Create your views here.


def profiles(request):
    if( request.user.is_authenticated ):
        cart_count = getcartc(request.user)
    else:
        cart_count = 0
    sellers = models.Entrepreneur.objects.all()
    context = {
        'cartc': cart_count,
        'sellers': sellers,
    }
    return render(request, 'seller/profiles.html', context)

def newSeller(request):
    if( request.user.is_authenticated ):
        cart_count = getcartc(request.user)
    else:
        cart_count = 0
    if( request.method == 'POST'):
        form = forms.NewSellerForm(request.POST)
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
                'form': forms.NewSellerForm(),
            }
            return render(request, 'seller/new.html', context)
    else:
        form = forms.NewSellerForm()
    context = {
        'cartc': cart_count,
        'form': form,

    }
    return render(request, 'seller/new.html', context)


