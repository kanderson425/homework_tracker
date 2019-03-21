from django import forms
from django.db import models
from django.urls import reverse
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .choices import USERTYPE_CHOICES, LOCATION_CHOICES, CLASSTYPE_CHOICES, DATE_CHOICES, ASSIGNMENT_STATUS_CHOICES

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200) 
    email = models.CharField(max_length=200)
    usertype = models.CharField(max_length=200,choices=USERTYPE_CHOICES)
    location = models.CharField(max_length=200,choices=LOCATION_CHOICES)
    class_start_date = models.CharField(max_length=200,choices=DATE_CHOICES, default='Jan-2019')
    class_type = models.CharField(max_length=200, choices=CLASSTYPE_CHOICES)

    def __str__(self):
        return f'{self.user} Profile'

class Unit(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100) 

class Week(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    number = models.IntegerField() 
        
class Assignment(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    number = models.IntegerField() 
    status = models.CharField(max_length=200, choices=ASSIGNMENT_STATUS_CHOICES)
    description = models.CharField(max_length=200)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

#     def __str__(self):
#         return self.name

# class Instructor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


# class Cohort(models.Model):
#         user = models.OneToOneField(User, on_delete=models.CASCADE)

# class AssignmentUpload(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)


# class Comment(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)






