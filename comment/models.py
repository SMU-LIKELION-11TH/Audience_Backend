from django.db import models

# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)
    # userable = models.ForeignKey('employ.Userable', on_delete=models.CASCADE)

class Reply(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey('comment.Comment', on_delete=models.CASCADE)
    # postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)
    # userable = models.ForeignKey('employ.Userable', on_delete=models.CASCADE)

