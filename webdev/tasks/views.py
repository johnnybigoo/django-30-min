from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webdev.tasks.forms import NewTaskForm


def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks: home'))
        else:
           return render(request, 'tasks/home.html', {'form': form}, status=400)

    return render(request, 'tasks/home.html')
