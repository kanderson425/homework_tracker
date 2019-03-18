from django.urls import path, include
from django.conf.urls import url
from .views import views, instructors, students

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/student', students.StudentSignUpForm, name='student-signup'),
    path('accounts/signup/instructor', instructors.InstructorSignUpForm, name='instructor-signup'),
    path('accounts/login/', views.login, name='login'),
]
