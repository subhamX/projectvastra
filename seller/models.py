from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entrepreneur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=200, default=None, null=True, blank=True)
    display_pic = models.ImageField(default=None)
    desc = models.CharField(max_length=200, default=None, null=True, blank=True)
    def __str__(self):
        return self.user.first_name


class NewSeller(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.IntegerField()
    why = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name