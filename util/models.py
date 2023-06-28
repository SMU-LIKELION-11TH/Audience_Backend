from django.db import models
from account import Userable
from job import Postable
class Like(models.Model):
    userable = models.ForeignKey("Userable", on_delete=models.CASCADE, null=True)
    postable = models.ForeignKey("Postable", on_delete=models.CASCADE, null=True)

class Dislike(models.Model):
    userable = models.ForeignKey("Userable", on_delete=models.CASCADE, null=True)
    postable = models.ForeignKey("Postable", on_delete=models.CASCADE, null=True)

class Interest(models.Model):
    name = models.CharField(max_length=16, null=False, default='')

class Hashtag(models.Model):
    name = models.CharField(max_length=10, null=False, default='')
    postable = models.ManyToManyField(Postable)