from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    # path('registration/signin/', views.signin, name='signin'),
    # path('registration', include('django.contrib.auth.urls')),
    # path('registration/signup/', views.signup, name='signup'),
]
