from django.contrib import admin

# Register your models here.
from .models import Buyer, Seller, Authenticator

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Authenticator)
