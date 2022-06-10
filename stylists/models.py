"""Imports from django and cloudinary."""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField


class Stylist(models.Model):
    """
    Stylist model for stylist database.
    """
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    telephone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    years_experience = models.PositiveIntegerField()
    background_details = models.CharField(max_length=250)
    image = CloudinaryField('image')

    def __str__(self):
        """
        Method to display stylist instance by first name.
        """
        return str(self.first_name)
