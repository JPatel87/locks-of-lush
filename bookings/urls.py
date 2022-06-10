"""Imports from django and bookings views"""
from django.urls import path
from bookings import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('add/', views.add_bookings, name='add_bookings'),
    path('edit/<booking_id>', views.edit_bookings, name='edit_bookings'),
    path('delete/<booking_id>', views.delete_bookings, name='delete_bookings')
]
