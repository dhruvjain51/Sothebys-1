from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# from django.utils.encoding import smart_unicode
#
#
# class User(AbstractUser):
#     is_buyer = models.BooleanField('student status', default=False)
#     is_seller = models.BooleanField('teacher status', default=False)


class Buyer(models.Model):
    email = models.CharField(max_length=50, default='DEFAULT VALUE')
    password = models.CharField(max_length=50, default='DEFAULT VALUE')
    first_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    last_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    phone = models.CharField(max_length=50, default='DEFAULT VALUE')
    shipping = models.CharField(max_length=100, default='DEFAULT VALUE')



class Seller(models.Model):
    email = models.CharField(max_length=50, default='DEFAULT VALUE')
    password = models.CharField(max_length=50, default='DEFAULT VALUE')
    first_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    last_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    phone = models.CharField(max_length=50, default='DEFAULT VALUE')
    description = models.CharField(max_length=150, default='DEFAULT VALUE')
    logo = models.CharField(max_length=150, default='DEFAULT VALUE')