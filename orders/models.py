from django.db import models


# Create your models here.
class Order(models.Model):
    timestamp = models.DateTimeField(blank=True)
    item = models.ForeignKey('paintings.Painting', on_delete=models.CASCADE)
    buyer = models.ForeignKey(
        'accounts.Buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(
        'accounts.Seller', on_delete=models.CASCADE)