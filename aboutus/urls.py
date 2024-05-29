from django.urls import path
from . import views

# URL patterns for the application
urlpatterns = [
    # URL pattern for the 'about' page
    path('aboutus/', views.about, name='about'),
    # URL pattern for the 'click' page
    path('click/', views.click, name='click'),
    # URL pattern for the 'wedo' page
    path('wedo/', views.wedo, name='wedo')
]
