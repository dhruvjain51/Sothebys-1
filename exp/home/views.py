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

def get_banner(request):
    response = requests.get('http://models-api:8000/api/v1/paintings/')
    json_data = json.loads(response.text)

    # had to use this awkward way because the objects resort themselves upon every deletion
    # so couldn't use for loop to go through indexes
    length = len(json_data) - 1
    while len(json_data) != 2:
        if json_data[0]["id"] <= length:
            del json_data[0]
        else:
            pass

    for element in json_data:
        del element['medium']
        del element['price']
        del element['timestamp']
        del element['description']
        del element['artist_id']

    return JsonResponse(json_data, safe = False)
# def get_newest_paintings(request):
