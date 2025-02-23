# File: views.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025
# Description: Views

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.
class ShowAllProfilesView(ListView):
    """Define a view class to show all profiles"""

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView):
    """Define a view class to show a profile page"""

    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'