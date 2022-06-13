"""Imports from django and stylist model."""
from django.shortcuts import render
from .models import Stylist


def stylists(request):
    """
    Function to view stylist page.

    Stylists displayed in order of years experience.
    Most experienced stylist first.
    """
    stylist = Stylist.objects.all().order_by('-years_experience')

    context = {
        'stylists': stylist
    }

    return render(request, 'stylists/stylists.html', context)
