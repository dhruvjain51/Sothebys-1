from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.http import JsonResponse
import json


# Create your views here.
def get_home(request):
    r = requests.get('http://exp-api:8000/home/recent_paintings/')
    context = {
        "latest_paintings": get_latest_paintings(),
        "banners": get_banners(),
    }
    return render(request, "home.html", context)


def get_latest_paintings():
    r = requests.get('http://exp-api:8000/home/recent_paintings/')
    return r.json


def get_banners():
    r = requests.get('http://exp-api:8000/home/banner/')
    return r.json
