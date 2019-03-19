from django.urls import path, include
from django.conf.urls import url
from . import views as views
from . import views

urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('student_detail/', views.student_detail, name="student_detail"),
    path('cohort_select/', views.cohort_select, name="cohort_select"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='login'),
]
