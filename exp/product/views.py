from django.shortcuts import render
import requests
import json
from kafka import KafkaProducer
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from elasticsearch import Elasticsearch
# Create your views here.


def get_paintings(request, id):
    response = requests.get('http://models-api:8000/api/v1/paintings/' + str(id) + '/')
    json_data = json.loads(response.text)
    for element in json_data:
        element['artist_name'] = get_painting_artist(int(element['artist_id']))
        element['seller_name'] = get_painting_seller(int(element['seller_id']))
    return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_painting(request):
    if request.method == "POST":
        title = request.POST['title']
        image = request.POST['image']
        description = request.POST['description']
        medium = request.POST['medium']
        price = request.POST['price']
        artist = request.POST['artist']
        auth = request.POST['auth']
        # seller = request.POST['seller']
        # First we check if the supplied auth token even exists in the DB
        auth_check = check_auth(auth)
        if auth_check is 0:  # Auth Failed
            return JsonResponse({'status': 400, 'login': 0}, safe=False, status=200)
        else:
            seller = auth_check
            # If it exists, we get the user id, and post as normal,
            # If not, we send error with some message that login failed.
        post_data = {'title': title, 'image': image, 'description': description,
                     'medium': medium, 'price': price, 'artist': artist, 'seller': seller}
        response = requests.post('http://models-api:8000/api/v1/paintings/create/', data=post_data)
        status = response.status_code
        if status == 200:
            producer = KafkaProducer(bootstrap_servers='kafka:9092')
            response = requests.get('http://models-api:8000/api/v1/paintings/latest/1')
            json_data = json.loads(response.text)
            producer.send('painting-topic', json.dumps(json_data).encode('utf-8'))
            return JsonResponse({'status': 200, 'login': 1, 'message': "Success"}, safe=False, status=200)
        else:
            return JsonResponse({'status': 400, 'login': 1, 'message': "Error"}, safe=False, status=400)

    if request.method == "GET":
        return HttpResponse("Has to be a POST Request")


def check_auth(auth):
    post_data_auth = {'auth': auth}
    response_auth = requests.post(
        'http://models-api:8000/api/v1/auth/', data=post_data_auth)
    json_data_auth = json.loads(response_auth.text)
    if json_data_auth['status'] is 400:
        return 0
    else:
        return json_data_auth['user_id']


def get_painting_artist(id):
    response = requests.get('http://models-api:8000/api/v1/artists/' + str(id) + '/')
    json_data = json.loads(response.text)
    return json_data[0]['name']


def get_painting_seller(id):
    response = requests.get('http://models-api:8000/api/v1/sellers/' + str(id) + '/')
    json_data = json.loads(response.text)
    return json_data[0]['first_name'] + " " + json_data[0]['last_name']


def get_all_by_artist(request, id):
    # Changed by SHABAD, so that the id passed is the painting id, which i have in the front end, i get the artist id from the painting id here (NOTE FOR ROMAN)
    res = requests.get('http://models-api:8000/api/v1/paintings/' + str(id) + '/')
    js = json.loads(res.text)
    id = js[0]['artist_id']

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


def get_all_artists(request):
    response = requests.get('http://models-api:8000/api/v1/artists/')
    json_data = json.loads(response.text)

    for element in json_data:
        del element['image']
        del element['description']
        del element['nationality']
        del element['dob']
        del element['dod']
    return JsonResponse(json_data, safe=False)

@csrf_exempt
def search_painting(request):
    if request.method == "POST":
        es = Elasticsearch(['es'])
        query = request.POST['query']
        json_data = es.search(index='painting_index', body={'query': {'query_string': {'query': query}}, 'size': 10})
        results = json_data['hits']['hits']
        if not results:
            return JsonResponse([], safe=False)
        else:
            for i in results:
                painting_id = (i.get('_source', {}).get('id'))
                response = requests.get('http://models-api:8000/api/v1/paintings/' + str(painting_id) + '/')
                json_data = json.loads(response.text)
                return JsonResponse(json_data, safe=False)

    if request.method == "GET":
        return HttpResponse("Has to be a POST Request")