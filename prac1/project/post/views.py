from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'post/home.html', {
        'posts':posts,
    })

@login_required
def new(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('post:home')
    return render(request, 'post/new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'post/detail.html', {
        'post':post,
    })

@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('post:detail', post_pk)
    return render(request, 'post/edit.html', {
        'post':post,
    })

@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('post:home')

