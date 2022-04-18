from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from . import createUserForm
from . import views
from cal import urls

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
def signin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.error(request, "Bad credentials!")
            return redirect('signin')

    return render(request, 'signin.html')

class RegisterForm(FormView):

    template_name = 'signup.html'
    form_class = UserCreationForm
    redirect_authenthicated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterForm, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterForm, self).get(*args, **kwargs)

# def signup(request):

#     if request.method == 'POST':
#         # username = request.POST.get('username')
#         # email = request.POST.get('email')
#         # pass1 = request.POST.get('pass1')
#         # pass2 = request.POST.get('pass2')
#         username = request.POST['username']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         NewUser = User.objects.create(username=username, email=email, password=pass1)
#         NewUser.save()

#         messages.success(request, "Your Account has been successfully created.")

#         return redirect('signin')

#     return render(request, 'signup.html')














# def signup(response):
#     if response.user.is_authenticated:
#         return redirect("/")

#     else:
#         if response.method == "POST":
#             form = RegisterForm(response.POST)
#             if form.is_valid():
#                 new_user = form.save()
#                 # messages.info(response, "Thanks for registering. You are now logged in.")
#                 new_user = authenticate(username=form.cleaned_data['username'],
#                                         password=form.cleaned_data['password1'],
#                                         )
#                 login(response, new_user)
#             return redirect("homepage")
#         else:
#             form = RegisterForm()

#         return render(response, "register/register.html", {"form": form})

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')