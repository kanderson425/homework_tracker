from django.urls import path, include
from django.conf.urls import url
from . import views as views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='login'),
]
