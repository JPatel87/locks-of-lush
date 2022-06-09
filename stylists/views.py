"""Imports from django and stylist model"""
from django.shortcuts import render
from .models import Stylist


def get_stylists_page(request):
    """
    Function to view stylist page.

    Stylists displayed in order of years experience
    """
    stylist = Stylist.objects.all().order_by('-years_experience')

    context = {
        'stylists': stylist
    }

    return render(request, 'stylists/stylists.html', context)
