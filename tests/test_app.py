from http.client import NOT_FOUND, OK

import mongomock

mongo_patcher = mongomock.patch()
mongo_patcher.start()

from flaskr.tasks import _get_employee, db

import pytest

from flaskr import app as flask_app


@pytest.fixture
def app():
    return flask_app


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == OK


def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == OK
    assert resp.text == "pong"


def test_no_employee(client, mocker):
    mocker.patch("flaskr._get_employee", _get_employee)
    resp = client.get("/employees/198")
    assert resp.status_code == NOT_FOUND


def test_no_employee(client, mocker):
    mocker.patch("flaskr._get_employee", _get_employee)
    resp = client.get("/employees/198")
    assert resp.status_code == NOT_FOUND
    assert resp.json == {"error": {"message": "No employee number 198"}}


def test_employee(client, mocker):
    mocker.patch("flaskr._get_employee", _get_employee)
    employee = {
        "EMPLOYEE_ID": "198",
        "FIRST_NAME": "Donald",
        "LAST_NAME": "OConnell",
        "EMAIL": "DOCONNEL",
        "PHONE_NUMBER": "650.507.9833",
        "HIRE_DATE": "21-JUN-07",
        "JOB_ID": "SH_CLERK",
        "SALARY": "2600",
        "COMMISSION_PCT": "-",
        "MANAGER_ID": "124",
        "DEPARTMENT_ID": "50",
    }
    db.employees.insert_one(employee.copy())
    resp = client.get("/employees/198")
    assert resp.status_code == OK
    assert resp.json == employee
