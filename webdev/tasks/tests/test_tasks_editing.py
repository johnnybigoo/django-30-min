import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tasks.models import Task


@pytest.fixture
def pending_task(db):
        return Task.objects.create(name='Task 1', done='False')


@pytest.fixture
def response_with_pending_task(client, pending_task):
    resp = client.post(
        reverse('tasks:detail', kwargs={'task_id': pending_task.id}),
        data={'done': 'true', 'name': f'{pending_task.name}-edited'}
    )
    return resp

def test_status_code(response_with_pending_task):
    assert response_with_pending_task.status_code == 302

def test_task_done(response_with_pending_task):
    assert Task.objects.first().done

@pytest.fixture
def task_done(db):
        return Task.objects.create(name='Task 1', done='True')


@pytest.fixture
def response_with_task_done(client, task_done):
    resp = client.post(
        reverse('tasks:detail', kwargs={'task_id': task_done.id}),
        data={'name': f'{task_done.name}-edited'}
    )
    return resp


def test_pending_task(response_with_task_done):
    assert not Task.objects.first().done

