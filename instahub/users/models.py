from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Creating a new UserProfile that inherits from AbstractUser
class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )

    def __str__(self):
        return self.username
