from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/registration/<int:user_id>', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
