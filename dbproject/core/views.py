from django.shortcuts import render

# Create your views here.


def home(request, *args, **kwargs):
    context = {

    }
    return render(request, 'home.html', context)

def sign_up(request, *args, **kwargs):
    context = {

    }
    return render(request, 'signup.html', context)

def login(request, *args, **kwargs):
    context = {

    }
    return render(request, 'login.html', context)