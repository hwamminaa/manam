from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

##KU만남
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    #제목
    subject = models.CharField(max_length = 200)
    #내용
    content = models.TextField()
    #카테고리
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    hashtag = models.CharField(max_length=200)
    inquiry = models.CharField(max_length=200)
    apply = models.CharField(max_length=200)
    create_date = models.DateTimeField(null=True,default='')
    modify_date = models.DateTimeField(null=True, blank=True)
    hits = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject

    @property
    def click(self):
        self.hits += 1
        self.save()


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


##커뮤니티

class Article(models.Model):
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

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
