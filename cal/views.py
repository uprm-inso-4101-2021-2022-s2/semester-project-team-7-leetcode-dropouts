from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.conf.urls.static import static
from django.conf import settings


def index(request):
    # return HttpResponse("Hello habibi, run keiven template eventually")
    return render(request, 'index.html')

def tasks(request):

    return render(request, 'task.html')


def pomodoro(request):

    return render(request, 'pomodoro.html')

def signin(request):

    return render(request, 'signin.html')

def signup(request):

    return render(request, 'signup.html')