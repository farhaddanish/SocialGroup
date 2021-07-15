from django.contrib.auth import models
from django.forms import fields
from .models import Posts
from django import forms




class PostCreationForm (forms.ModelForm):
    def __init__(self,*args, **kwargs):
        self.Byuser = kwargs.pop('Byuser',None)
        self.group = kwargs.pop('group',None)
        self.profile = kwargs.pop('profile',None)
        super(PostCreationForm,self).__init__(*args,**kwargs)


    def save(self,force_insert=False,force_update=False,commit=True):
        obj = super(PostCreationForm,self).save(commit=False)
        obj.Byuser = self.Byuser
        obj.group = self.group
        obj.profile = self.profile


        if commit:
            obj.save()
        return obj

    class Meta:
        model = Posts
        fields =['text']