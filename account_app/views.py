from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from account_app.forms import LoginForm, SignUpForm, EditProfile


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home_app:home')


    else:
        form = LoginForm()

    return render(request, "account_app/login.html", {"form": form, })


def user_logout(request):
    logout(request)
    return redirect('home_app:home')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('home_app:home')
    else:
        form = SignUpForm()

    return render(request, "account_app/register.html", {'form': form})


def edit_profile(request):
    user = request.user
    form = EditProfile(instance=user)
    if request.method == "POST":
        form = EditProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()

    return render(request, "account_app/edit.html", {'form': form})
