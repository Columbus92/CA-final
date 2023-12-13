from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(max_length=2083)


