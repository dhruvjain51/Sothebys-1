from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'home'

urlpatterns = [
    path('home/popular_paintings/', views.get_popular_paintings),
]
