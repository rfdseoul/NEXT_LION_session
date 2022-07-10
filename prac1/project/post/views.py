from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'post/home.html', {
        'posts':posts,
    })

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

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('post:home')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        found_user = User.objects.filter(username=username)

        if len(found_user):
            error = "아이디가 이미 존재합니다."
            return render(request, 'post/signup.html', {
                'error':error,
            })
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect('post:home')
    return render(request, 'post/signup.html')

def login(request):
    if request.method == "post":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(request, 'post/login.html', {
            'error':error,
        })
    return render(request, 'post/login.html')

def logout(request):
    auth.logout(request)

    return redirect('post:home')