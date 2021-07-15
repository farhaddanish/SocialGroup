from profiles.models import Profile

from django.db import models

from django.contrib.auth.models import User
from groupapp.models import Group
# Create your models here.


class Posts (models.Model):
    text = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    Byuser = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default="",null=True,blank=True)

    def __str__(self):
        return f'ByUser :     {self.Byuser}'
