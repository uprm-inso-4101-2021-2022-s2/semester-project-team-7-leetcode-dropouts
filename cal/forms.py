from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class Profile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        labels = {"email": "E-Mail", "password":"Password","username":"Username"}