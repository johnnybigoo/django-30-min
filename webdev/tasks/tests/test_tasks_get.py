import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tasks.models import Task

@pytest.fixture
def response(client, db):
    resp = client.get(reverse('tasks:home'))
    return resp


def test_status_code(response):
    assert response.status_code == 200


def test_form_present(response):
    assertContains(response, '<form')


def test_save_button_present(response):
    assertContains(response, '<button type="submit"')


@pytest.fixture
def pending_task_list(db):
    tasks =  [
        Task(name='Task 1', done='False'),
        Task(name='Task 2', done='False'),
    ]
    Task.objects.bulk_create(tasks)
    return tasks


@pytest.fixture
def response_with_task_list(client, pending_task_list):
    resp = client.get(reverse('tasks:home'))
    return resp

def test_pending_task_list_present(response_invalid_data, pending_task_list):
    for task in pending_task_list:
        assertContains(response_invalid_data, task.name)

