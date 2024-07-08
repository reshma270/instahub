from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "caption", "created_at", "total_likes")
    search_fields = ("author__username", "caption")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

    def total_likes(self, obj):
        return obj.likes.count()

    total_likes.short_description = "Likes"


admin.site.register(Post, PostAdmin)
