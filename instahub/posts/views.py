# posts/views.py

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm
from .models import Post


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
    return render(request, "posts/create_post.html", {"form": form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = PostCreationForm(instance=post)
    return render(request, "posts/edit_post.html", {"form": form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("profile")
    return render(request, "posts/delete_post.html", {"post": post})
