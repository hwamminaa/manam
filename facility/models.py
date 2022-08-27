from django.db import models

# Create your models here.
class Facility(models.Model):
    cate_1 = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    dong = models.CharField(max_length=50)
    cate_2 = models.CharField(max_length=50)
    content = models.TextField()
    url = models.CharField(max_length=500)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name