from django.conf.urls import url
from django.urls import include, path
from django.urls import reverse
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'logout'

urlpatterns = [
    path('', views.logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
