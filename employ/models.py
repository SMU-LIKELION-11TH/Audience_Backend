from django.db import models

class Postable(models.Model):
    post_title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    # userable = models.ForeignKey('account.Userable', on_delete=models.CASCADE)

class Employ_post(Postable,models.Model):
    required_num = models.IntegerField()
    start_date = models.DateTimeField(max_length=20)
    end_date = models.DateTimeField(max_length=20)
    prefer_condition = models.CharField(max_length=30)
    image = models.ImageField(upload_to='post/employ/')
    CAREER_CHOICES = (('a', '경력'), ('b', '신입'))
    career = models.CharField(max_length=1, default='a', choices=CAREER_CHOICES)

class Question(Postable,models.Model):
    employ_post_ref = models.ForeignKey(Employ_post, on_delete=models.CASCADE)
    # userable = models.ForeignKey('account.Userable', on_delete=models.CASCADE)

class Answer(Postable, models.Model):
    progress = models.CharField(max_length=10)
    question_ref = models.ForeignKey(Question, on_delete=models.CASCADE)
    # userable = models.ForeignKey('account.Userable', on_delete=models.CASCADE)


