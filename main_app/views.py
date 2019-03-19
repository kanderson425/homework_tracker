from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'users/index.html')

def signin(request):
    return render(request, 'registration/signin.html')

def student_detail(request):
    return render(request, 'instructors/student_detail.html')

def cohort_select(request):
    return render(request, 'instructors/cohort_select.html')

def signup(request):
  error_message=''
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid credentials - try again'
  form = SignUpForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
