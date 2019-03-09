from django.shortcuts import render
from .forms import SellerRegisterForm
from django.http import HttpResponseRedirect


# Create your views here.
def get_login(request):
    if request.method == "GET":
        return render(request, "login.html")


# Register for the seller
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
            message = "Success, you have been registered on Sothebys!"
    else:
        form = SellerRegisterForm()
        message = "We are excited as you join us"
    return render(request, "signup.html", {'form': form, 'message': message})
