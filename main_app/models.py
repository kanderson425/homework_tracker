from django import forms
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from .choices import USERTYPE_CHOICES, LOCATION_CHOICES, CLASSTYPE_CHOICES, DATE_CHOICES

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    usertype = models.CharField(max_length=200,choices=USERTYPE_CHOICES)
    location = models.CharField(max_length=200,choices=LOCATION_CHOICES)
    class_start_date = models.CharField(max_length=200,choices=DATE_CHOICES, default='Jan-2019')
    class_type = models.CharField(max_length=200, choices=CLASSTYPE_CHOICES)

    def __str__(self):
        return f'{self.user} Profile'

# class Instructor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
