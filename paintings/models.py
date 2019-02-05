from django.db import models
from django.contrib.auth.models import User
# from django.utils.encoding import smart_unicode



class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    shipping = models.CharField(max_length=100)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    logo = models.CharField(max_length=150)


# Create your models here.
class Paitings(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    artist = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    medium = models.CharField(max_length=30)
    price = models.IntegerField()
