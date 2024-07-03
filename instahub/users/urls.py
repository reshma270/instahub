# users/urls.py

from django.urls import path
from .views import (
    CustomPasswordChangeView,
    follow_user,
    register,
    profile,
    custom_logout,
    edit_profile,
    unfollow_user,
    view_profile,
    search_users,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "register/",
        register,
        name="register",
    ),
    path("profile/", profile, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", custom_logout, name="logout"),  # Use the custom logout view,
    path(
        "password_change/", CustomPasswordChangeView.as_view(), name="password_change"
    ),  # URL for changing password
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),  # URL for success message
    path("search/", search_users, name="search_users"),  # URL fr searching users
    path(
        "follow/<str:username>/", follow_user, name="follow_user"
    ),  # URL for following users
    path(
        "unfollow/<str:username>/", unfollow_user, name="unfollow_user"
    ),  # URL for unfollowing users
    path(
        "profile/<str:username>/", view_profile, name="view_profile"
    ),  # URL for viewing other users' profiles
]
