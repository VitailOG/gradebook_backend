import pytest

from rest_framework.test import APIClient


pytestmark = [pytest.mark.django_db]


def test_get():
    c = APIClient()
    r = c.get('http://127.0.0.1:8000/methodist/ps/')
    assert r.status_code == 200


def test_create():
    c = APIClient()
    r = c.post('http://127.0.0.1:8000/methodist/ps/', {"name": "asdd"})
    assert r.status_code == 201
