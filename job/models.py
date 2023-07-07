from django.db import models
from employ.models import Postable

# Create your models here.
class Job_post(Postable):
    image = models.ImageField(upload_to='post/job/')
    # 회사, 평점 추가

    employer = models.ForeignKey('account.Employer', on_delete=models.SET_NULL, null=True)

    STARS = [
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
    ]
    rating = models.IntegerField(choices=STARS, null=True)
    search_company = models.CharField(max_length=20)

class Freepost(Postable):
    pass

class report(models.Model):
    content = models.CharField(max_length=100)
    postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)

