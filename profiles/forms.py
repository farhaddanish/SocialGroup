from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Profile
from django.contrib.auth.forms import UserChangeForm,UserCreationForm



class Profiles_forms (UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']





        
    