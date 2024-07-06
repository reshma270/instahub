# users/views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from posts.models import Post
from .models import UserProfile
from .forms import UserRegisterForm, UserSearchForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

# from django.http import HttpResponse
# from django.conf import settings
# def debug_view(request):
#     return HttpResponse(f"Redirect URL: {settings.LOGIN_REDIRECT_URL}")


# Create your views here.


# Define the register view function
def register(request):
    if request.method == "POST":  # Check if the request method is POST
        form = UserRegisterForm(
            request.POST, request.FILES
        )  # Create a form instance with POST data and files
        if form.is_valid():  # Validate the form
            user = form.save()  # Save the form and create a new user
            login(request, user)  # Log in the new user
            return redirect("profile")  # Redirect to the profile page

    else:
        form = (
            UserRegisterForm()
        )  # Create a new blank form if the request method is not POST
    return render(
        request, "users/register.html", {"form": form}
    )  # Render the registration template with the form


# View for displaying the user's profile
@login_required
def profile(request):
    user_posts = Post.objects.filter(
        author=request.user
    )  # Fetch posts for the logged-in user
    return render(request, "users/profile.html", {"user_posts": user_posts})


# View for editing profile information
@login_required
def edit_profile(request):
    if request.method == "POST":  # Check if the request is POST
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():  # Validate the form
            form.save()  # Save the updated user info
            return redirect("profile")  # redirect to profile page
    else:
        form = UserUpdateForm(
            instance=request.user
        )  # Create a form instance with current user data
    return render(
        request, "users/edit_profile.html", {"form": form}
    )  # Render the edit profile template


# Custom password change view to use our own template and redirect on success
class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = (
        "users/change_password.html"  # Template for rendering the change password form
    )
    success_url = reverse_lazy(
        "password_change_done"
    )  # URL to redirect to after successful password change


# Searching for users ny username
@login_required
def search_users(request):
    form = UserSearchForm()
    results = []
    if request.method == "GET":
        form = UserSearchForm(request.GET)
        if form.is_valid():
            username = form.cleaned_data["username"]
            results = UserProfile.objects.filter(
                username__icontains=username
            )  # Search users by username
    return render(request, "users/search.html", {"form": form, "results": results})


# Following users
@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(UserProfile, username=username)
    request.user.following.add(user_to_follow)
    return redirect("view_profile", username=username)


# Unfollow users
@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(UserProfile, username=username)
    request.user.following.remove(user_to_unfollow)
    return redirect("view_profile", username=username)


@login_required
def view_profile(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)
    return render(request, "users/view_profile.html", {"user": user_profile})


@login_required
def followers_list(request, username):
    if request.user.username != username:
        return redirect(
            "profile"
        )  # Redirect to own profile if trying to access others' lists
    user_profile = get_object_or_404(UserProfile, username=username)
    followers = user_profile.followers.all()
    referrer = request.META.get("HTTP_REFERER", "")  # Get the referring URL
    return render(
        request,
        "users/followers_list.html",
        {"user_profile": user_profile, "followers": followers, "referrer": referrer},
    )


@login_required
def following_list(request, username):
    if request.user.username != username:
        return redirect("profile")
    user_profile = get_object_or_404(UserProfile, username=username)
    following = user_profile.following.all()
    referrer = request.META.get("HTTP_REFERER", "")  # Get the referring URL
    return render(
        request,
        "users/following_list.html",
        {"user_profile": user_profile, "following": following, "referrer": referrer},
    )


# Custom logout view to handle user logout
def custom_logout(request):
    logout(request)
    return redirect("login")
