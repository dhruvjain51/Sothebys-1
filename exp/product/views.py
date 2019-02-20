from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

# Create your views here.
def get_paintings(request, id):
    response = requests.get('http://models-api:8000/api/v1/paintings/' + str(id))
    json_data = json.loads(response.text)
    for element in json_data:
        element['artist_name'] = get_painting_artist(int(element['artist_id']))
    return JsonResponse(json_data, safe=False)



def get_painting_artist(id):
    response = requests.get('http://models-api:8000/api/v1/artists/' + str(id))
    json_data = json.loads(response.text)
    return json_data[0]['name']
