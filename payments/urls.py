from django.urls import path
from payments import views

app_name = 'payments'

urlpatterns = [
    path('sorry/', views.sorry, name='sorry')
]