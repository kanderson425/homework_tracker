from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='First Name', help_text='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name', help_text='Last Name') 
    username = forms.CharField(max_length=30, label='Username', help_text='Username')
    email = forms.EmailField(max_length=250, label='Email', help_text='Email')
    location = forms.CharField(max_length=30, label='Location', help_text='Location')
    class_start_date = forms.CharField(max_length=30, label='Start Date', help_text='Start Date')
    class_type = forms.CharField(max_length=30, label='Class Type', help_text='Class Type')    

    class Meta:
        model = User
        fields = {
            'first_name', 
            'last_name', 
            'email', 
            'location', 
            'class_start_date', 
            'class_type', 
            'password1', 
            'password2'
            }
