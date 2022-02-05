from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webdev.tasks.forms import NewTaskForm
from webdev.tasks.models import Task

def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:home'))
        else:
            pending_tasks = Task.objects.filter(done=False).all()
            return render(request, 'tasks/home.html', {'form': form, 'pending_tasks': pending_tasks}, status=400)
    pending_tasks = Task.objects.filter(done=False).all()
    return render(request, 'tasks/home.html', {'pending_tasks': pending_tasks})
