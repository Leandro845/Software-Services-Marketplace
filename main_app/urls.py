from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for rendering index page and processing contact form
    path('news_letter/', views.news_lettwer, name='news_lettwer')  # URL pattern for managing newsletter subscriptions
]
