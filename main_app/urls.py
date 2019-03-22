from django.urls import path, include 
from main_app import views 

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('about/', views.about, name='about'),
  path('assignments/', views.assignments_index, name='index'),
  path('assignments/<int:assignment_id>/', views.assignments_detail, name='detail'),
  path('assignments/create/', views.assignmentCreate.as_view(), name='assignments_create'),
  path('assignments/<int:pk>/update/', views.assignmentUpdate.as_view(), name='assignments_update'),
  path('assignments/<int:pk>/delete/', views.assignmentDelete.as_view(), name='assignments_delete'),
  path('assignments/<int:assignment_id>/add_feedback/', views.add_feedback, name='add_feedback'),
  path('assignments/<int:assignment_id>/assoc_objective/<int:objective_id>/', views.assoc_objective, name='assoc_objective'),
  path('assignments/<int:assignment_id>/unassoc_objective/<int:objective_id>/', views.unassoc_objective, name='unassoc_objective'),
  path('assignments/<int:assignment_id>/add_photo/', views.add_photo, name='add_photo'),
  path('objectives/', views.objectiveList.as_view(), name='objectives_index'),
  path('objectives/<int:pk>/', views.objectiveDetail.as_view(), name='objectives_detail'),
  path('objectives/create/', views.objectiveCreate.as_view(), name='objectives_create'),
  path('objectives/<int:pk>/update/', views.objectiveUpdate.as_view(), name='objectives_update'),
  path('objectives/<int:pk>/delete/', views.objectiveDelete.as_view(), name='objectives_delete'),
]