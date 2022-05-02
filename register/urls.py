from django.urls import path, include

from . import views

urlpatterns = [
    # path('signin/', views.signin, name = 'signin'),
    path('signin/', views.CustomLoginView.as_view(), name = 'signin'),
    # path('signup/', views.signup, name = 'signup'),
    path('signup/', views.RegisterForm.as_view(), name = 'signup'),
    path('signout/', views.signout, name = 'signout'),
]