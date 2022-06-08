"""Imports from django and models."""
from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    """
    Service form used to add services.
    """

    class Meta:
        """
        Class to define service form fields and labels.
        """

        model = Service
        fields = ['name', 'service_type', 'price']
        labels = {
            'name': 'Service name',
            'price': 'Price (£)'
        }

    def clean_name(self):
        """
        Method to capitalize service names from service form.
        """
        return self.cleaned_data['name'].capitalize()
