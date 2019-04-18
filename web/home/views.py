import json
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 15)
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
