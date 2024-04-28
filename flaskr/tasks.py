from celery import Celery
import logging
import os

from dotenv import load_dotenv
import pymongo

load_dotenv()

logger = logging.getLogger(__name__)

db = pymongo.MongoClient(os.environ["ME_CONFIG_MONGODB_URL"], 27017).weaverlabs

REDIS_URL = os.environ["REDIS_URL"]
app = Celery("tasks", broker=REDIS_URL, backend=REDIS_URL)  # , include="tasks")


@app.task(name="tasks.get_employee")
def get_employee(employee_id):
    return _get_employee(employee_id)


def _get_employee(employee_id):
    return db.employees.find_one(
        {"EMPLOYEE_ID": employee_id}, projection={"_id": False}
    )
