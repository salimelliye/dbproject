from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import *

class CustomLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name','username','email','password1','password2']

class CreateRideForm(forms.Form):
    tripName = forms.CharField(
        label='Trip Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Trip Name'}),
        required=True
    )
    date = forms.DateField(
        label='Date',
        required=True
    )
    time = forms.TimeField(
        label='Departure Time',
        required=True
    )
    images = forms.ImageField(
        label='Images',
        widget=forms.FileInput(attrs={'accept': 'image/*', 'multiple': False}),
        required=False
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'placeholder': 'Enter Trip Description'}),
        required=True
    )
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Trip Location'}),
        required=True
    )
    participants = forms.CharField(
        label='Participants',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Participants'}),
        required=True
    )
    car = forms.ChoiceField(
        label='Choose a Car',
        choices=[('car1', 'Car 1'), ('car2', 'Car 2'), ('car3', 'Car 3')],
        required=True
    )    

