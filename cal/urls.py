from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('tasks/', views.tasks, name = 'tasks'),
    path('pomodoro/', views.pomodoro, name = 'pomodoro'),
    path('signin/', views.signin, name = 'signin'),
]