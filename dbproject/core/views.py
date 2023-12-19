from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
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



def user_login(request):
    context = {

    } 
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
          user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
          user = None

        if user is not None and user.check_password(password):
            if Person.objects.filter(user=user).exists():
                login(request, user)
                return redirect('home')
        else:
            error_message = 'Invalid email or password. Please try again.'
            messages.error(request, error_message)
    error_messages = messages.get_messages(request)
    context['error_messages'] = error_messages
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


def check_email_availability(request):
    if request.method == "GET":
        email = request.GET.get("email")
        # Check if the email already exists in the database
        if User.objects.filter(email=email).exists():
            response_data = {"exists": True}
        else:
            response_data = {"exists": False}
        return JsonResponse(response_data)