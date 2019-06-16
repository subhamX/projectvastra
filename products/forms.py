from django import forms
from products import models

class AddProduct(forms.ModelForm):
    name = forms.CharField(max_length=30, label='Name:')
    price = forms.IntegerField(label='Price:')
    img = forms.ImageField(label='Product Image:')
    quantity = forms.IntegerField(label='Quantity Available:')
    class Meta:
        model = models.Product
        fields = [
            'name',
            'price',
            'img',
            'quantity',
        ]