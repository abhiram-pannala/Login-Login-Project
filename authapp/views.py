from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def movies(request):
    return render(request, 'movies.html')


def registerUser(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render (request, 'register.html', {'form': form})


def webseries(request):
    return render(request, 'webseries.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username Or Password Is Incorrect')
        else:
            messages.error(request, 'Fill Out All The Fields')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return render(request, 'logout.html')


def faq(request):
    return render(request, 'faq.html')

def sports(request):
    return render (request, 'sports.html')
    

def contact(request):
    return render(request, 'contact.html')


def NANAoffical(request):
    return render(request, 'NANAoffical.html')