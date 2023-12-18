from django.shortcuts import render

# Create your views here.


def landing(request, *args, **kwargs):
    context = {

    }
    return render(request, 'landing.html', context)

def sign_up_user(request, *args, **kwargs):
    context = {

    }
    return render(request, 'signupUser.html', context)

def sign_up_org(request, *args, **kwargs):
    context = {

    }
    return render(request, 'signupOrg.html', context)

def login(request, *args, **kwargs):
    context = {

    }
    return render(request, 'login.html', context)

def home(request, *args, **kwargs):
    context = {

    }
    return render(request, 'home.html', context)


def create_trip(request, *args, **kwargs):
    context = {

    }
    return render(request, 'createTrip.html', context)

def my_trips(request, *args, **kwargs):
    context = {

    }
    return render(request, 'myTrips.html', context)

def trip_details(request, *args, **kwargs):
    context = {

    }
    return render(request, 'tripDetails.html', context)

def user_profile(request, *args, **kwargs):
    context = {

    }
    return render(request, 'profile.html', context)   

def feed(request, *args, **kwargs):
    context = {

    }
    return render(request, 'feed.html', context)   