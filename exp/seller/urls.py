from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'seller'

urlpatterns = [
    path('seller/create/', views.create_seller),
]
