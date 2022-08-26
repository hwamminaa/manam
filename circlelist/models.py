from django.db import models

# Create your models here.
class Circle(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
