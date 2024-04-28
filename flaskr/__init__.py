from http.client import NOT_FOUND, OK, BAD_REQUEST

from flask import Flask

from flaskr.tasks import get_employee


def create_app():
    return Flask(__name__)


app = create_app()


@app.route("/health", methods=["GET"])
def health():
    return "pong", OK


ping = app.route("/ping", methods=["GET"])(health)


@app.route("/employees/<employee_id>", methods=["GET"])
def employees(employee_id):
    if not employee_id.isdigit():
        return {"error": {"message": f"Bad request"}}, BAD_REQUEST
    employee = _get_employee(employee_id)
    if employee is None:
        return {"error": {"message": f"No employee number {employee_id}"}}, NOT_FOUND
    return employee


def _get_employee(employee_id):
    return get_employee.delay(employee_id).get(timeout=5)
