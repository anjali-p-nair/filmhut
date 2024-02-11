from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# models.py
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='gallery')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    user = models.ForeignKey(User,default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

