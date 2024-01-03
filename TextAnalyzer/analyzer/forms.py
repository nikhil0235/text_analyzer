# analyzer/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    # Add any additional fields you want for user registration

    class Meta:
        model = User  # Assuming you have imported User model from django.contrib.auth.models
        fields = ['username', 'password1', 'password2']
