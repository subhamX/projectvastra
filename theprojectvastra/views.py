from django.shortcuts import render


def errorHandler(request, exception=None):
    return render(request, 'error.html')


def forDeveloper(request, exception=None):
    return render(request, 'main/developer.html')