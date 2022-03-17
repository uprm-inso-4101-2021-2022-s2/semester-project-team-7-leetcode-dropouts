from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from django.conf import settings


def index(request):
    # return HttpResponse("Hello habibi, run keiven template eventually")
    return render(request, 'index.html')