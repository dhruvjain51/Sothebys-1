from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'artists'

urlpatterns = [
    path('api/v1/artists/', views.get_artists),
    path('api/v1/artists/<int:id>/', views.get_artists_by_id),
    path('api/v1/artists/create/', views.create_artist),
    path('api/v1/artists/<int:id>/update/', views.update_artist),
    path('api/v1/artists/<int:id>/delete/', views.delete_artist),
]
