# File: models.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025 modified 3/26/2025
# Description: Models

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """Model the data attributes of individual Facebook users"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=254)
    profile_image_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
    
    def get_friends(self):
        """Return a list of friend's profiles"""
        friend_objects = Friend.objects.filter(profile1=self) | Friend.objects.filter(profile2=self)
        
        friend_profiles = []
        
        # For each Friend object, add other profile to list
        for friend in friend_objects:
            if friend.profile1 == self:
                friend_profiles.append(friend.profile2)
            else:
                friend_profiles.append(friend.profile1)
                
        return friend_profiles
    
    def add_friend(self, other):
        """Add a friend to this profile"""
        # Check if other is self
        if other == self:
            return

        # Check if friendship already exists
        if Friend.objects.filter(profile1=self, profile2=other).exists():
            return
        
        Friend.objects.create(profile1=self, profile2=other)
    
    def get_friend_suggestions(self):
        """Return a list of friend suggestions for this profile"""
        all_profiles = Profile.objects.exclude(pk=self.pk) 
        current_friends = self.get_friends()
        # Exclude current friends from suggestions
        suggestions = all_profiles.exclude(pk__in=[friend.pk for friend in current_friends])
        
        return suggestions
    
    def get_news_feed(self):
        """Return a list of status messages from self and friends"""
        friends = self.get_friends()
        news_feed = StatusMessage.objects.filter(profile__in=[self] + friends).order_by('-timestamp')
        return news_feed

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

class Friend(models.Model):
    """Model the data attributes of individual friendships"""
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile1')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile2')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of this model instance"""
        return f'{self.profile1.first_name} {self.profile1.last_name} & {self.profile2.first_name} {self.profile2.last_name}'