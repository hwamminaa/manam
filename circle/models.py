from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #제목
    subject = models.CharField(max_length = 200)
    #내용
    content = models.TextField()
    #카테고리
    category = models.CharField(max_length=20)
    create_date = models.DateTimeField(null=True,default='')
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
