from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Product(models.Model):
    usage_possibilities = (('P', 'Prywatne'), ('K', 'Komercyjne'), ('KO', 'Komercyjne ograniczone'))

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=600, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    username = models.CharField(max_length=100, null=True)
    usage = models.CharField(max_length=2, choices=usage_possibilities)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Messages(models.Model):
    usage_possibilities = (('P', 'Prywatne'), ('K', 'Komercyjne'), ('KO', 'Komercyjne ograniczone'))
    status_possibilities = (('A', 'Zaakceptowana'), ('O', 'Odrzucona'))

    photo_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_from = models.CharField(max_length=100)
    user_to = models.CharField(max_length=100)
    message_text = models.CharField(max_length=600, null=True, blank=True)
    negotiation_price = models.FloatField()
    negotiation_usage = models.CharField(max_length=2, choices=usage_possibilities)
    negotiation_status = models.CharField(max_length=1, choices=status_possibilities, blank=True)
