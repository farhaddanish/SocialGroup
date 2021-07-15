import json
from profiles.views import profiles
from profiles.models import Profile
from posts.models import Posts
from django.db.models.query import RawQuerySet
from groupapp.models import Group
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import PostCreationForm
# Create your views here.


def createPost_ajax(request, id):

    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        group = Group.objects.get(id=id)
        form = PostCreationForm(
            Byuser=request.user, group=group, profile=profile, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:

        form = PostCreationForm()
        return render(request, 'createPost.html', {
            'form': form
        })


def seePosts(request, id):
    group = Group.objects.get(id=id)
    post = Posts.objects.filter(group=group)
    

    return render(request, 'allPostGroup.html', {
        'posts': post
    })


def postFromYou(request):
    post = Posts.objects.filter(Byuser=request.user)
    return render(request,'postbyMe.html',{
        'posts' :post
    })


def  delete (request):
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        post = Posts.objects.get(id=id)
        post.delete()
        return JsonResponse({
            'deleted' :True
        })
