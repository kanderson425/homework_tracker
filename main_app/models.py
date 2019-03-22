from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

HOURS = (
    ('1', '1 hour'),
    ('2', '2 hours'),
    ('3', '3 hours'),
)

ASSIGNMENT_STATUS_CHOICES = (
    ('Complete', ("Complete")),
    ('Incomplete', ("Incomplete"))
)

class Objective(models.Model):
    unit = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.unit
        return self.description

    def get_absolute_url(self):
        return reverse('objectives_detail', kwargs={'pk': self.id})

class Assignment(models.Model):
    name = models.CharField(max_length=200)
    github_url = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=ASSIGNMENT_STATUS_CHOICES)
    description = models.TextField(max_length=250)
    objectives = models.ManyToManyField(Objective)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'assignment_id': self.id})

class Feedback(models.Model):
    date = models.DateField('Feedback Date')
    comment = models.TextField(max_length=500)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_hour_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for assignment_id: {self.assignment_id} @{self.url}"









# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200) 
#     email = models.CharField(max_length=200)
#     usertype = models.CharField(max_length=200,choices=USERTYPE_CHOICES)
#     location = models.CharField(max_length=200,choices=LOCATION_CHOICES)
#     class_start_date = models.CharField(max_length=200,choices=DATE_CHOICES, default='Jan-2019')
#     class_type = models.CharField(max_length=200, choices=CLASSTYPE_CHOICES)

#     def __str__(self):
#         return f'{self.user} Profile'

# class Assignment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     github_url = models.CharField(max_length=500)
#     status = models.CharField(max_length=200, choices=ASSIGNMENT_STATUS_CHOICES)
#     description = models.CharField(max_length=200)














