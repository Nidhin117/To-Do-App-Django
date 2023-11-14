from typing import Any
from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin #this is to stop access to pages if not logged in

# Create your views here.
# def tasklist(request):
#     return HttpResponse('To Do list') 

#ListView expects a default template _list.html
#so we will create task_list.html in templates file
#No need to connect that .html with the view
#as ListView already knows which html to look for

class TaskList(LoginRequiredMixin,ListView):
    #LoginRequiredMixin stops access to URL if user is not logged in
    model = Task
    context_object_name='tasks' #this can be referred to as tasks in .html file instead of object_list

#this function is to make sure items belonging to logged in user are displayed and not all items
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        return context



class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name='details'
    #template_name = 'base/task.html' to specify custom template for this class view

#model form creates the specified fields of a model as a form, for editing purpose
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = '__all__'
    success_url= reverse_lazy('tasks') #if item is created, just send user back to URL with name tasks(Tasklist)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    success_url= reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name='task'
    success_url= reverse_lazy('tasks')

#https://ccbv.co.uk/projects/Django/4.2/django.contrib.auth.views/LoginView/
class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields= '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')