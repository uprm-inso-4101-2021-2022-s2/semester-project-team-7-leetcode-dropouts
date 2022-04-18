from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.conf.urls.static import static
from django.conf import settings


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task

from django.urls import reverse_lazy

def index(request):
    # return HttpResponse("Hello habibi, run keiven template eventually")
    return render(request, 'index.html')

def pomodoro(request):

    return render(request, 'pomodoro.html')


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasklist.html'

# def tasks(request):
#     return render(request, 'task.html')

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'task_form.html'

class TaskUpdate(UpdateView):
    template_name = 'task_form.html'
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')