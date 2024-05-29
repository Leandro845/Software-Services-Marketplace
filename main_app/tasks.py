from celery import shared_task
from .models import Client, NewsLetterEmail
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_e(name, email, phone_number, message):
    """
    Task to save client data and send email notification.
    
    Args:
    - name: Name of the client
    - email: Email of the client
    - phone_number: Phone number of the client
    - message: Message from the client
    
    Returns:
    - True if email is sent successfully, False otherwise
    """
    # Save client data
    cliente = Client(name=name, email=email, phone_number=phone_number, message=message)
    cliente.save()
    
    # Send email notification
    send_ = send_mail(
        f'Cliente {name}',
        message,
        email,
        [settings.EMAIL_HOST_USER],
        fail_silently=False
    )
    
    return send_

@shared_task
def send_news_lettwer(subject, message, email_sender, email_recipient): 
    """
    Task to send newsletter email.
    
    Args:
    - subject: Subject of the email
    - message: Body of the email
    - email_sender: Sender's email address
    - email_recipient: Recipient's email address
    """
    send_mail(
        subject,
        message,
        email_sender, 
        [email_recipient],
        fail_silently=False
    )

@shared_task
def happy_holidays_email():
    """
    Task to send happy holidays email to all subscribers.
    """
    subject = 'Feliz Natal🎅'
    message = 'Desejamos a você um feliz Natal🎅 e um próspero ano novo🎆'

    # Get email addresses of all newsletter subscribers
    emails = NewsLetterEmail.objects.values_list('email', flat=True)
    
    # Send email to each subscriber
    for email in emails:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, 
            [email],
            fail_silently=False
        )
