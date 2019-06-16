from django.shortcuts import render


def errorHandler(request):
    return render(request, 'error.html')