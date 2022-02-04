import pytest
from django.urls import reverse
from webdev.tasks.models import Task


@pytest.fixture
def response(client, db):
    resp = client.post(reverse('tasks:home'), data={'name': 'Task'})
    return resp


def test_task_existent_db(response):
    assert Task.objects.exists()


def test_form_present(response):
    assertContains(response, '<form')


def test_save_button_present(response):
    assertContains(response, '<button type="submit"')
