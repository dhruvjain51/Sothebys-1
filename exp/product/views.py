from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

# Create your views here.
def get_paintings(request, id):
    response = requests.get('http://models-api:8000/api/v1/paintings/' + str(id) + '/')
    json_data = json.loads(response.text)
    for element in json_data:
        element['artist_name'] = get_painting_artist(int(element['artist_id']))
    return JsonResponse(json_data, safe=False)



def get_painting_artist(id):
    response = requests.get('http://models-api:8000/api/v1/artists/' + str(id) + '/')
    json_data = json.loads(response.text)
    return json_data[0]['name']

def get_all_by_artist(request, id):
    response = requests.get('http://models-api:8000/api/v1/paintings/')
    json_paintings = json.loads(response.text)

    to_remove = []
    for p in json_paintings:
        if p["artist_id"] != id:
            to_remove.append(p)

    for rem in to_remove:
        json_paintings.remove(rem)

    # alternative method of removing from list

    # done = False
    # while done == False:
    #     remove = False
    #     for p in json_paintings:
    #         if p["artist_id"] != id:
    #             json_paintings.remove(p)
    #             remove = True
    #     if remove == False:
    #         done = True

    return JsonResponse(json_paintings, safe=False)
