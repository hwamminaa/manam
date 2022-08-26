from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=5)
    category = models.CharField(max_length=10)
    age = models.CharField(max_length=5)
    price = models.IntegerField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    host = models.CharField(max_length=20, null=True)
    link = models.CharField(max_length=400, null=True)
    coorx = models.CharField(max_length=30, null=True)
    coory = models.CharField(max_length=30, null=True)

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