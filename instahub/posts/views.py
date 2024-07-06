# posts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm


# Create your views here.
# View to handle creation of new posts
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("profile")
    else:
        form = PostCreationForm()
    return render(request, "users/create_post.html", {"form": form})
