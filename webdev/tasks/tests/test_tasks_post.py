import pytest
from django.urls import reverse
from webdev.tasks.models import Task


@pytest.fixture
def response(client, db):
    resp = client.post(reverse('tasks:home'), data={'name': 'Task'})
    return resp


def test_task_existent_db(response):
    assert Task.objects.exists()

def test_redirecting_after_saving(response):
    assert response.status_code == 302


@pytest.fixture
def response_invalid_data(client, db):
    resp = client.post(reverse('tasks:home'), data={'name': ''})
    return resp


def test_task_not_existent_db(response_invalid_data):
    assert not Task.objects.exists()

def test_page_with_invalid_data(response_invalid_data):
    assert response_invalid_data.status_code == 400
