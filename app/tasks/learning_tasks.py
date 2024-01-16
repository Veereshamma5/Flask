import time
from celery.utils.log import get_task_logger
from app.tasks.base_celery import cdp_app_celery, on_failure, on_success
from app.mailers.learning_mailer import LearningMailer

logger = get_task_logger(__name__)


@cdp_app_celery.task(bind=True, queue='send_new_learning_email')
def send_new_learning_email(unused_arg, to_email, recipient_name, skill_name):
    print("In send_email_method")
    try:
        print("Inside try block")
        logger.info('Received task - send_new_learning_email')
        learning_mailer = LearningMailer()
        learning_mailer.send_new_learning_email(to_email, recipient_name, skill_name)
    except Exception as ex:
        logger.error(ex, exc_info=True)
        raise ex
