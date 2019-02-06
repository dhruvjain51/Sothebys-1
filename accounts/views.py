from django.shortcuts import render
from .models import Buyer, Seller
from django.http import HttpResponse
from .models import Buyer, Seller
from django.http import JsonResponse

# Create your views here.
def get_buyers(request):
    data = list(Buyer.objects.values())
    return JsonResponse(data, safe=False)


def get_buyers_by_id(request, id):
    data = list(Buyer.objects.values().filter(id = id))
    return JsonResponse(data, safe=False)
