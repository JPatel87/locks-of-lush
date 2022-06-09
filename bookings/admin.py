"""Imports from django and booking model."""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    """
    Booking model view on django admin for admin user.
    """
    list_display = (
        'date',
        'time',
        'stylist',
        'first_name',
        'last_name',
        'service'
        )
