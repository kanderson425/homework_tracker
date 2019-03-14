from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'homework_tracker/index.html')

def signin(request):
    return render(request, 'registration/signin.html')
