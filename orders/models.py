from django.db import models


# Create your models here.
class Order(models.Model):
    timestamp = models.DateTimeField(blank=True)
    item = models.ForeignKey('paintings.Painting', on_delete=models.CASCADE)
