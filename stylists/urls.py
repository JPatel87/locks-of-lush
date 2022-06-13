"""Imports from django and stylist views."""
from django.urls import path
from stylists import views

# Url link to the stylist home page
urlpatterns = [
    path('', views.stylists, name='stylists')
]
