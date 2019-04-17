import json
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60 * 15)
def get_product(request, id):
    r = requests.get('http://exp-api:8000/product/' + str(id))
    context = {
        "painting_info": get_painting_info(id),
        "more_by": get_more_by_artist_of(id),
    }
    return render(request, "product.html", context)
    # return HttpResponse("DF" + str(id))


def get_painting_info(id):
    r = requests.get('http://exp-api:8000/product/'+ str(id))
    return r.json



def get_more_by_artist_of(id):
    r = requests.get('http://exp-api:8000/product/more_by/'+ str(id))
    return r.json
