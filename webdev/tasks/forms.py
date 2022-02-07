from django.forms import ModelForm

from webdev.tasks.models import Task


class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'done']