from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import NewsLetterContent, NewsLetterEmail
from django.conf import settings

@receiver(post_save, sender=NewsLetterContent)
def send_signals(sender, instance, created, **kwargs):
    """
    Signal receiver function to send email notification to all subscribers 
    when new content is added to the newsletter.
    
    Args:
    - sender: The model class sending the signal (NewsLetterContent)
    - instance: The actual instance being saved
    - created: A boolean; True if a new instance was created, False if an existing one was modified
    - kwargs: Additional keyword arguments
    """
    # If a new instance of NewsLetterContent is created
    if created:
        # Get email addresses of all newsletter subscribers
        emails = NewsLetterEmail.objects.values_list('email', flat=True)
        
        # Send email notification to each subscriber
        for email in emails:
            send_mail(
                '🔴New content',
                instance.subject,
                settings.EMAIL_HOST_USER,
                [email],
            )
