"""Imports from django."""
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Service(models.Model):
    """
    Service model for services database.
    """

    class ServiceType(models.TextChoices):
        """
        Service type field options
        """

        CUT = 'CUT', 'Cut'
        COLOUR = 'COLOUR', 'Colour'
        STYLE = 'STYLE', 'Style'

    name = models.CharField(max_length=100, unique=True)
    service_type = models.CharField(
        max_length=10,
        choices=ServiceType.choices,
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('25.00')),
                    MaxValueValidator(Decimal('300.00'))]
        )

    def __str__(self):
        """
        Method to display service instance by its name.
        """
        return str(self.name)
