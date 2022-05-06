from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.conf.urls.static import static
from django.conf import settings


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, Pomodorout

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

def index(request):
    # return HttpResponse("Hello habibi, run keiven template eventually")
    return render(request, 'index.html')

# def pomodoro(request):
#     # ob=Pomodorout.objects.get(id=2)





#     # return render(request,'pomodoro.html',{'ob':ob})
#     return render(request, 'pomodoro.html')


class Pomodoro(LoginRequiredMixin, ListView):
    model = Pomodorout
    context_object_name = 'Pomodorout'
    template_name = 'pomodoro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Pomodorout'] = context['Pomodorout'].filter(user=self.request.user)
        return context


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasklist.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
            # context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context

# def tasks(request):
#     return render(request, 'task.html')

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = {'title', 'description', 'complete', 'importance_raiting', 'due_dates'}
    success_url = reverse_lazy('tasks')
    template_name = 'task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'task_form.html'
    model = Task
    # fields = '__all__'
    fields = {'title', 'description', 'complete', 'importance_raiting', 'due_dates'}
    
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')