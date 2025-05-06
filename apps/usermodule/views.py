from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm  # make sure your custom form is imported

def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return render(request, "users/message.html")
    else:
        form = SignUpForm()
    return render(request, "users/register.html", {"form": form})

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return render(request, "users/message.html")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logoutUser(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "users/message.html")
