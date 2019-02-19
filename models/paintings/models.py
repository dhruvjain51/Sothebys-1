from django.db import models
from datetime import datetime
# from django.utils.encoding import smart_unicode


# Create your models here.
class Painting(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=30)
    medium = models.CharField(max_length=30)
    price = models.IntegerField()
    artist = models.ForeignKey(
        'artists.Artist', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
