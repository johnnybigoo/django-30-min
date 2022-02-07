import pytest
from django.urls import reverse

from webdev.tasks.models import Task


@pytest.fixture
def task(db):
        return Task.objects.create(name='Task 1', done='True')


@pytest.fixture
def response(client, task):
    resp = client.post(
        reverse('tasks:delete', kwargs={'task_id': task.id}),
    )
    return resp

def test_delete_task(response):
    assert not Task.objects.exists()