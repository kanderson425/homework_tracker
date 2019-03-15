from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    is_instructor = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
