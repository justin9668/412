# File: models.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025
# Description: Models

from django.db import models

# Create your models here.
class Profile(models.Model):
    """Model the data attributes of individual Facebook users"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=254)
    profile_image_url = models.URLField()

    def __str__(self):
        """Return a string representation of this model instance"""
        return f'{self.first_name} {self.last_name}'