from django.shortcuts import render, reverse, get_object_or_404, redirect
from cart import models
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from misc.funcart import getcartc
from django.db.models import Sum
# Create your views here.

# @login_required(login_url='/accounts/login/')
def home(request):
    if(request.user.is_authenticated):
        cart_items = models.CartItem.objects.filter(user=request.user, bought=False)
        cart_count = getcartc(request.user)
        # k.aggregate(k = Sum('quantity')*Sum('prod__price'))
        sum=0
        for item in cart_items:
            sum = sum + item.quantity * item.prod.price
            print(sum)
        context = {
            'items': cart_items,
            'cartc': cart_count,
            'final_price': sum,
        }
    else:
        context = {
            'items': 0,
            'cartc': 0,
        }
    return render(request, 'cart/checkout.html', context)

@login_required(login_url='/accounts/login/')
def addToCart(request, id):
    if( not request.user.is_authenticated ):
        context = {
            'message':'',
        }
        return HttpResponseRedirect(reverse('accounts:signin'), context)
    product = get_object_or_404(Product, id=id)
    products = Product.objects.exclude(id=id)
    oldCartInstance = models.CartItem.objects.filter(prod=product, user=request.user, bought=False)
    if(oldCartInstance.count()):
        if(oldCartInstance[0].prod.quantity > oldCartInstance[0].quantity):
            oldCartInstance.update(quantity=oldCartInstance[0].quantity+1)
        else:
            cart_count = getcartc(request.user)
            context = {
                'product': product,
                'products': products,
                'cartc': cart_count,
            }
            return render(request, 'cart/cannotAdd.html', context)
    else:
        cartInstance = models.CartItem(prod=product, user=request.user)
        cartInstance.save()

    cart_count = getcartc(request.user)
    context = {
        'product': product,
        'products': products,
        'cartc': cart_count,
    }
    return render(request, 'cart/addToCart.html', context)

