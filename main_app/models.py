from django.db import models
from django.utils import timezone

class Client(models.Model):
    """
    Model representing a client's contact information and message.
    """
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone_number = models.CharField(max_length=20)
    message = models.TextField(max_length=2000)

    def __str__(self) -> str:
        """
        String representation of the client.
        """
        return self.name

class NewsLetterEmail(models.Model):
    """
    Model representing an email address subscribed to the newsletter.
    """
    email = models.EmailField(max_length=60)

    def __str__(self) -> str:
        """
        String representation of the email address.
        """
        return self.email

class NewsLetterContent(models.Model):
    """
    Model representing the content of a newsletter.
    """
    subject = models.CharField(max_length=1500)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        """
        String representation of the newsletter content.
        """
        return self.subject
