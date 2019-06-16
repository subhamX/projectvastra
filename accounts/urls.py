from django.contrib import admin
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signUpView, name='signup'),
    path('login/', views.loginView, name='signin'),
    path('logout/', views.logoutView, name='logout'),
]
