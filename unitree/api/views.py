from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UniversitySerializer, SpecialitySerializer, ProfessionSerializer
from features.models import University, Speciality, Profession

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/features'},
    ]

    return Response(routes)

@api_view(['GET'])
def getUniversities(request):
    universities = University.objects.all()
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUniversity(request, pk):
    universety = University.objects.get(id=pk)
    serializer = UniversitySerializer(universety, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getSpecialties(request):
    specialties = Speciality.objects.all()
    serializer = SpecialitySerializer(specialties, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSpecialty(request, pk):
    specialty = Speciality.objects.get(id=pk)
    serializer = SpecialitySerializer(specialty, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getProfessions(request):
    professions = Profession.objects.all()
    serializer = ProfessionSerializer(professions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProfession(request, pk):
    profession = Profession.objects.get(id=pk)
    serializer = ProfessionSerializer(profession, many=False)
    return Response(serializer.data)