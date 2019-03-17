from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'users/index.html')

def signin(request):
    return render(request, 'registration/signin.html')

# def signup(request):
    # error_message=''
    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         login(request, user)
    #         return redirect('index')
    #     else:
    #         error_message = 'Invalid credentials = try again'
    # form = UserCreationForm()
    # context = {'form': form, 'error_message': error_message}
    # return render(request, 'registration/signup.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
