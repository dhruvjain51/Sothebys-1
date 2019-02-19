from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'paintings'

urlpatterns = [
    path('api/v1/paintings/', views.get_paintings),
    path('api/v1/paintings/<int:id>/', views.get_paintings_by_id),
    path('api/v1/paintings/create/', views.create_painting),
    path('api/v1/paintings/<int:id>/update/', views.update_painting),
    path('api/v1/paintings/<int:id>/delete/', views.delete_painting),
]
