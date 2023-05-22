from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('universities/', views.universities, name="universities"),
    path('university/<str:pk>/', views.university, name="university"),
    path('specialties/', views.specialties, name="specialties"),
    path('speciality/<str:pk>/', views.speciality, name="speciality"),
    path('professions/', views.professions, name="professions"),
    path('profession/<str:pk>/', views.profession, name="profession"),
    path('django_api/', include('django_api.urls')),
]
