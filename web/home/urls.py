from django.conf.urls import url
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'home'

urlpatterns = [
    path('', views.get_home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
