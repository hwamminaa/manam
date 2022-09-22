from django.db import models
from django.conf import settings

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=10)
    host = models.CharField(max_length=20, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    price = models.IntegerField()
    age = models.CharField(max_length=30)
    link = models.CharField(max_length=400, null=True)
    description = models.TextField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_program')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Recommendation(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=20, null=True)
    rec1 = models.CharField(max_length=200)
    rec2 = models.CharField(max_length=200)
    rec3 = models.CharField(max_length=200)
    rec4 = models.CharField(max_length=200)
    rec1age = models.CharField(max_length=20, null=True)
    rec2age = models.CharField(max_length=20, null=True)
    rec3age = models.CharField(max_length=20, null=True)
    rec4age = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name