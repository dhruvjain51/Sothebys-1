from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('api/v1/buyers/', views.get_buyers),
    path('api/v1/buyers/<int:id>/', views.get_buyers_by_id),
]
