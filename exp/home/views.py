from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.http import JsonResponse
import json


# Create your views here.
def get_recent_paintings(request):
    response = requests.get('http://models-api:8000/api/v1/paintings/latest/3')
    json_data = json.loads(response.text)
    for element in json_data:
        del element['medium']
        del element['price']
        del element['timestamp']
    return JsonResponse(json_data, safe=False)

# def get_newest_paintings(request):
