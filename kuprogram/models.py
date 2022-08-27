from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Circleprogram(models.Model):
    author = models.ForeignKey(User, related_name='circleprogram', on_delete=models.CASCADE, blank=True, null=True)
    #동아리명
    title = models.CharField(max_length=15)
    #제목
    subject = models.CharField(max_length = 200)
    #내용
    content = models.TextField()
    #카테고리
    category = models.CharField(max_length=20)
    create_date = models.DateTimeField(null=True,default='')
    modify_date = models.DateTimeField(null=True, blank=True)
    #해시태그
    hashtag = models.TextField(max_length=100)
    #문의사항
    inquiry = models.TextField()
    #신청연락처
    apply = models.CharField(max_length=20)
    def __str__(self):
        return self.subject

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name