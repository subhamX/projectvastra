from django.shortcuts import render, reverse
from accounts import forms
from django.http import HttpResponseRedirect
from accounts import models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from customer.models import Customer

# Create your views here.
def signUpView(request):
    # Checking If the User is already Logged In
    if( request.user.is_authenticated ):
        checkAndRedirect(request.user)
    if( request.method == 'POST'):
        form = forms.SignUpForm(request.POST)
        if( form.is_valid() ):
            # print()
            instance = form.save(commit=False)
            # Only after instance is saved We can access id
            instance.save()

            # Creating Profile Instance for the new user
            profileInstance = models.Profile(user=instance)
            profileInstance.save()

            # Creating Customer Instance for the new user
            customerInstance = Customer(
                user = instance
            )
            customerInstance.save()

            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if( user ):
                login(request, user)
                return HttpResponseRedirect(reverse('customer:landing'))
    else:
        form = forms.SignUpForm()
    
    context = {
        'form': form,
        'cartc': 0,
    }
    return render(request, 'accounts/signup.html', context)


def checkAndRedirect(user):
    profileInstance = models.Profile.objects.get(user=user)
    if( profileInstance.is_customer == True):
        return HttpResponseRedirect(reverse('customer:landing'))
    else:
        return HttpResponseRedirect(reverse('products:addproduct'))


def loginView(request):
    # Checking If the User is already Logged In
    message = ''
    if( request.user.is_authenticated ):
        return checkAndRedirect(request.user)
    if( request.method == 'POST'):
        print(request.POST.get('next'))
        form = forms.LoginForm(request.POST)
        if( form.is_valid() ):
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if( user ):
                login(request, user)
                return checkAndRedirect(request.user)
            else:
                message = 'Invalid Username Or Password'
                
    context = {
        'form': forms.LoginForm(),
        'error_message': message,
        'cartc': 0,
    }
    return render(request, 'accounts/signin.html', context)



@login_required(login_url='/accounts/login/')
def logoutView(request):
    logout(request)
    context = {
        'cartc': 0,
    }
    return render(request, 'accounts/logout.html', context)