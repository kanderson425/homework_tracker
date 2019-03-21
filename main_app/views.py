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
from .models import Profile

# Create your views here.
def home(request):
  return render(request, 'home.html')

def index(request):
  return render(request, 'users/index.html')

def signin(request):
  return render(request, 'registration/signin.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      profile_form = ProfileForm()
      user_form = UserCreationForm()
      login(request, user)
      return redirect('registration')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'UserCreationForm': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def registration(request):
  user = request.user
  return render(request, 'registration/registration.html', {'form': ProfileForm})


# def CreateProfile(request, user_id):
#   form = ProfileForm(request.POST)
#   if form.is_valid():
#     new_profile = form.save(commit=False)
#     new_profile.user_id = user_id
#     new_profile.save()
#     return redirect('index', user_id=user_id)
#   else:
#     return redirect('home')

def create_profile(request):
  print('CreateProfile is getting hit')
  error_message = ''
  if request.method == 'POST':
    # user_form = UserCreationForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST)
    print('Made it past user_form & profile_form')
    if profile_form.is_valid():
      print('Forms have been validated')
      new_profile = profile_form.save(commit=False)
      new_profile.user = request.user
      print('new_profile.user = request.user is working')
      # new_profile.save()
      print(ProfileForm)
    else:
      msg = 'Errors: %s' % profile_form.errors.as_text()
      print(msg)  
  else:
    print('We are hitting the redirect')
    user_form = UserCreationForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
  return redirect('index')
 

# def CreateProfile(request, user_id):
#   form = ProfileForm(request.POST)
#   if form.is_valid():

#     new_profile = form.save(commit=False)
#     new_profile.user_id = user_id
#     new_profile.save()
#   return redirect('index')
      
