from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Group (models.Model):
    name = models.CharField(max_length=50)
    describe = models.CharField(max_length=200)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="admin", null=True)
    date = models.DateTimeField(auto_now_add=True)
    member = models.ManyToManyField(User)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'name :   {self.name}   Date :  {self.date}'
