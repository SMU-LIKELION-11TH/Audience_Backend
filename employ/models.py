from django.db import models

class Postable(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    userable = models.ForeignKey('account.Userable', on_delete=models.CASCADE, null=True)

class Employ_post(Postable):
    required_num = models.IntegerField()
    start_date = models.DateTimeField(max_length=20)
    end_date = models.DateTimeField(max_length=20)
    prefer_condition = models.CharField(max_length=30)
    image = models.ImageField(upload_to='post/employ/', null=True)
    CAREER_CHOICES = (('a', '경력'), ('b', '신입'))
    career = models.CharField(max_length=1, default='a', choices=CAREER_CHOICES)
    EMPLOY_SHAPE_CHOICES = (('a','인턴'),('b','정규직'),('c','비정규직'))
    employ_shape = models.CharField(max_length=1, default='a', choices=EMPLOY_SHAPE_CHOICES )
    apply_method = models.CharField(max_length=50)

class Freepost_e (Postable,models.Model):
    pass


class Question(Postable):
    employ_post_ref = models.ForeignKey(Employ_post, on_delete=models.CASCADE)


class Answer(Postable):
    progress = models.CharField(max_length=10)
    question_ref = models.ForeignKey(Question, on_delete=models.CASCADE)


