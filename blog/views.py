from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'blog/login.html')

def home(request):
    return render(request, "blog/home.html")
