from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime

from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend

logger = get_task_logger(__name__)


@shared_task(name='tasks.send_email', bind=True, retry_kwargs={'max_retries': 3})
def send_email(self, email):
    mailbox = email.mailbox
    template = email.template
    backend = EmailBackend(host=mailbox.host,
                           port=mailbox.port,
                           username=mailbox.login,
                           password=mailbox.password,
                           use_ssl=mailbox.use_ssl,
                           fail_silently=False)
    email_to_send = EmailMessage(subject=template.subject,
                                 body=template.text,
                                 from_email=mailbox.email_from,
                                 to=email.to,
                                 cc=email.cc,
                                 bcc=email.bcc,
                                 connection=backend,
                                 reply_to=email.reply_to)
    if template.attachment:
        email_to_send.attach_file(template.attachment)
    try:
        success = email_to_send.send(fail_silently=False)
        if success:
            email.sent_date = datetime.now()
            email.save()
        else:
            raise self.retry()
    except Exception as e:
        logger.error(f"Error while sending message {email.id}: {e}")
        raise self.retry(exc=e)

