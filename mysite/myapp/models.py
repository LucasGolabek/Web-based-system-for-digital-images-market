from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=600, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name



