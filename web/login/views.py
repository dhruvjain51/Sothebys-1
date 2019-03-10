from django.shortcuts import render
from .forms import SellerRegisterForm, SellerLoginForm
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.urls import reverse
import json


# Create your views here.
def get_login(request):
    if request.method == "POST":
        form = SellerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # next = request.GET.get('next') or reverse('home:home')
            resp = login_exp_api(email, password)

            if resp['status'] is 200:
                authenticator = resp['auth']
                return render(request, "login.html", {'form': form, 'message': "Login Success Baby"})
            else:
                return render(request, "login.html", {'form': form, 'message': "Error"})

    if request.method == "GET":
        forma = SellerLoginForm()
        return render(request, "login.html", {'form': forma, 'message': ""})


def login_exp_api(email, password):
    post_data = {'email': email, 'password': password}
    response = requests.post(
        'http://exp-api:8000/seller/login/', data=post_data)
    json_data = json.loads(response.text)
    return json_data

    # RSend the details to login EXP API, and expect to get back an auth token


def get_signup(request):
    if request.method == "POST":
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            logo = form.cleaned_data['logo']
            description = form.cleaned_data['description']
            # SEND POST REQ TO EXP API
            post_data = {'email': email, 'password': password, 'phone': phone,
                         'description': description, 'first_name': first_name, 'last_name': last_name, 'logo': logo}
            response = requests.post(
                'http://exp-api:8000/seller/create/', data=post_data)
            status = response.status_code
            if status == 200:
                message = "You have been Registered Successfully"
            else:
                message = "Sorry there was an error"

    else:
        form = SellerRegisterForm()
        message = "We are excited as you join us"
    return render(request, "signup.html", {'form': form, 'message': message})
