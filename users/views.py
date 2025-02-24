from django.shortcuts import render,redirect
from users.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.urls import reverse 

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    
    if request.method == "POST":
        form = LoginForm(data = request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
    
            user = authenticate(username=username, password=password)

            if user:
                login(request,user)
                return render(request, "index.html")
            else:
                form.add_error(None, "해당 사용자가 존재하지 않습니다")

        context = {"form":form}
        return render(request, "users/login.html", context)
    
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)
    

def logout_view(request):
    logout(request)

    return redirect("/users/login/")