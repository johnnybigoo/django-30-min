from django.http import HttpResponse
from django.shortcuts import render
from webdev.tasks.forms import NewTaskForm


def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tasks/home.html')
