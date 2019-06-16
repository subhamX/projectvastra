from cart import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('checkout/', views.home, name='checkout'),
    path('add/<int:id>/', views.addToCart, name='addToCart'),
]
