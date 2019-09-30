from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return self.user.first_name

        
class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    query = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    class Meta:
        verbose_name = 'Collection Request'
    def __str__(self):
        return self.name

