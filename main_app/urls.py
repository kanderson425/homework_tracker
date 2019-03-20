from django.urls import path, include
from django.conf.urls import url
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/register/', views.registration, name='registration'),
    path('accounts/create_profile/', views.create_profile, name='create_profile'),
    # path('accounts/register/<int:user_id>', views.registration, name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
]
