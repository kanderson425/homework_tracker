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

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    github_url = models.URLField()
    status = models.CharField(max_length=200, choices=ASSIGNMENT_STATUS_CHOICES)
    description = models.CharField(max_length=200)

# HOURS = (
#     ('1', '1 hour'),
#     ('2', '2 hours'),
#     ('3', '3 hours'),
# )

# class Amp(models.Model):
#     make = models.CharField(max_length=50)
#     model = models.CharField(max_length=50)

#     def __str__(self):
#         return self.make
#         return self.model
    
#     def get_absolute_url(self):
#         return reverse('amps_detail', kwargs={'pk': self.id})

# class Guitar(models.Model):
#     name = models.CharField(max_length=100)
#     make = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     description = models.TextField(max_length=250)
#     amps = models.ManyToManyField(Amp)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'guitar_id': self.id})
    
#     def practice_enough_for_today(self):
#         return self.practice_set.count() >= 5

# class Practice(models.Model):
#     date = models.DateField('Last Practice Date')
#     hour = models.CharField(
#         max_length=1,
#         choices=HOURS,
#         default=HOURS[0][0]
#     )
#     guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.get_hour_display()} on {self.date}"

#     class Meta:
#         ordering = ['-date']

# class Photo(models.Model):
#     url = models.CharField(max_length=200)
#     guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Photo for guitar_id: {self.guitar_id} @{self.url}"