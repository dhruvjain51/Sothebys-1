from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'product'

urlpatterns = [
    path('product/<int:id>/', views.get_paintings),
    path('product/more_by/<int:id>/', views.get_all_by_artist),
    path('product/create/', views.create_painting),
]
