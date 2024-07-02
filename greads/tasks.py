from django.core.mail import send_mail
from greads.celery import app


@app
def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        '42ikromjon@gmail.com',
        recipient_list
    )
