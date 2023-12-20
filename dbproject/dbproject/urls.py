"""dbproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing , name='landing'),
    path('signupUser/', views.sign_up_user, name='signupUser'),
    path('signupOrg/', views.sign_up_org, name='signupOrg'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('createTrip/', views.create_trip, name='createTrip'),
    path('createBranch/', views.create_branch, name='createBranch'),
    path('myTrips/', views.my_trips, name='myTrips'),
    path('tripDetails/<str:trip_id>/', views.trip_details, name="tripDetails"),
    path('profile/', views.user_profile, name='userProfile'),
    path('feed/', views.feed, name='feed'),
    path('createCar/', views.create_car, name='createCar'),

    #Authentication
    path('signupuser/', views.save_person, name='signupuser'),
    path('signupOrg/', views.save_org, name='signupOrg'),
    path('check-email-availability/', views.check_email_availability, name='check-email-availability'),
    
    # Add friends list url + template 
    # Add view for bookmarked trips
    # Add view for vehicles
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)