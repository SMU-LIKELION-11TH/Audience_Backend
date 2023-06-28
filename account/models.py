from django.db import models
from django.contrib.auth.models import AbstractUser

class Userable(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=16, unique=True, null=False, default='')
    CHOICES = [
        ('선택', None), ('구직자', 'Applicant'), ('구인자', 'Employer')
    ]
    type = models.CharField(max_length=3, choices=CHOICES)
    interest = models.ManyToManyField('util.Interest', related_name='interests')

class Applicant(Userable):
    nickname = models.CharField(max_length=16, unique=True, null=False, default='')
    age = models.IntegerField(null=False, default='20')

    GENDER = [
        ('남자', 'male'), ('여자', 'female'), ('선택 안 함', None)
    ]
    gender = models.CharField(max_length=10, choices=GENDER)

    SCHOOL = [
        ('중졸', '중졸'), ('고졸', '고졸'), ('고졸', '고졸'), ('대학교 2,3년제', '대학교 2,3년제'),
        ('대학교 4년제', '대학교 4년제'), ('졸업 예정자', '졸업 예정자'), ('졸업자', '졸업자')
    ]
    school = models.CharField(max_length=10, choices=SCHOOL)

    career = models.CharField(max_length=100, null=True)

class Employer(Userable):
    company = models.CharField(max_length=20, null=False, default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
