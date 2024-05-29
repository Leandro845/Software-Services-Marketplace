from .models import SoftwereMaker, ExpenseManagementMaker, GroupRevenueMaker  # Importing models
from django.db.models.signals import post_save  # Importing post_save signal
from django.dispatch import receiver  # Importing receiver decorator
from django.core.mail import send_mail  # Importing send_mail function
from django.conf import settings  # Importing settings module


# Signal handler for SoftwereMaker model
@receiver(post_save, sender=SoftwereMaker)
def send_softwere_maker_email(sender, instance, created, **kwargs):
    if created:
        # Composing email subject
        subject = 'Budget Received Successfully! 🌟'
        
        # Composing email message
        message = f'Hello {instance.name_surname},\n\nYour budget has been received successfully.\n\nThank you for your contribution.'
        
        # Getting sender's email address from settings
        email_from = settings.EMAIL_HOST_USER
        
        # Creating a list of recipient email addresses
        recipient_list = [instance.email_client]

        # Sending email
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)


# Signal handler for ExpenseManagementMaker model
@receiver(post_save, sender=ExpenseManagementMaker)
def send_expense_management_maker_email(sender, instance, created, **kwargs):
    if created:
        # Composing email subject
        subject = 'Budget Received Successfully! 🌟'
        
        # Composing email message
        message = f'Hello {instance.contact_name},\n\nYour budget has been received successfully.\n\nThank you for your contribution.'
        
        # Getting sender's email address from settings
        email_from = settings.EMAIL_HOST_USER
        
        # Creating a list of recipient email addresses
        recipient_list = [instance.contact_email]

        # Sending email
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)


# Signal handler for GroupRevenueMaker model
@receiver(post_save, sender=GroupRevenueMaker)
def send_group_revenue_maker_email(sender, instance, created, **kwargs):
    if created:
        # Composing email subject
        subject = 'Budget Received Successfully! 🌟'
        
        # Composing email message
        message = f'Hello {instance.contact_name_second},\n\nYour budget has been received successfully.\n\nThank you for your contribution.'
        
        # Getting sender's email address from settings
        email_from = settings.EMAIL_HOST_USER
        
        # Creating a list of recipient email addresses
        recipient_list = [instance.contact_email_second]

        # Sending email
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
