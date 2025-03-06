# File: views.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025 modified 3/06/2025
# Description: Views

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, Image, StatusImage, StatusMessage
from .forms import CreateProfileForm, CreateStatusMessageForm, UpdateProfileForm, UpdateStatusMessageForm
from django.urls import reverse

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

class CreateProfileView(CreateView):
    """Define a view class to create a new profile"""

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

class CreateStatusMessageView(CreateView):
    """Define a view class to create a new status message"""

    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_context_data(self):
        """Return the context data for the create status form"""
        context = super().get_context_data()
        pk = self.kwargs['pk']
        context['profile'] = Profile.objects.get(pk=pk)
        return context
    
    def form_valid(self, form):
        """Set the profile for the status message"""
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile

        sm = form.save()
        files = self.request.FILES.getlist('files')

        for file in files:
            image = Image.objects.create(profile=profile, image_file=file, caption="")
            StatusImage.objects.create(image=image, status_message=sm)

        return super().form_valid(form)
    
    def get_success_url(self):
        """Return the URL to redirect to after successful form submission"""
        pk = self.kwargs['pk']
        return reverse('show_profile', kwargs={'pk': pk})

class UpdateProfileView(UpdateView):
    """Define a view class to update a profile"""

    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

class DeleteStatusMessageView(DeleteView):
    """Define a view class to delete a status message"""

    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status_message'

    def get_success_url(self):
        """Return the URL to redirect to after successful form submission"""
        status_message = self.get_object()
        profile_pk = status_message.profile.pk
        return reverse('show_profile', kwargs={'pk': profile_pk})

class UpdateStatusMessageView(UpdateView):
    """Define a view class to update a status message"""

    model = StatusMessage
    form_class = UpdateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'
    context_object_name = 'status_message'

    def get_success_url(self):
        """Return the URL to redirect to after successful form submission"""
        status_message = self.get_object()
        profile_pk = status_message.profile.pk
        return reverse('show_profile', kwargs={'pk': profile_pk})