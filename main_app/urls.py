from django.urls import path, include
from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/register/', views.registration, name='registration'),
    path('accounts/create_profile/', views.create_profile, name='create_profile'),
    # path('accounts/register/<int:user_id>', views.registration, name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('cohort_create', views.cohort_create, name='cohort_create'),
    # path('cohort_overview', views.cohort_overview, name='cohort_overview'),
    # path('single_unit_view', views.assignment_upload, name='assignment_upload')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

