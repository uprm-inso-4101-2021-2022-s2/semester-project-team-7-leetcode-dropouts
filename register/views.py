from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib import messages
def register(request):
    return HttpResponse("Register Page")


def signin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth

    return render(request, 'signin.html')

def signup(request):

    if request.method == 'POST':
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        # pass1 = request.POST.get('pass1')
        # pass2 = request.POST.get('pass2')
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        NewUser = User.objects.create(username=username, email=email, password=pass1)
        NewUser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')

    return render(request, 'signup.html')

def signout(request):
    pass

