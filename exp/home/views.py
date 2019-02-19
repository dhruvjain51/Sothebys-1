from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Create your views here.
def get_popular_paintings(request):
    response = requests.get('http://models-api:8000/api/v1/paintings/')
    json_data = json.loads(response.text)
    for element in json_data:
        del element['medium']
        del element['price']
    return HttpResponse(json_data)
