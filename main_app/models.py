from django import forms
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from .choices import USERTYPE_CHOICES, LOCATION_CHOICES, CLASSTYPE_CHOICES, DATE_CHOICES

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = forms.CharField(max_length=30, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your first name"}))
    last_name = forms.CharField(max_length=30, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your last name"})) 
    # username = forms.CharField(max_length=30, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input username"}))
    email = forms.EmailField(max_length=250, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your email"}))
    usertype = forms.CharField(label= "Student or Instructor", initial = '', widget=forms.Select(choices=USERTYPE_CHOICES))
    location = forms.CharField(label="What City is your cohort in?", widget=forms.Select(choices=LOCATION_CHOICES))
    class_start_date = forms.DateField(widget = forms.Select(choices=DATE_CHOICES))
    class_type = forms.CharField(label = "Class Type", initial= '', widget = forms.Select(choices=CLASSTYPE_CHOICES)) 
    password1 = forms.CharField(max_length=30, label='', help_text='', widget=forms.PasswordInput(attrs={"placeholder": "Input your password"}))
    password2 = forms.CharField(max_length=30, label='', help_text='', widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"}))

# class Instructor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
