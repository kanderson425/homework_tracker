from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Assignment 
from .choices import USERTYPE_CHOICES, LOCATION_CHOICES, CLASSTYPE_CHOICES, DATE_CHOICES, ASSIGNMENT_STATUS_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your first name"}))
    last_name = forms.CharField(max_length=30, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your last name"})) 
    email = forms.CharField(required=False, max_length=250, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your email"}))
    usertype = forms.CharField(label= "Student or Instructor", initial = '', widget=forms.Select(choices=USERTYPE_CHOICES))
    location = forms.CharField(label="What City is your cohort in?", widget=forms.Select(choices=LOCATION_CHOICES))
    class_start_date = forms.CharField(required=False, widget = forms.Select(choices=DATE_CHOICES))
    class_type = forms.CharField(label = "Class Type", initial= '', widget = forms.Select(choices=CLASSTYPE_CHOICES)) 
    # password1 = forms.CharField(max_length=30, label='', help_text='', widget=forms.PasswordInput(attrs={"placeholder": "Input your password"}))
    # password2 = forms.CharField(max_length=30, label='', help_text='', widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"}))

    class Meta:
        model = Profile
        fields = [
            'first_name', 
            'last_name',
            # 'username',
            'email',
            'usertype',
            'location', 
            'class_start_date', 
            'class_type', 
            # 'password1', 
            # 'password2'
        ]

class UploadAssignmentForm(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder": "Input Assignment Name"}) )
    github_url = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Input Assignment URL"}))
    status = forms.CharField(label="Is the assignment complete?", widget=forms.Select(choices=ASSIGNMENT_STATUS_CHOICES))
    description = forms.CharField(max_length = 500, required=True, widget=forms.TextInput(attrs={"placeholder": "Input Assignment Description"}))

    class Meta:
        model = Assignment 
        fields = ['name','github_url', 'status','description']