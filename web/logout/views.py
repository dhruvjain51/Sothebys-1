from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.urls import reverse
import json


def logout(request):
    response = HttpResponseRedirect(reverse('home:home'))
    response.delete_cookie('auth')
    return response
