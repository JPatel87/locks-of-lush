"""Imports from django and models."""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Service

# Register your models here.


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    """
    Service model view on django admin for admin user.
    """

    list_display = ('name', 'service_type', 'price')
    list_filter = ('service_type',)
