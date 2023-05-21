from .models import University, Speciality, Profession
from django.db.models import Q


def searchUniversity(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    universities = University.objects.filter(Q(university_name__icontains=search_query) |
                                             Q(short_name__icontains=search_query) |
                                             Q(university_code__icontains=search_query))

    return universities, search_query

def searchSpeciality(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    specialties = Speciality.objects.filter(Q(speciality_name__icontains=search_query) |
                                             Q(speciality_code__icontains=search_query))
    return specialties, search_query

def searchProfession(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    professions = Profession.objects.filter(Q(profession_name__icontains=search_query))
    
    return professions, search_query