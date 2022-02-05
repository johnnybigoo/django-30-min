import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains


@pytest.fixture
def response(client):
    resp = client.get(reverse('tasks:home'))
    return resp


def test_status_code(response):
    assert response.status_code == 200


def test_form_present(response):
    assertContains(response, '<form')


def test_save_button_present(response):
    assertContains(response, '<button type="submit"')

