"""Imports from django and views"""
from django.urls import path
from services.views import services, add_services, edit_services, delete_services


urlpatterns = [
    path('', services, name='services'),
    path('add/', add_services, name='add_services'),
    path('edit/<service_id>', edit_services, name='edit_services'),
    path('delete/<service_id>', delete_services, name='delete_services')
]
