from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'home'

urlpatterns = [
    path('home/', views.get_home),
]
