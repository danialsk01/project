from django.shortcuts import render
from django.http import HttpResponse
from .models import University, Speciality, Profession
from django.db.models import Q
from .utils import searchUniversity, searchSpeciality, searchProfession


def home(request):
    return render(request, 'features/index.html')

def universities(request):
    universities, search_query = searchUniversity(request)

    context = {
        'universities': universities,
        'search_query': search_query
    }
    return render(request, 'features/universities.html', context)

def university(request, pk):
    universityObj = University.objects.get(id=pk)
    context = {
        'university': universityObj,
    }
    return render(request, 'features/university-page.html', context)

def specialties(request):
    specialties, search_query = searchSpeciality(request)

    context = {
        'specialties': specialties,
        'search_query': search_query
    }
    return render(request, 'features/specialties.html', context)

def speciality(request, pk):
    specialityObj = Speciality.objects.get(id=pk)
    context = {
        'speciality': specialityObj
    }
    return render(request, 'features/speciality-page.html', context)

def professions(request):
    professions, search_query = searchProfession(request)
    
    context = {
        'professions': professions,
        'search_query': search_query
    }
    return render(request, 'features/professions.html', context)

def profession(request, pk):
    professionObj = Profession.objects.get(id=pk)
    context = {
        'profession': professionObj
    }
    return render(request, 'features/profession-page.html', context)