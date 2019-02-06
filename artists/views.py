from django.shortcuts import render
from .models import Artist
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ArtistForm

# Create your views here.
def get_artists(request):
    data = list(Artist.objects.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_artists_by_id(request, id):
    if request.method == 'GET':
        data = list(Artist.objects.values().filter(id = id))
        return JsonResponse(data, safe=False)

@csrf_exempt
def create_artist(request):
    if request.method == 'POST':
        form_data = ArtistForm(request.POST)
        form_data.save()
        return HttpResponse(status=200)

@csrf_exempt
def update_artist(request, id):
    if request.method == 'POST':
        artist = Artist.objects.get(pk=id)
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


@csrf_exempt
def delete_artist(request, id):
    if request.method == 'POST':
        Artist.objects.get(pk=id).delete()
        return HttpResponse(status=200)
