from django.db import models
from datetime import datetime
from django.utils import timezone

class Buyer(models.Model):
    email = models.CharField(max_length=50, default='DEFAULT VALUE')
    password = models.CharField(max_length=50, default='DEFAULT VALUE')
    first_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    last_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    phone = models.CharField(max_length=50, default='DEFAULT VALUE')
    shipping = models.CharField(max_length=100, default='DEFAULT VALUE')

    def __str__(self):
        return self.first_name



class Seller(models.Model):
    email = models.CharField(max_length=50, default='DEFAULT VALUE')
    password = models.CharField(max_length=50, default='DEFAULT VALUE')
    first_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    last_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    phone = models.CharField(max_length=50, default='DEFAULT VALUE')
    description = models.CharField(max_length=150, default='DEFAULT VALUE')
    logo = models.CharField(max_length=150, default='DEFAULT VALUE')

    def __str__(self):
        return self.first_name

class Authenticator(models.Model):
    authenticator = models.CharField(max_length=50, default='DEFAULT VALUE')
    user_id = models.ForeignKey(
        'accounts.Buyer', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.authenticator
