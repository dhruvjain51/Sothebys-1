from django.db import models

# Create your models here.
class Paitings(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    artist = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    medium = models.CharField(max_length=30)
    price = models.IntegerField()
