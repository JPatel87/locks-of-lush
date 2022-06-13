"""Imports from django and home views."""
from django.urls import path
from home import views

# Url link to the home page
urlpatterns = [
    path('', views.home, name='home')
]
