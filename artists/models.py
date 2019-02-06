from django.db import models
import datetime
# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    dob = models.DateField(blank=True)
    dod = models.DateField(blank=True)

    def __str__(self):
        return self.name
