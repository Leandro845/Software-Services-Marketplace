from pathlib import Path
from django.contrib.messages import constants
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Secret key used for Django security. Do not share this key.
SECRET_KEY = 'django-insecure-qf4jo1bcympph93#ees-7q6%r0g)e$a6f#ck53puv@b0zrhb0@'

# SECURITY WARNING: don't run with debug turned on in production!
# Debug mode. Do not activate in production environment.
DEBUG = True

# List of allowed hosts for the Django application.
ALLOWED_HOSTS = ['https://localhost:8000/', 'https://127.0.0.1:8000/']


# Application definition

# Installed applications in the Django project.
INSTALLED_APPS = [
    'django.contrib.admin',  # Django Admin
    'django.contrib.auth',  # Django Authentication
    'django.contrib.contenttypes',  # Django Content Types
    'django.contrib.sessions',  # Django Sessions
    'django.contrib.messages',  # Django Messages
    'django.contrib.staticfiles',  # Django Static Files
    'django_celery_results',  # Celery Results for Django
    'django_celery_beat',  # Celery Beat for Django
    'main_app',  # Main Application
    'aboutus',  # About Us
    'budgets',  # Budgets
    'pm',  # Project Management
    'axes'  # Protection against attacks
]

# Middleware processing HTTP requests.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security Middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Django Session Middleware
    'django.middleware.common.CommonMiddleware',  # Django Common Middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF Protection Middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Django Authentication Middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Django Messages Middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking Protection Middleware
    'axes.middleware.AxesMiddleware'  # Protection against attacks Middleware
]


# Authentication configuration

# Authentication backends used by Django
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',  # Protection against attacks Backend
    'django.contrib.auth.backends.ModelBackend'  # Default Django Authentication Backend
]


# Django project URL configuration
ROOT_URLCONF = 'projects.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR, 'templates').joinpath()],  # Project templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'projects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Database configuration for PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],  # Database name
        'USER': os.environ['DB_USER'],  # User
        'PASSWORD': os.environ['DB_PASSWORD'],  # Password
        'HOST': os.environ['DB_HOST'],  # Host
        'PORT': os.environ['DB_PORT'],  # Port
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# Language and timezone settings
LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Static files settings
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    Path(BASE_DIR, 'templates/static').joinpath()
]
MEDIA_ROOT = Path(BASE_DIR, 'media').joinpath()
MEDIA_URL = 'media/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Messages

# Message tags mapping to CSS classes
MESSAGE_TAGS = {
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
}

# Email

# Email configuration
# Setting the email backend
EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
# Setting the email host
EMAIL_HOST = os.environ['EMAIL_HOST']
# Setting the email port
EMAIL_PORT = os.environ['EMAIL_PORT']
# Setting whether to use TLS for email
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
# Setting the email host user (e.g., Gmail email)
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']  # Your Gmail email here
# Setting the email host password
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']  # Your email password here

# Celery

# Celery configuration
# Setting the Celery broker URL
CELERY_BROKER_URL = 'redis://localhost:6379/0'
# Setting the Celery result backend
CELERY_RESULT_BACKEND = 'django-db'
# Setting the accepted content types for Celery tasks
CELERY_ACCEPT_CONTENT = ['json']
# Setting the result serializer for Celery tasks
CELERY_RESULT_SERIALIZER = 'json'
# Setting the task serializer for Celery tasks
CELERY_TASK_SERIALIZER = 'json'
# Setting the concurrency level for Celery workers
CELERY_WORKER_CONCURRENCY = 4
# Setting the maximum number of tasks each Celery worker process can execute before it's replaced
CELERYD_MAX_TASKS_PER_CHILD = 100


# Celery Beat

# Celery Beat configuration
CELERY_TIMEZONE = TIME_ZONE


# Axes

# django-axes settings
AXES_FAILURE_LIMIT = 5  # Limit of attempts before blocking
AXES_COOLOFF_TIME = 1  # Wait time in hours before releasing the lock
AXES_LOCKOUT_PARAMETERS = ['username', 'ip_address']  # Block by combination of username and IP
AXES_RESET_ON_SUCCESS = True  # Resets the failure counter after a successful login
AXES_USERNAME_FORM_FIELD = 'username'  # Form field used for username


# Other security settings

# Secure SSL redirect
SECURE_SSL_REDIRECT = True  # Redirects all HTTP traffic to HTTPS

# HTTP Strict Transport Security (HSTS) settings
SECURE_HSTS_SECONDS = 31536000  # HSTS duration, in seconds (1 year)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include subdomains in HSTS policy
SECURE_HSTS_PRELOAD = True  # Enable HSTS preload list submission

# Clickjacking protection
X_FRAME_OPTIONS = 'DENY'  # Deny any framing

# Secure content type settings
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from MIME-sniffing a response away from the declared content type

# XSS (Cross-Site Scripting) protection
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filter in browsers
