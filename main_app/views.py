from django.contrib.auth import login
from django.contrib.auth.models import User
from django.dispatch import receiver
# from django.core.signals import post_save
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Profile

def home(request):
  return render(request, 'home.html')

def index(request):
  return render(request, 'users/index.html')

def signin(request):
  return render(request, 'registration/signin.html')

def registration(request):
  return render(request, 'registration/registration.html', {'form': RegistrationForm()})

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
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# def register(request):
#   error_message = ''
#   if request.method == 'POST':
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#       profile = form.save()
#       return redirect('index')
#     else:
#       error_message = 'Invalid credentials - try again'
#   form = RegistrationForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, './templates/home.html', context)

# class ProfileCreate(CreateView):
#   print('Is the function even running?')
#   model = Profile
#   print("We made it to the first line")
#   fields = ['first_name', 'last_name', 'email', 'usertype', 'location', 'class_start_date', 'class_type']

#   def form_valid(self, RegistrationForm):
#     RegistrationForm.instance.user = self.request.user
#     return super().RegistrationForm_valid(RegistrationForm)
#   print('This is a test 123456789')
#   success_url = './templates/home.html'
#   print('This is another test 123444444')

# @receiver(post_save, sender=User)
# def ensure_profile_exists(sender, **kwargs):
#   if kwargs.get('created', False):
#     Profile.objects.get_or_create(user=kwargs.get('instance'))

# def register(request, user_id):
#   form = RegistrationForm(request.POST)
#   if form.is_valid():
#     new_profile = form.save(commit=False)
#     new_profile.user_id = user_id
#     new_profile.save()
#   return redirect('home', user_id=user_id)

def register(request):
  print('This info should be pushed to the database')
  error_message = ''
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    print('The request method is working')
    if form.is_valid():
      print('the form is valid')
      post = form.save(commit=False)
      post.user = request.user
      post.save()
      return redirect('./templates/home')
    else:
      error_message = 'Invalid profile credentials - try again'
      print('The form is invalid')
  print('The request method is not POST')
  form = RegistrationForm()
  context = {'form': form, 'error_message': error_message}
  print('We are re-routing')
  return render(request, './templates/home', context)

# def register(request):
#   class ProfileCreate(CreateView):
#     model = Profile
#     fields = ['user', 'first_name', 'last_name', 'email', 'usertype', 'location', 'class_start_date', 'class_type', 'password1', 'password2']

#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True)
#     last_name = forms.CharField(max_length=30, required=True)
#     email = forms.EmailField(max_length=256, required=True)
#     location = forms.CharField(max_length=30, required=True)
#     class_start_date = forms.CharField(max_length=30, required=True)
#     class_type = forms.CharField(max_length=30, required=True)

#     class Meta:
#         model = User
#         fields = {'first_name', 'last_name', 'email', 'location', 'class_start_date', 'class_type', 'password1', 'password2'}
