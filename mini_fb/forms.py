# File: forms.py
# Author: Justin Wang (justin1@bu.edu), 2/27/2025 modified 3/06/2025
# Description: Forms

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    """Form for creating a new profile"""
    first_name = forms.CharField(label='First Name', required=True, max_length=30)
    last_name = forms.CharField(label='Last Name', required=True, max_length=30)
    city = forms.CharField(label='City', required=True, max_length=30)
    email_address = forms.EmailField(label='Email Address', required=True, max_length=254)
    profile_image_url = forms.URLField(label='Profile Image URL', required=True)

    class Meta:
        """Meta class for CreateProfileForm"""
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', 'profile_image_url']
        
        
class CreateStatusMessageForm(forms.ModelForm):
    """Form for creating a new status message"""
    message = forms.CharField(label='Message', required=True)

    class Meta:
        """Meta class for CreateStatusMessageForm"""
        model = StatusMessage
        fields = ['message']

class UpdateProfileForm(forms.ModelForm):
    """Form for updating a profile"""
    city = forms.CharField(label='City', required=True, max_length=30)
    email_address = forms.EmailField(label='Email Address', required=True, max_length=254)
    profile_image_url = forms.URLField(label='Profile Image URL', required=True)

    class Meta:
        """Meta class for UpdateProfileForm"""
        model = Profile
        fields = ['city', 'email_address', 'profile_image_url']

class UpdateStatusMessageForm(forms.ModelForm):
    """Form for updating a status message"""
    message = forms.CharField(label='Message', required=True)

    class Meta:
        """Meta class for UpdateStatusMessageForm"""
        model = StatusMessage
        fields = ['message']