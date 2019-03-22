from django.urls import path, include
from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/register/', views.registration, name='registration'),
  path('accounts/create_profile/', views.create_profile, name='create_profile'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('about/', views.about, name='about'),
  path('assignments/', views.assignments_index, name='index'),
  # path('guitars/<int:guitar_id>/', views.guitars_detail, name='detail'),
  path('assignments/', views.assignment, name='assignment'),
  path('assignments/create', views.create_assignment, name='create_assignment'),
  # path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitars_update'),
  # path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitars_delete'),
  # path('guitars/<int:guitar_id>/add_practice/', views.add_practice, name='add_practice'),
  # path('guitars/<int:guitar_id>/assoc_amp/<int:amp_id>/', views.assoc_amp, name='assoc_amp'),
  # path('guitars/<int:guitar_id>/unassoc_amp/<int:amp_id>/', views.unassoc_amp, name='unassoc_amp'),
  # path('guitars/<int:guitar_id>/add_photo/', views.add_photo, name='add_photo'),
  # path('amps/', views.AmpList.as_view(), name='amps_index'),
  # path('amps/<int:pk>/', views.AmpDetail.as_view(), name='amps_detail'),
  # path('amps/create/', views.AmpCreate.as_view(), name='amps_create'),
  # path('amps/<int:pk>/update/', views.AmpUpdate.as_view(), name='amps_update'),
  # path('amps/<int:pk>/delete/', views.AmpDelete.as_view(), name='amps_delete'),
  
]