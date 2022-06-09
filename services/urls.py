"""Imports from django and service views"""
from django.urls import path
from services import views


urlpatterns = [
    path('', views.services, name='services'),
    path('add/', views.add_services, name='add_services'),
    path('edit/<service_id>', views.edit_services, name='edit_services'),
    path('delete/<service_id>', views.delete_services, name='delete_services')
]
