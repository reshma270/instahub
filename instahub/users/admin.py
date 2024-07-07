# users/admin.py

from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = ["username", "email", "is_staff", "is_active"]
    list_filter = ["is_staff", "is_active"]
    fieldsets = (
        ("User Details", {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email", "bio", "profile_picture")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
    search_fields = ["username", "email"]
    ordering = ["username"]


admin.site.register(UserProfile, UserProfileAdmin)
