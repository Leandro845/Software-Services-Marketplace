from celery import Celery
from celery.schedules import crontab
import os

# Set the Django settings module for the Celery app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projects.settings')

# Create a Celery instance
app = Celery('projects')

# Disable UTC and set timezone to America/Sao_Paulo
app.conf.enable_utc = False
app.conf.update(timezone='America/Sao_Paulo')

# Load Celery settings from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in all installed apps
app.autodiscover_tasks()

# Schedule a periodic task to send happy holidays email
app.conf.beat_schedule = {
    'send_happy_holidays': {
        'task': 'main_app.tasks.happy_holidays_email',
        'schedule': crontab(minute=0, hour=0, day_of_month=25, month_of_year=12),
    }
}

# Define a debug task
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
