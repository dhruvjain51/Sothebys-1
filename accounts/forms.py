from django.db import models
from django.forms import ModelForm
from .models import Buyer, Seller

class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'shipping']

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'description','logo']
