# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


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
    return render(request, "users/profile.html")


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
class CustomPasswordCHangeView(auth_views.PasswordChangeView):
    template_name = (
        "users/change_password.html"  # Template for rendering the change password form
    )
    success_url = reverse_lazy(
        "password_change_done"
    )  # URL to redirect to after successful password change


# Custom logout view to handle user logout
def custom_logout(request):
    logout(request)
    return redirect("login")
