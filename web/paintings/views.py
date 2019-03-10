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
        form = CreatePaintingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            medium = form.cleaned_data['medium']
            price = form.cleaned_data['price']
            artist = form.cleaned_data['artist']
            # Need to get the user that is currently logged in
            # seller = form.cleaned_data['seller']

            status = create_painting_exp_api(auth, title, image, description, medium, price, artist)

            if status == 200:
                message = "Your item has been added Successfully"
                return render(request, "create.html", {'form': form, 'message': message})
            else:
                message = "Sorry there was an error"
                return render(request, "create.html", {'form': form, 'message': message})

    if request.method == "GET":
        form = CreatePaintingForm()
        return render(request, "create.html", {'form': form, 'message': "Fill out all the fields to create your new listing."})


def create_painting_exp_api(auth, title, image, description, medium, price, artist):
    post_data = {'title': title, 'image': image, 'description': description,
                 'medium': medium, 'price': price, 'artist': artist}
    response = requests.post(
        'http://exp-api:8000/product/create/', data=post_data)
    json_data = json.loads(response.text)

    return response.text
    # Call Exp API, pass everything form data.
    # Get result, return json result
