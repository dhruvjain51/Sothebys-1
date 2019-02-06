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
        try:
            painting = Painting.objects.get(pk=id)

            if 'title' in request.POST:
                Painting.objects.filter(id = id).update(title = request.POST.get("title"))

            if 'image' in request.POST:
                Painting.objects.filter(id = id).update(image = request.POST.get("image"))

            if 'description' in request.POST:
                Painting.objects.filter(id = id).update(description = request.POST.get("description"))

            if 'medium' in request.POST:
                Painting.objects.filter(id = id).update(medium = request.POST.get("medium"))

            if 'price' in request.POST:
                Painting.objects.filter(id = id).update(price = request.POST.get("price"))

            if 'artist' in request.POST:
                Painting.objects.filter(id = id).update(artist = request.POST.get("artist"))

            return HttpResponse(status=200)

        except:
            return HttpResponse(status=400)

@csrf_exempt
def delete_painting(request, id):
    if request.method == 'POST':
        Painting.objects.get(pk=id).delete()
        return HttpResponse(status=200)
