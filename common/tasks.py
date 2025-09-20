from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
import uuid

@shared_task
def generate_report_task(report_name=None):
    report_name = report_name or f"report-{uuid.uuid4()}"
    path = f"/tmp/{report_name}.txt"
    with open(path, "w") as f:
        f.write(f"Report generated at {timezone.now().isoformat()}")
    return {'report': path}

@shared_task
def scheduled_cleanup_task():
    deleted = 0
    return {'deleted': deleted}

@shared_task
def send_email_task(to_email, subject='Hello', body='Body'):
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [to_email])
    return True
