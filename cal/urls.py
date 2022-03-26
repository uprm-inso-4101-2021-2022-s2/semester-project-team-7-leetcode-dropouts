from django.urls import path

from . import views

from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('tasks/', views.tasks, name = 'tasks'),
    path('pomodoro/', views.pomodoro, name = 'pomodoro'),
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_DOC_ROOT}),
]