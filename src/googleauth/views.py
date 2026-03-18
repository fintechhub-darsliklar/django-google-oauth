from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    return render(request, 'index.html')
    

def login_page(request):
    errors = ""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index') 
        errors = form.errors
    forms = AuthenticationForm()
    return render(request, 'login.html', context={"userform": forms, "errors": errors})


def register_page(request):
    errors = ""
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        errors = form.errors
    form = UserForm()
    return render(request, 'register.html', {"form": form, "errors": errors})


def logout_page(request):
    logout(request)
    return redirect("login_page")