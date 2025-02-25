from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdminUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = AdminUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']