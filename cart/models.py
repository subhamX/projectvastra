from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class CartItem(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.prod.name