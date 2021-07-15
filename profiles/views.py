import json
from django import forms
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Profiles_forms
# Create your views here.
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, UserChangeForm
from django.contrib import messages
from .models import Profile
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize


def signUP(request):
    if request.method == 'POST':
        form = Profiles_forms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('sign successfully'))
            return HttpResponseRedirect('/login')
    else:
        form = Profiles_forms()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def LoginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = authenticate(request, username=username, password=password)
        if form is not None:
            login(request, form)
            messages.success(request, ("Login Scussefully"))
            return HttpResponseRedirect("/")
        else:
            messages.success(request, ("try again"))
            return HttpResponseRedirect("/login")

    else:
        return render(request, 'login.html')


def profiles(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        print(profile.image)
        context = {
            'image': profile.image,
            'bio': profile.bio
        }
        return render(request, 'profiles.html', context)

    else:
        return render(request, 'profiles.html', {
            'login': True
        })


def EditProfile(request):
    if request.method == 'POST':
        print(request.user)
        image = request.FILES['imagename']
        try:
            profile = Profile.objects.get(user = request.user)
        except:
            return HttpResponse('not user')
        profile.image = image
        profile.save()
        return HttpResponseRedirect('/profiles/')

    else:
        return render(request, 'editProfile.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'index.html')


def changePassword(request):
    if request.method == 'POST':
        print(request.POST)
        profile = Profile()
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return JsonResponse({
                'message': 'Your Messege have been changed',
            })
        else:

            return JsonResponse({
                'type': 'enter fields correctly'
            })
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change.html', {
        'form': form
    })


def changeName(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        alluser =  User.objects.all()
        form = User.objects.get(username=request.user)
        for i in alluser :
            if i.username == username:
                messages.success(request,('this user is alerdy there'))
                return HttpResponseRedirect('/profiles/')
            
        form.username = username
        form.save()
        messages.success(request, ('chnaged'))
        return HttpResponseRedirect('/profiles/')
    else:
        pass
        

    return render(request, 'userchange.html', {})
