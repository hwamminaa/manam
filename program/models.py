from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=5)
    category = models.CharField(max_length=10)
    age = models.CharField(max_length=5)
    price = models.CharField(max_length=10)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    host = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name