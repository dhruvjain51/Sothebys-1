from django.db import models
import datetime

# Create your models here.
class Order(models.Model):
    timestamp = models.DateTimeField(blank=True)
    item = models.ForeignKey('paintings.Painting', on_delete=models.CASCADE)
    buyer = models.ForeignKey(
        'accounts.Buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(
        'accounts.Seller', on_delete=models.CASCADE)
<<<<<<< HEAD

    def __str__(self):
        return self.item
=======
>>>>>>> de10bb69e2f9d8b629c15984dfd94632dcd8bf24
