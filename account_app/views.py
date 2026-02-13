from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None  :
            login(request, user)
            return redirect('home_app:home')
    return render(request, "account_app/login.html")

def user_logout(request):
    logout(request)
    return redirect('home_app:home')


def user_register(request):
    context = {"error":[]}
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            context["error"].append("Username already exists")
            return render(request, "account_app/register.html", context)
        if password1 != password2:
            context["error"].append("Passwords don't match")
            return render(request, "account_app/register.html", context)


        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home_app:home')
    return render(request,"account_app/register.html",{})