from django.db import models


# Create your models here.

class Product(models.Model):
    usage_possibilities = (('Prywatne', 'Prywatne'), ('Komercyjne', 'Komercyjne'), ('Komercyjne ograniczone',
                                                                                    'Komercyjne ograniczone'))

    photo_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.TextField(max_length=600, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    username = models.CharField(max_length=100, null=True)
    usage = models.CharField(max_length=100, choices=usage_possibilities)

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
    usage_possibilities = (('Prywatne', 'Prywatne'), ('Komercyjne', 'Komercyjne'), ('Komercyjne ograniczone',
                                                                                    'Komercyjne ograniczone'))
    status_possibilities = (('Zaakceptowana', 'Zaakceptowana'), ('Odrzucona', 'Odrzucona'),
                            ('Oczekująca', 'Oczekująca'), ('Archiwalna', 'Archiwalna'),
                            ('Oczekuje na wpłatę', 'Oczekuje na wpłatę'))

    message_id = models.BigAutoField(primary_key=True)
    user_from = models.CharField(max_length=100)
    user_to = models.CharField(max_length=100)
    message_text = models.TextField(max_length=600, null=True, blank=True)
    negotiation_price = models.FloatField()
    negotiation_usage = models.CharField(max_length=100, choices=usage_possibilities)
    negotiation_status = models.CharField(max_length=100, choices=status_possibilities,
                                          default=status_possibilities[2][0])
    photo_id = models.ForeignKey(Product, on_delete=models.CASCADE)
