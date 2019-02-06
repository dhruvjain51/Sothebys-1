from django.db import models

# Create your models here.
class Review(models.Model):
    order_id = models.ForeignKey(
        'orders.Order', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

