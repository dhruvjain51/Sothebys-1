from django.conf.urls import url
from django.urls import include, path
from django.urls import reverse
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'paintings'

urlpatterns = [
    path('all/', views.all_paintings, name='all_paintings'),
    path('create/', views.create_painting, name='create_painting'),
    path('search/', views.get_search_results, name='search_paintings')
]

urlpatterns += staticfiles_urlpatterns()
