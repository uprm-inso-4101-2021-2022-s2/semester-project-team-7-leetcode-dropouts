from django.urls import path

from . import views

from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('tasks/', views.TaskList.as_view(), name = 'tasks'),
    path('create-task/', views.TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', views.DeleteView.as_view(), name = 'task-delete'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name = 'task'),
    path('pomodoro/', views.Pomodoro.as_view(), name = 'pomodoro'),
]