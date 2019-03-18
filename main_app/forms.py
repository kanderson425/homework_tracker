from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .choices import USERTYPE_CHOICES, LOCATION_CHOICES, CLASSTYPE_CHOICES, DATE_CHOICES

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='First Name', help_text='First Name', widget=forms.TextInput(attrs={"placeholder": "Input your first name"}))
    last_name = forms.CharField(max_length=30, label='Last Name', help_text='Last Name', widget=forms.TextInput(attrs={"placeholder": "Input your last name"})) 
    username = forms.CharField(max_length=30, label='Username', help_text='Username', widget=forms.TextInput(attrs={"placeholder": "Input username"}))
    email = forms.EmailField(max_length=250, label='Email', help_text='Email', widget=forms.TextInput(attrs={"placeholder": "Input your email"}))

    usertype = forms.CharField(
        label= "Student or Instructor", 
        initial = '', 
        widget=forms.Select(choices=USERTYPE_CHOICES)
    )

    location = forms.CharField(
        label="What City is your cohort in?",
        widget=forms.Select(choices=LOCATION_CHOICES)
    )
    

    class_start_date = forms.DateField(
        widget = forms.Select(choices=DATE_CHOICES),  
    )

    class_type = forms.CharField(
        label = "Class Type", 
        initial= '', 
        widget = forms.Select(choices=CLASSTYPE_CHOICES)
    ) 

    password1 = forms.CharField(max_length=30, label='Password', help_text='Password', widget=forms.PasswordInput(attrs={"placeholder": "Input your password"}))
    password2 = forms.CharField(max_length=30, label=' Confirm Password', help_text=' Confirm Password', widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"}))


    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'username',
            'email',
            'usertype',
            'location', 
            'class_start_date', 
            'class_type', 
            'password1', 
            'password2'
        ]
    