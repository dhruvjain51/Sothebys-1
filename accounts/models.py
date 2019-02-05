from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from django.utils.encoding import smart_unicode


class User(AbstractUser):
    is_buyer = models.BooleanField('student status', default=False)
    is_seller = models.BooleanField('teacher status', default=False)


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    shipping = models.CharField(max_length=100)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    logo = models.CharField(max_length=150)
