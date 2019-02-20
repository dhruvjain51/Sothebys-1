from django.conf.urls import url
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'product'

urlpatterns = [
    path('<int:id>/', views.get_product),
]

urlpatterns += staticfiles_urlpatterns()
