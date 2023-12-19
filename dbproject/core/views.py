import random
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import login as auth_login

# Create your views here.
lebanon_facts = [
    "Lebanon introduced the world to mezze, a delightful array of small dishes like hummus, tabbouleh, and falafel. Perfect for sharing.",
    "Lebanon is home to some of the oldest olive trees globally, with olive oil being a staple in Lebanese cuisine for thousands of years.",
    "You can explore the ancient ruins of Baalbek, where you'll find Roman temples so well-preserved, they make time travel feel possible.",
    "Lebanon boasts Jeita Grotto, a natural wonder featuring breathtaking limestone formations and an underground river.",
    "Lebanon is a linguistic playground; Arabic is official, but French and English are widely spoken, reflecting its diverse heritage.",
    "The coastal city of Byblos, one of the oldest continuously inhabited cities, showcases Lebanon's deep connection to Phoenician history.",
    "Indulge in Lebanese sweets like baklava and ma'amoul, where every bite is a burst of honey, nuts, and exquisite flavors.",
    "Have a sip on Lebanese coffee, a symbol of hospitality, served strong and often with a touch of cardamom.",
    "Lebanon's compact size allows you to ski in the morning in the mountain resorts and relax on the Mediterranean beaches in the afternoon.",
    "Visit the Cedar Forest, a UNESCO site, and stand among ancient cedar trees, some over a thousand years old, symbolizing Lebanon's endurance."
]


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
        "fun_fact": random.choice(lebanon_facts)
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

#Authentication
def save_person(request):
    form = CreateUserForm()
    if request.method == 'POST':
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')

        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower() 
            password = form.cleaned_data.get('password2')
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
            )
            user.first_name = form.cleaned_data['first_name'].lower().capitalize()
            user.last_name = form.cleaned_data['last_name'].lower().capitalize()
            user.save()

            person = Person.objects.create(
                user=user,
                gender=gender,
                dob=date_of_birth,
            )
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)  # Log in the user

                # Redirect the user to the home page
                return redirect('home')
            else:
                error_message = 'User authentication failed. Please try logging in.'
                messages.error(request, error_message)

        else:
            print('Form is not valid. Errors:')
            print(form.errors)

            for field in form:
                for error in field.errors:
                    if "A user with that username already exists." in error:
                        # Replace the generic error message with a custom one for the email field
                        form.add_error('email', forms.ValidationError(
                            'A user with this email already exists.'))

    context = {'form': form}
    return render(request, 'signupUser.html', context)

