from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.

def get_product(request, id):
    r = requests.get('http://exp-api:8000/product/' + str(id))
    context = {
        "painting_info": get_painting_info(id),
    }
    return render(request, "product.html", context)
    # return HttpResponse("DF" + str(id))


def get_painting_info(id):
    r = requests.get('http://exp-api:8000/product/'+ str(id))
    return r.json
