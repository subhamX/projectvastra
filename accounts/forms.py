from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password:', 
        widget=forms.PasswordInput(attrs={
        })
    )
    password2 = forms.CharField(
        label='Password Confirmation:', 
        widget=forms.PasswordInput(attrs={
        })
    )
    username = forms.CharField(
        label='Username:',
        widget=forms.TextInput(attrs={
            'autofocus': None
        })
    )
    first_name = forms.CharField(
        label='First Name:',
        widget=forms.TextInput(attrs={
            'autofocus': 'autofocus'
        })
    )
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput())