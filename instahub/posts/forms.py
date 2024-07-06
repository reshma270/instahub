# posts/forms.py

from django import forms
from .models import Post


# Form to handle post creation
class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "caption"]
