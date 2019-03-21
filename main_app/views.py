from django.contrib.auth import login
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login 
from .models import Profile, Unit, Week, Assignment
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
  return render(request, 'home.html')

def index(request):
  unit = Unit.objects.all()
  week = Week.objects.all()
  assignment = Assignment.objects
  return render(request, 'users/index.html', {'unit': unit, 'week': week, 'assignment': assignment})

def signin(request):
  return render(request, 'registration/signin.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('registration')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'UserCreationForm': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def registration(request):
  return render(request, 'registration/registration.html', {'form': ProfileForm})

def create_profile(request):
  print('CreateProfile is getting hit')
  if request.method == 'POST':
    # user_form = UserCreationForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST)
    print('Made it past user_form & profile_form')
    if profile_form.is_valid():
      print('Forms have been validated')
      new_profile = profile_form.save(commit=False)
      new_profile.user = request.user
      print('new_profile.user = request.user is working')
      # print(profile_form)
      profile_form.save()
      print(profile_form.save())
    else:
      msg = 'Errors: %s' % profile_form.errors.as_text()
      print(msg)  
  else:
    print('We are hitting the redirect')
    profile_form = ProfileForm(instance=request.user.profile)
  return redirect('index')


