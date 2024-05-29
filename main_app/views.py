from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Client, NewsLetterEmail, NewsLetterContent
from django.conf import settings
from django.contrib.messages import constants
from django.contrib import messages
from .tasks import send_news_lettwer


def index(request):
    """Render index page and process contact form."""
    if request.method == 'GET':
        return render(request, 'index.html')
    
    elif request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Phone Number')
        message = request.POST.get('Message')

        # Validate form data
        if not name and not email and not phone_number and not message:
            messages.add_message(request, constants.ERROR, '❌ You need to fill out all the fields.')
            return redirect('index')

        # Save client data to database
        cliente = Client(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message
        )
        cliente.save()
        
        # Send email notification
        send_mail(
            f'Cliente {name}',
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )

        return redirect('index')
      
def news_lettwer(request): 
    """Render index page and process newsletter subscription."""
    if request.method == 'GET':
        return render(request, 'index.html')
    
    elif request.method == 'POST':
        # Retrieve email from form
        email = request.POST.get('Email')

        # Validate email
        if not email:
            return redirect('index')
        
        # Save email to newsletter subscribers
        news = NewsLetterEmail(
            email=email
        )
        news.save()

        return redirect('index')
    
        
def send_news_lettwer_client(request):
    """Send newsletter to subscribed clients."""
    # Retrieve newsletter content
    contents = NewsLetterContent.objects.all()
    subject = 'New Content 📢'

    # Iterate through content and send to subscribers
    for conte in contents:
        emails = NewsLetterEmail.objects.values_list('email', flat=True)
        for email in emails:
            send_news_lettwer(
                subject, 
                conte.subject, 
                settings.EMAIL_HOST_USER, 
                email
            )
        
    # Delete sent content
    return contents.delete()
