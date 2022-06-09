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
    telephone = PhoneNumberField(default='')
    email = models.EmailField(max_length=254, default='')
    years_experience = models.PositiveIntegerField(default=1)
    background_details = models.CharField(max_length=250, default='')
    image = CloudinaryField('image', default='')

    def __str__(self):
        """
        Method to display stylist instance by first and last name.
        """
        return str(self.first_name + " " + self.last_name)
