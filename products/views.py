from django.shortcuts import render, redirect
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from products import forms
from seller.models import Entrepreneur
from django.http import HttpResponse, Http404
from products import models
from misc.funcart import getcartc

@login_required(login_url='/accounts/login')
def addProduct(request):
    if( Profile.objects.get(user=request.user).is_customer ):
        return redirect('customer:landing')

    message = ''
    if( request.method == 'POST' ):
        form = forms.AddProduct(request.POST, request.FILES)
        if( form.is_valid() ):
            instance = form.save(commit=False)
            instance.entrpr = Entrepreneur.objects.get(user=request.user)
            instance.save()
            message = 'Product Added Successfully'
            form = forms.AddProduct()
    else:
        form = forms.AddProduct()

    context = {
        'message':message,
        'form' : form,
    }
    return render(request, 'products/addproducts.html', context)


def productDetail(request, id):
    product = models.Product.objects.filter(pk=id)
    if( request.user.is_authenticated ):
        cart_count = getcartc(request.user)
    else:
        cart_count = 0
    if(product.count()):
        context = {
            'product': product[0],
            'cartc': cart_count,
        }
    else:
        raise Http404("Product does not exist")
    return render(request, 'products/productDetail.html', context)