from django.db import models
import datetime
# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    dob = models.DateTimeField(blank=True)
    dod = models.DateTimeField(blank=True)

