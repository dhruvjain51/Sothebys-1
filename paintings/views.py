from django.shortcuts import render
from .models import Painting
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PaintingForm

# Create your views here.
def get_paintings(request):
    data = list(Painting.objects.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_paintings_by_id(request, id):
    if request.method == 'GET':
        data = list(Painting.objects.values().filter(id = id))
        return JsonResponse(data, safe=False)

@csrf_exempt
def create_painting(request):
    if request.method == 'POST':
        form_data = PaintingForm(request.POST)
        form_data.save()
        return HttpResponse(status=200)

@csrf_exempt
def update_painting(request, id):
    if request.method == 'POST':
        painting = Painting.objects.get(pk=id)
        form = PaintingForm(request.POST, instance=painting)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


@csrf_exempt
def delete_painting(request, id):
    if request.method == 'POST':
        Painting.objects.get(pk=id).delete()
        return HttpResponse(status=200)
