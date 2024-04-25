from http.client import OK

import pytest

from flaskr import app as the_app


@pytest.fixture
def app():
    return the_app


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == OK
