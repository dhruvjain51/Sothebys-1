from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Create your views here.
def get_home(request):
    context = {
        "products": "products",
    }
    return render(request, "home.html", context)



# def get_latest_paintings():
