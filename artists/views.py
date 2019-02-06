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
        try:
            artist = Artist.objects.get(pk=id)

            if 'name' in request.POST:
                Artist.objects.filter(id = id).update(name = request.POST.get("name"))

            if 'image' in request.POST:
                Artist.objects.filter(id = id).update(image = request.POST.get("image"))

            if 'description' in request.POST:
                Artist.objects.filter(id = id).update(description = request.POST.get("description"))

            if 'nationality' in request.POST:
                Artist.objects.filter(id = id).update(nationality = request.POST.get("nationality"))

            if 'dob' in request.POST:
                Artist.objects.filter(id = id).update(dob = request.POST.get("dob"))

            if 'dod' in request.POST:
                Artist.objects.filter(id = id).update(dod = request.POST.get("dod"))

            return HttpResponse(status=200)

        except:
            return HttpResponse(status=400)


@csrf_exempt
def delete_artist(request, id):
    if request.method == 'POST':
        Artist.objects.get(pk=id).delete()
        return HttpResponse(status=200)
