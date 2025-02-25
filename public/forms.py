from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Buyer

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Buyer
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']