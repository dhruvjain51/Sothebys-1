from django.conf.urls import url
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'product'

urlpatterns = [
    # path('', views.get_home),
]

urlpatterns += staticfiles_urlpatterns()
