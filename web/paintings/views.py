from django.shortcuts import render
from .forms import CreatePaintingForm
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.urls import reverse


def create_painting(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect(reverse("login:login-home") + "?next=" + reverse("paintings:create_painting"))

    if request.method == "POST":
        # Call create_listing_exp_api pass in name, title, aithor ... here
        # get result, see if success, then redirect to success page, else redirect to error
        return render(request, "success.html", {'form': form, 'message': ""})
    if request.method == "GET":
        form = CreatePaintingForm()
        return render(request, "create.html", {'form': form, 'message': ""})


def create_painting_exp_api(auth):
    # Call Exp API, pass everything form data.
    # Get result, return json result
