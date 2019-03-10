from django.conf.urls import url
from django.urls import include, path
from django.urls import reverse
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'login'

urlpatterns = [
    path('', views.get_login, name='login-home'),
    path('s/', views.get_signup),
]

urlpatterns += staticfiles_urlpatterns()
