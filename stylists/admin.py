"""Imports from django and stylist model."""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Stylist


@admin.register(Stylist)
class StylistAdmin(ModelAdmin):
    """
    Stylist model view on django admin for admin user.
    """

    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
