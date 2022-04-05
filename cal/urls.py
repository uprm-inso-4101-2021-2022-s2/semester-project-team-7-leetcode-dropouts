from django.urls import path

from . import views

from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('tasks/', views.tasks, name = 'tasks'),
    path('pomodoro/', views.pomodoro, name = 'pomodoro'),
]