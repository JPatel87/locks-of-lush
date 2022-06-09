"""Imports from django and stylist views"""
from django.urls import path
from stylists import views


urlpatterns = [
    path('', views.stylists, name='stylists')
]
