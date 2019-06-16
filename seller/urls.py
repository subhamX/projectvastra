from django.urls import path
from seller import views

app_name = 'seller'

urlpatterns = [
    path('profiles/', views.profiles, name='profiles'),
    path('new/', views.newSeller, name='new'),
]
