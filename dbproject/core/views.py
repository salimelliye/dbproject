import random
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
lebanon_facts = [
    "Lebanon introduced the world to mezze, a delightful array of small dishes like hummus, tabbouleh, and falafel. Perfect for sharing.",
    "Lebanon is home to some of the oldest olive trees globally, with olive oil being a staple in Lebanese cuisine for thousands of years.",
    "You can explore the ancient ruins of Baalbek, where you'll find Roman temples so well-preserved, they make time travel feel possible.",
    "Lebanon boasts Jeita Grotto, a natural wonder featuring breathtaking limestone formations and an underground river.",
    "Lebanon is a linguistic playground; Arabic is official, but French and English are widely spoken, reflecting its diverse heritage.",
    "The coastal city of Byblos, one of the oldest continuously inhabited cities, showcases Lebanon's deep connection to Phoenician history.",
    "Indulge in Lebanese sweets like baklava and ma'amoul, where every bite is a burst of honey, nuts, and exquisite flavors.",
    "A sip on Lebanese coffee, a symbol of hospitality, is served strong and often with a touch of cardamom.",
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
        "fun_fact": random.choice(lebanon_facts)
    }
    return render(request, 'home.html', context)




def create_branch(request, *args, **kwargs):
    context = {

    }
    return render(request, 'createBranch.html', context)

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



def create_trip(request):
 if request.method == 'POST':
    logged_person = request.user.person
    my_cars = Vehicle.objects.filter(userID=logged_person).order_by('-plateNb')
    my_friends = Friend.objects.filter(personID=logged_person)
    userID = request.user.person
    orgID = request.POST.get('org_id')  
    plateNb = request.POST.get('plate_number')  
    ride_date = request.POST.get('ride_date') 
    nb_participants = request.POST.get('num_participants')  
    departure = request.POST.get('departure_location')
    ride_date = datetime.strptime(ride_date, '%Y-%m-%d %H:%M:%S')
    vehicle = get_object_or_404(Vehicle, plateNb=plateNb)
    organization = get_object_or_404(Organization, id=orgID)
    trip = Trip.objects.create(
            userID=userID,
            orgID=organization,
            plateNb=vehicle,
            rideDate=ride_date,
            nbParticipants=nb_participants,
            departure=departure,
            isCompleted=False,
            isFeatured=False,
            isBookmarked=False
        )
    participant_ids = request.POST.getlist('participant_ids')  
    if participant_ids:
            for participant_id in participant_ids:
                participant = Person.objects.get(pk=participant_id)
                trip.participants.add(participant)
    context={

        'my_cars' : my_cars,
        'my_friends' : my_friends
    }
    return render(request, 'createTrip.html', context)