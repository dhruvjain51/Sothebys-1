from django.shortcuts import render
from .models import Buyer, Seller
from django.http import HttpResponse
from .models import Buyer, Seller
from django.http import JsonResponse
from .forms import BuyerForm
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
