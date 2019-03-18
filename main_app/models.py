from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .choices import USERTYPE_CHOICES, LOCATION_CHOICES, CLASSTYPE_CHOICES, DATE_CHOICES

# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     first_name = models.OneToOneField(User)
#     last_name = models.OneToOneField(User)
#     username = models.OneToOneField(User)
#     email = models.OneToOneField(User)
#     usertype = models.OneToOneField(User)
#     location = models.OneToOneField(User)
#     class_start = models.OneToOneField(User)
#     class_type = models.OneToOneField(User)


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

