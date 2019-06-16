# from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import User
from customer import models

class ContactUsForm(forms.ModelForm):
    query = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = models.ContactUs
        fields = [
            'name',
            'phone',
            'email',
            'query',
        ]



class CollectionForm(forms.ModelForm):
    query = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = models.Collection
        fields = [
            'name',
            'phone',
            'email',
            'location',
            'comments',
        ]

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=40)
#     password = forms.CharField(widget=forms.PasswordInput())


    # name = models.CharField(max_length=200)
    # query = models.CharField(max_length=200)
    # email = models.EmailField()
    # phone = models.IntegerField(max_length=10)



    #     name = models.CharField(max_length=200)
    # location = models.CharField(max_length=200)
    # comments = models.CharField(max_length=200)
    # email = models.EmailField()
    # phone = models.IntegerField(max_length=10)
    # user = models.ForeignKey(Us