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
    CONTENT_CHOICES = (('a','사기/도배'),('b','욕설/비하'))
    content = models.CharField(max_length=1, default='a', choices=CONTENT_CHOICES)
    postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)

