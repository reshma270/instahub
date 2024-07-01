# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


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


@login_required
def profile(request):
    return render(request, "users/profile.html")


def custom_logout(request):
    logout(request)
    return redirect("login")
