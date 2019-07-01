from django import forms
from seller import models


class NewSellerForm(forms.ModelForm):
    why = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = models.NewSeller
        fields = [
            'name',
            'phone',
            'why',
            'location',
        ]

