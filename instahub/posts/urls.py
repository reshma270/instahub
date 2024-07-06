# posts/urls.py

from django.urls import path
from .views import create_post, delete_post, edit_post, feed

urlpatterns = [
    path("create/", create_post, name="create_post"),
    path("edit/<int:post_id>/", edit_post, name="edit_post"),  # URL for editing posts
    path(
        "delete/<int:post_id>/", delete_post, name="delete_post"
    ),  # URL for deleting posts
    path("feed/", feed, name="feed"),  # URL for viewing the feed
]
