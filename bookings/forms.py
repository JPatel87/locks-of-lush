"""Imports from django and booking model."""
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    Class for date input widget
    """
    input_type = 'date'


class BookingFormAdmin(forms.ModelForm):
    """
    Booking form used to book appointments.

    This form is for the admin user only.
    It allows the admin to view all users
    and make bookings for them.
    """

    class Meta:
        """
        Class to define booking form fields, labels and widgets.
        """

        model = Booking
        fields = [
            'user',
            'first_name',
            'last_name',
            'date',
            'time',
            'stylist',
            'service']
        labels = {
            'first_name': 'Client First Name',
            'last_name': 'Client Last Name'
        }
        widgets = {
            'date': DateInput(),
        }

    def clean_first_name(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['last_name'].capitalize()

class BookingForm(forms.ModelForm):
    """
    Booking form used to book appointments.

    This form is for a non-admin user.
    It does not allow the user to see
    the user field hence only allowing them
    to control their own bookings.
    """

    class Meta:
        """
        Class to define booking form fields, labels and widgets.
        """
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'date',
            'time',
            'stylist',
            'service']
        labels = {
            'first_name': 'Client First Name',
            'last_name': 'Client Last Name'
        }
        widgets = {
            'date': DateInput(),
        }

    def clean_first_name(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['last_name'].capitalize()
