from django.db import models

# Create your models here.
# class Userable(models.Model):
#     name = models.CharField(max_length=10)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=30)
#
# class Postable(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     # userable = models.ForeignKey('employ.Userable', on_delete=models.CASCADE)

class Employ_post(models.Model):
    required_num = models.IntegerField()
    start_date = models.DateTimeField(max_length=20)
    end_date = models.DateTimeField(max_length=20)
    prefer_condition = models.CharField(max_length=30)
    image = models.ImageField(upload_to='download/')
    # postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)

class Question(models.Model):
    # postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)
    employ_post = models.ForeignKey('employ.Employ_post', on_delete=models.CASCADE)
    # userable = models.ForeignKey('employ.Userable', on_delete=models.CASCADE)

class Answer(models.Model):
    progress = models.CharField(max_length=10)
    # postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)
    question = models.ForeignKey('employ.Question', on_delete=models.CASCADE)
    # userable = models.ForeignKey('employ.Userable', on_delete=models.CASCADE)


