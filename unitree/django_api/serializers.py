from rest_framework import serializers
from features.models import University, Speciality, Profession

class SpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'speciality_name', 'speciality_code', 'subject_1', 'subject_2']

class UniSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'university_name', 'university_code', 'short_name']

class UniversitySerializer(serializers.ModelSerializer):
    specialities = SpecSerializer(many=True)
    class Meta:
        model = University
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    universities = UniSerializer(many=True)
    class Meta:
        model = Speciality
        fields = '__all__'

class ProfessionSerializer(serializers.ModelSerializer):
    specialties = SpecSerializer(many=True)
    class Meta:
        model = Profession
        fields = '__all__'