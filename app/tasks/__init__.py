from app.tasks.learning_tasks import send_new_learning_email
from app.tasks.base_celery import cdp_app_celery, on_failure, on_success
