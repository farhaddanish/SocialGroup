import json
from typing import FrozenSet
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Group
# Create your views here.
from .forms import GroupCreationForm
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        group = Group.objects.filter(member=request.user)
        return render(request, 'index.html', {
            'group':    group,
        })
    else:
        return render(request, 'index.html', {})


def creategroup(request):
    if request.method == 'POST':
        form = GroupCreationForm(admin =request.user  ,data=request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/Allgroups/')

    else:
        form = GroupCreationForm()

    return render(request, 'creategroup.html', {
        'form': form
    })


def AllGroups(request):
    group = Group.objects.all()
    return render(request, 'Allgroup.html', {
        'Allgroup': group
    })



def join_ajax (request):
    if request.is_ajax() and request.method =='POST':
        id= request.POST['id']
        group = Group.objects.get(id= id)
        join =False
        count = group.member.all().count()
        if request.user in group.member.all():
            group.member.remove(request.user)
            join =False
            count -=1
        else:
            group.member.add(request.user)
            join =True
            count +=1

        return JsonResponse({
            'join' :join,
            'count' :count
        })


def delete_ajax (request):
    if request.is_ajax() and request.method == 'POST':
        id  =  request.POST['id']
        group = Group.objects.get(id=id)
        group.delete()

        return JsonResponse({
            'deleted' : True
        })
