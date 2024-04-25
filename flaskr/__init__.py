from http.client import OK

from flask import Flask


def create_app():
    return Flask(__name__)


app = create_app()


@app.route("/health")
def health():
    return "pong", OK
