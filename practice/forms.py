from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    #To Extand fields
    email = forms.EmailField(help_text="Please enter your email")

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
    
