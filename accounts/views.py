from django.shortcuts import render
from .models import Buyer, Seller
from django.http import HttpResponse
from .models import Buyer, Seller
from django.http import JsonResponse
from .forms import BuyerForm, SellerForm
from django.views.decorators.csrf import csrf_exempt

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
        buyer = Buyer.objects.get(pk=id)
        form = BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


def get_sellers(request):
    data = list(Seller.objects.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_sellers_by_id(request, id):
    if request.method == 'GET':
        data = list(Seller.objects.values().filter(id = id))
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        seller = Seller.objects.get(pk=id)
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
