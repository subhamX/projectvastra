from django.db import models
from seller.models import Entrepreneur
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=None)
    img = models.ImageField(default=None)
    entrpr = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=None)

    def __str__(self):
        return self.name
        