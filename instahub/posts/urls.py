# posts/urls.py

from django.urls import path
from .views import create_post, delete_post, edit_post, feed, like_post, unlike_post

urlpatterns = [
    path("create/", create_post, name="create_post"),
    path("edit/<int:post_id>/", edit_post, name="edit_post"),  # URL for editing posts
    path(
        "delete/<int:post_id>/", delete_post, name="delete_post"
    ),  # URL for deleting posts
    path("feed/", feed, name="feed"),  # URL for viewing the feed
    path("like/<int:post_id>/", like_post, name="like_post"),
    path("unlike/<int:post_id>/", unlike_post, name="unlike_post"),
]
