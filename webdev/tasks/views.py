from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webdev.tasks.forms import NewTaskForm, TaskForm
from webdev.tasks.models import Task

def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:home'))
        else:
            pending_tasks = Task.objects.filter(done=False).all()
            tasks_done = Task.objects.filter(done=True).all()
            return render(
                request, 'tasks/home.html',
                {
                    'form': form,
                    'pending_tasks': pending_tasks,
                    'tasks_done': tasks_done,
                },
                status=400)
    pending_tasks = Task.objects.filter(done=False).all()
    tasks_done = Task.objects.filter(done=True).all()
    return render(request, 'tasks/home.html',
                  {
                      'pending_tasks': pending_tasks,
                      'tasks_done': tasks_done,
                  })

def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('tasks:home'))