from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('api/v1/buyers/', views.get_buyers, name='get_buyers'),
    path('api/v1/buyers/<int:id>/', views.get_buyers_by_id),
    path('api/v1/sellers/', views.get_sellers, name='get_sellers'),
    path('api/v1/sellers/<int:id>/', views.get_sellers_by_id),
    path('api/v1/sellers/create/', views.create_seller),
    path('api/v1/sellers/login/', views.login_seller),
    path('api/v1/auth', views.check_auth),
]
