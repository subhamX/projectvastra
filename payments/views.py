from django.shortcuts import render

# Create your views here.


def sorry(request):
    return render(request, 'payments/sorry.html')