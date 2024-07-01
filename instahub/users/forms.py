# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


# Define the UserRegisterForm class, which extends the built-in UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Adding an email field to the form

    class Meta:
        model = UserProfile  # Specify the model to use for this form
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]  # Fields to include in the form
