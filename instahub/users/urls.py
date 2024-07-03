# users/urls.py

from django.urls import path
from .views import (
    CustomPasswordCHangeView,
    register,
    profile,
    custom_logout,
    edit_profile,
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
        "password_change/", CustomPasswordCHangeView.as_view(), name="password_change"
    ),  # URL for changing password
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),  # URL for success message
]
