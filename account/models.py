from django.db import models
from django.contrib.auth.models import AbstractUser
from util import Interest

class Userable(AbstractUser):
    first_name = None
    last_name = None
    email = None
    username = models.CharField(max_length=16, unique=True, null=False, default='')
    CHOICES = [
        ('선택', None), ('구직자', 'Applicant'), ('구인자', 'Employer')
    ]
    type = models.CharField(max_length=3, choices=CHOICES)
    interest = models.ManyToManyField(Interest)

class Applicant(Userable):
    nickname = models.CharField(max_length=16, unique=True, null=False, default='')
    age = models.IntegerField(null=False)
    GENDER = [
        ('남자', 'male'), ('여자', 'female'), ('선택 안 함', None)
    ]
    gender = models.CharField(max_length=10, choices=GENDER)
    school = models.CharField(max_length=30, null=False, default=None)

class Employer(Userable):
    company = models.CharField(max_length=20, null=False, default='')
    phone_num = models.CharField(max_length=12, null=False, default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1)