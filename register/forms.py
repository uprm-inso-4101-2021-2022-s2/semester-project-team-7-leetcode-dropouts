from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createUserForm(UserCreationForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "password2"]