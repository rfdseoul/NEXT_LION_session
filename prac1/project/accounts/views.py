from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        found_user = User.objects.filter(username=username)

        if len(found_user):
            error = "아이디가 이미 존재합니다."
            return render(request, 'accounts/signup.html', {
                'error':error,
            })
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect('post:home')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('post:home')
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(request, 'accounts/login.html', {
            'error':error,
        })
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)

    return redirect('post:home')