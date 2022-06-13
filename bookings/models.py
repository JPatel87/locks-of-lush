"""Imports from django, user model imported."""
from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Booking model for booking database.
    """

    TIMESLOT_LIST = (
        (0, '10AM'),
        (1, '11AM'),
        (2, '12PM'),
        (3, '1PM'),
        (4, '2PM'),
        (5, '3PM'),
        (6, '4PM'),
        (7, '5PM'),
    )

    def validate_date(self):
        """
        Method to display error message if date selected is in the past.
        """
        if self < date.today():
            raise ValidationError("Date cannot be in the past")

    date = models.DateField(
        validators=[validate_date]
        )

    time = models.IntegerField(choices=TIMESLOT_LIST)
    stylist = models.ForeignKey(
        'stylists.Stylist',
        on_delete=models.CASCADE,
        )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    service = models.ForeignKey(
        'services.Service',
        on_delete=models.CASCADE,
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="timeslot")

    def __str__(self):
        """
        Method to display booking instance by date, time and stylist.
        """
        return f'{self.date} {self.get_time_display()} {self.stylist}'

    class Meta:
        """
        Class to ensure booking is classified as
        unique by date, time and stylist.
        """
        unique_together = ('date', 'time', 'stylist')

    @property
    def past_date(self):
        """
        Decorator to check if date is in the past.
        """
        today = date.today()
        if self.date < today:
            return True
