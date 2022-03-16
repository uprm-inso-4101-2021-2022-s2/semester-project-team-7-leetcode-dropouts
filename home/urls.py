# cal/urls.py

from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path(r'^$', views.index, name='index'),
]