from django.db import models
from employ.models import Postable

# Create your models here.
class Job_post(Postable,models.Model):
    image = models.ImageField(upload_to='post/job/')
    APPLY_CONDITION = (('a','인턴'),('b','정규직'),('c','비정규직'))
    apply_condition = models.CharField(max_length=1, default='a', choices= APPLY_CONDITION  )
    # userable = models.ForeignKey('account.Userable', on_delete=models.CASCADE)

class Freepost(Postable,models.Model):
    pass

class report(models.Model):
    CONTENT_CHOICES = (('a','사기/도배'),('b','욕설/비하'))
    content = models.CharField(max_length=1, default='a', choices=CONTENT_CHOICES)
    postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)

