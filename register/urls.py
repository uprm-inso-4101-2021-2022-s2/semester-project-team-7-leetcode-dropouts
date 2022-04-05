from django.urls import path, include

from . import views

urlpatterns = [
    path('disabled/', views.register, name = 'register'),
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('signout/', views.signout, name = 'signout'),
]