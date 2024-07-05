from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Creating a new UserProfile that inherits from AbstractUser
class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )  # Many-to-many field for following users

    def __str__(self):
        return self.username

    def followers_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()
