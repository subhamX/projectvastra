from django.contrib import admin
from django.urls import path
from customer import views

app_name = 'customer'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('collection/', views.collection, name='collectionDrive'),
    path('contactus/', views.contactus, name='generalContact'),
]
