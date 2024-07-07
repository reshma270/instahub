# posts/models.py

from django.db import models
from users.models import UserProfile


# Create your models here.
# Post model with fields for an image, caption, and the author.
class Post(models.Model):
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="posts"
    )  # A foreign key to UserProfile model, indicating the user who created the post
    image = models.ImageField(upload_to="posts/")
    caption = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # A datetime field to automatically set the time when the post is created.
    likes = models.ManyToManyField(UserProfile, related_name="liked_posts", blank=True)

    def __str__(self):
        return f"{self.author.username}'s post"

    def total_likes(self):
        return self.likes.count()
