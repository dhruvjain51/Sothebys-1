from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_seller(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        description = request.POST['description']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        logo = request.POST['logo']
        # Make POST Request with all this data
        post_data = {'email': email, 'password': password, 'phone': phone,
                     'description': description, 'first_name': first_name, 'last_name': last_name, 'logo': logo}
        response = requests.post('http://models-api:8000/api/v1/sellers/create/', data=post_data)
        status = response.status_code
        if status == 200:
            return JsonResponse("Success", safe=False, status=200)
        else:
            return JsonResponse("Error", safe=False, status=400)

    if request.method == "GET":
        return HttpResponse("Has to be a POST Request")
        # Get the data from the req, and create post req to Models API


@csrf_exempt
def login_seller(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        post_data = {'email': email, 'password': password}
        response = requests.post('http://models-api:8000/api/v1/sellers/login/', data=post_data)
        status = response.status_code
        json_data = json.loads(response.text)
        if status == 200:
            data = {'status': 200, 'auth': json_data['auth']}
            return JsonResponse(data, safe=False, status=200)
        else:
            return JsonResponse({'status': 400, 'message': "Error"}, safe=False, status=400)

    if request.method == "GET":
        return HttpResponse("Has to be a POST Request")
        # Get the data from the req, and create post req to Models API
