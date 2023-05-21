from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('universities/', views.getUniversities),
    path('universities/<str:pk>/', views.getUniversity),
    path('specialties/', views.getSpecialties),
    path('specialties/<str:pk>/', views.getSpecialty),
    path('professions/', views.getProfessions),
    path('professions/<str:pk>/', views.getProfession),
]
