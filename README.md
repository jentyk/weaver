# Software Developer Task

## Description

System is design using Microservices architecture.\
It utilises Celery Distributed Task Queue with Redis as a Message Broker as well as the Result Backend and MongoDB as database.

## Requirements

- Python 3.11.8
- Packages: flask, gunicorn, celery, pymongo, python-dotenv, pytest, pytest-flask, mongomock, pytest-mock
- Docker Images: mongo, mongo-express, redis

## Installation

- Install Python if you haven't already. You can download Python from the official website at: https://www.python.org/downloads/.
- Clone the project into a directory of you choice.

`$ git clone PROJECT_URL <your project directory>`

- Go into the project directory:

`$ cd <your project directory>`

- Upgrade pip.

`$ pip install --upgrade pip`

- Install pipenv.

`$ pip install pipenv`

- Create virtual environment and install dependencies.

`$ pipenv install --dev`

## Running tests

Run tests to check that everything is complete.

`$ pipenv run pytest tests`

## Running containerised version of the system

`$ docker compose up -d`

You may need to wait a few seconds for the system to become ready.

## Usage

You can check content of db by visiting http://localhost:8081/

You can check if server is alive by visiting http://localhost:8080/ping

You can get information about employee by visiting http://localhost:8080/employees/198

## Testing Strategies

Basic unit and integration tests has been included in the project.\
What is missing is automated End To End test which could be implemented using pytest,
pytest-docker and Docker Compose configuration I provided.\
Unfortunately pytest-docker plugin does not work on my MacBook ATM, 
the most likely due to depreciation of Python version of Docker Compose in a favor of the one written in Golang.\
Another type of test which could be useful would be performance test of the system carried on Kubernetes cluster.
