from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Create your views here.
def get_popular_paintings(request):
    response = requests.get('http://models-api:8000/api/v1/paintings/')
    json_data = json.loads(response.text)



    # return requests.get('http://models-api:8000/api/v1/paintings/')
    return HttpResponse(json_data)
