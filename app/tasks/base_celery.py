from celery import Celery
from config import BaseConfig

cdp_app_celery = Celery(
    backend=BaseConfig.CELERY_RESULT_BACKEND,
    broker=BaseConfig.CELERY_BROKER_URL
)


def on_failure():
    print("Email trigger is failed")


def on_success():
    print("Email gets triggered successfully!!")
