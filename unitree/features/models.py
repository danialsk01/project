from django.db import models
import uuid, datetime
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

class University(models.Model):
    # center
    university_name = models.CharField(max_length=150, default='')
    short_name = models.CharField(max_length=50, default='')
    university_code = models.CharField(max_length=10, default='')

    # right info bar
    location = models.CharField(max_length=200, default='')
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    number_of_specialties = models.IntegerField(default=0)
    study_language = models.CharField(max_length=100, default='')
    student_count = models.IntegerField(blank=True, null=True)
    website = models.URLField(blank=True)
    established_year = models.IntegerField(blank=True, null=True)
    tuition_price = models.IntegerField(blank=True, null=True)

    # main
    description = RichTextField(blank=True, null=True)
    logo = models.ImageField(default='', blank=True)
    main_img = models.ImageField(default='', blank=True)

    specialities = models.ManyToManyField('Speciality', blank=True)

    # it's include student life, dormitory, study abroad programs, cluba, organizations, athletics, alumni
    about_university = RichTextField(blank=True, null=True)

    # university accreditation
    accreditation = RichTextField(blank=True, null=True)

    # map
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)

    # carousel
    carousel_1 = models.ImageField(default='', blank=True)
    carousel_2 = models.ImageField(default='', blank=True)
    carousel_3 = models.ImageField(default='', blank=True)

    # social media
    facebook = models.CharField(max_length=250, default='')
    instagram = models.CharField(max_length=250, default='')
    youtube =models.CharField(max_length=250, default='')

    # unique id
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)


    def __str__(self):
        return self.university_name


class Speciality(models.Model):
    # main info
    speciality_name = models.CharField(max_length=150)
    speciality_code = models.CharField(max_length=10)
    description = RichTextField(blank=True, null=True)

    SUBJECTS = [
        ('biology', 'Biology'), 
        ('geography', 'Geography'),
        ('creative exam', 'Creative exam'), 
        ('the World History','The World History'), 
        ('mathematics', 'Mathematics'), 
        ('physics', 'Physics'), 
        ('informatics', 'Informatics'), 
        ('chemistry', 'Chemistry'), 
        ('kazakh language', 'Kazakh language'), 
        ('kazakh literature', 'Kazakh literature'), 
        ('russian language', 'Russian language'), 
        ('russian literature', 'Russian literature'), 
        ('foreign language', 'Foreign language'), 
        ('fundamentals of Law', 'Fundamentals of Law')
    ]

    # 2 subjects to choose
    subject_1 = models.CharField(max_length=20, choices=SUBJECTS)
    subject_2 = models.CharField(max_length=20, choices=SUBJECTS)

    # main speciality image
    main_image = models.ImageField(default='', blank=True)

    salary_from = models.IntegerField(default=0)
    salary_to = models.IntegerField(default=0)

    # images for carousel
    carousel_1 = models.ImageField(default='', blank=True)
    carousel_2 = models.ImageField(default='', blank=True)
    carousel_3 = models.ImageField(default='', blank=True)

    # additional info
    job_outlook = RichTextField(blank=True, null=True)
    salary_range = RichTextField(blank=True, null=True)

    # universities to choose
    universities = models.ManyToManyField('University', blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)


    def __str__(self):
        return self.speciality_name
    

class Profession(models.Model):
    # main info
    profession_name = models.CharField(max_length=150)
    description = RichTextField(blank=True, null=True)
    education = RichTextField(blank=True, null=True)

    # demand for the profession
    DEMAND = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    demand = models.CharField(max_length=10, choices=DEMAND)

    # additional info
    employment_outlook = RichTextField(blank=True, null=True)
    salary_range = RichTextField(blank=True, null=True)

    salary_from = models.IntegerField(default=0)
    salary_to = models.IntegerField(default=0)

    # specialties to choose
    specialties = models.ManyToManyField('Speciality', blank=True)

    skills = RichTextField(blank=True, null=True)

    # main profession image
    main_image = models.ImageField(default='', blank=True)

    # images for carousel
    carousel_1 = models.ImageField(default='', blank=True)
    carousel_2 = models.ImageField(default='', blank=True)
    carousel_3 = models.ImageField(default='', blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)

    def __str__(self):
        return self.profession_name