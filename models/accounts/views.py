from django.shortcuts import render
from .models import Buyer, Seller
from django.http import HttpResponse
from .models import Buyer, Seller
from django.http import JsonResponse
from .forms import BuyerForm, SellerForm
from django.views.decorators.csrf import csrf_exempt
import os
import hmac
from django.conf import settings


# Create your views here.
def get_buyers(request):
    data = list(Buyer.objects.values())
    return JsonResponse(data, safe=False)


@csrf_exempt
def get_buyers_by_id(request, id):
    if request.method == 'GET':
        data = list(Buyer.objects.values().filter(id = id))
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        try:
            if 'email' in request.POST:
                Buyer.objects.filter(id = id).update(email = request.POST.get("email"))
            if 'password' in request.POST:
                Buyer.objects.filter(id = id).update(password = request.POST.get("password"))
            if 'first_name' in request.POST:
                Buyer.objects.filter(id = id).update(first_name = request.POST.get("first_name"))
            if 'last_name' in request.POST:
                Buyer.objects.filter(id = id).update(last_name = request.POST.get("last_name"))
            if 'phone' in request.POST:
                Buyer.objects.filter(id = id).update(phone = request.POST.get("phone"))
            if 'shipping' in request.POST:
                Buyer.objects.filter(id = id).update(shipping = request.POST.get("shipping"))

            data = list(Buyer.objects.values().filter(id = id))
            return JsonResponse(data, safe=False)

        except:
            message = "wrong format of POST body"
            return JsonResponse({'message':message}, status=400)


def get_sellers(request):
    data = list(Seller.objects.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_sellers_by_id(request, id):
    if request.method == 'GET':
        data = list(Seller.objects.values().filter(id = id))
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        try:
            if 'email' in request.POST:
                Seller.objects.filter(id = id).update(email = request.POST.get("email"))
            if 'password' in request.POST:
                Seller.objects.filter(id = id).update(password = request.POST.get("password"))
            if 'first_name' in request.POST:
                Seller.objects.filter(id = id).update(first_name = request.POST.get("first_name"))
            if 'last_name' in request.POST:
                Seller.objects.filter(id = id).update(last_name = request.POST.get("last_name"))
            if 'phone' in request.POST:
                Seller.objects.filter(id = id).update(phone = request.POST.get("phone"))
            if 'description' in request.POST:
                Seller.objects.filter(id = id).update(description = request.POST.get("description"))
            if 'logo' in request.POST:
                Seller.objects.filter(id = id).update(logo = request.POST.get("logo"))

            data = list(Seller.objects.values().filter(id = id))
            return JsonResponse(data, safe=False)

        except:
            message = "wrong format of POST body"
            return JsonResponse({'message':message}, status=400)


def generate_authenticator():
    authenticator = hmac.new(
        key = settings.SECRET_KEY.encode('utf-8'),
        msg = os.urandom(32),
        digestmod = 'sha256',
    ).hexdigest()

    return authenticator
