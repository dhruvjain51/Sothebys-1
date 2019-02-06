from django.db import models


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
