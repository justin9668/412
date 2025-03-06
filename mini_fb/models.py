# File: models.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025 modified 3/06/2025
# Description: Models

from django.db import models
from django.urls import reverse

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
    
    def get_status_messages(self):
        """Return all status messages associated with this profile"""
        status_messages = StatusMessage.objects.filter(profile=self).order_by('-timestamp')
        return status_messages
    
    def get_absolute_url(self):
        """Return the URL to access a particular instance of this model"""
        return reverse('show_profile', kwargs={'pk':self.pk})
    
class StatusMessage(models.Model):
    """Model the data attributes of individual status messages"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=False)

    def __str__(self):
        """Return a string representation of this model instance"""
        return f'{self.profile.first_name} {self.profile.last_name} at {self.timestamp}'
    
    def get_images(self):
        """Return all images associated with this status message"""
        images = Image.objects.filter(statusimage__status_message=self)
        return images
    
class Image(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image_file = models.ImageField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(blank=True)

class StatusImage(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    status_message = models.ForeignKey(StatusMessage, on_delete=models.CASCADE)