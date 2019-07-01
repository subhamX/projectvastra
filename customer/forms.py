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
    comments = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = models.Collection
        fields = [
            'name',
            'phone',
            'email',
            'location',
            'comments',
        ]