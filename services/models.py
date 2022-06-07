from django.db import models

# Create your models here.


class Service(models.Model):
    class ServiceType(models.TextChoices):
        CUT = 'CUT', 'Cut'
        COLOUR = 'COLOUR', 'Colour'
        STYLE = 'STYLE', 'Style'
    name = models.CharField(max_length=100, unique=True)
    service_type = models.CharField(
        max_length=10,
        choices=ServiceType.choices,
        default=ServiceType.CUT
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.name)
