from celery.decorators import task
from .email import send_review_email
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name='send_email_review_task')    #This name is the name of the task we called  in the forms
def send_email_review_task(name,email,review):
    logger.info("sent review email")
    return send_review_email(name,email,review)
