# File: views.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025 modified 3/26/2025
# Description: Views

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Profile, Image, StatusImage, StatusMessage
from .forms import CreateProfileForm, CreateStatusMessageForm, UpdateProfileForm, UpdateStatusMessageForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
class ShowAllProfilesView(ListView):
    """Define a view class to show all profiles"""

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

    def get_context_data(self, **kwargs):
        """Add information about which profile belongs to the current user"""
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_user_profile = self.request.user.profile_set.first()
            context['current_user_profile'] = current_user_profile
        return context

class ShowProfilePageView(DetailView):
    """Define a view class to show a profile page"""

    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

class CreateProfileView(CreateView):
    """Define a view class to create a new profile"""

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_context_data(self, **kwargs):
        """Add UserCreationForm to the context"""
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserCreationForm()
        return context

    def form_valid(self, form):
        """Handle both forms and create User and Profile"""
        user_form = UserCreationForm(self.request.POST)
        user = user_form.save()
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

class CreateStatusMessageView(LoginRequiredMixin, CreateView):
    """Define a view class to create a new status message"""

    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_login_url(self):
        """Return the URL required for login"""
        return reverse('login')
    
    def get_context_data(self):
        """Return the context data for the create status form"""
        context = super().get_context_data()
        context['profile'] = self.request.user.profile_set.first()
        return context
    
    def form_valid(self, form):
        """Set the profile for the status message"""
        profile = self.request.user.profile_set.first()
        form.instance.profile = profile

        sm = form.save()
        files = self.request.FILES.getlist('files')

        for file in files:
            image = Image.objects.create(profile=profile, image_file=file, caption="")
            StatusImage.objects.create(image=image, status_message=sm)

        return super().form_valid(form)
    
    def get_success_url(self):
        """Return the URL to redirect to after successful form submission"""
        profile = self.request.user.profile_set.first()
        return reverse('show_profile', kwargs={'pk': profile.pk})

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Define a view class to update a profile"""

    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def get_login_url(self):
        """Return the URL required for login"""
        return reverse('login')

    def get_object(self):
        """Get the profile object for the logged-in user"""
        return self.request.user.profile_set.first()

class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    """Define a view class to delete a status message"""

    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status_message'

    def get_login_url(self):
        """Return the URL required for login"""
        return reverse('login')

    def get_success_url(self):
        """Return the URL to redirect to after successful form submission"""
        status_message = self.get_object()
        profile_pk = status_message.profile.pk
        return reverse('show_profile', kwargs={'pk': profile_pk})

class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
    """Define a view class to update a status message"""

    model = StatusMessage
    form_class = UpdateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'
    context_object_name = 'status_message'

    def get_login_url(self):
        """Return the URL required for login"""
        return reverse('login')

    def get_success_url(self):
        """Return the URL to redirect to after successful form submission"""
        status_message = self.get_object()
        profile_pk = status_message.profile.pk
        return reverse('show_profile', kwargs={'pk': profile_pk})

class AddFriendView(LoginRequiredMixin, View):
    """Define a view class to add a friend to a profile"""

    def get_login_url(self):
        """Return the URL required for login"""
        return reverse('login')

    def dispatch(self, request, other_pk):
        """Add a friend to a profile"""
        profile = request.user.profile_set.first()
        other = Profile.objects.get(pk=other_pk)
        
        profile.add_friend(other)
        return redirect('show_profile', pk=profile.pk)
    
class ShowFriendSuggestionsView(LoginRequiredMixin, DetailView):
    """Define a view class to show friend suggestions"""

    def get_login_url(self):
        """Return the URL required for login"""
        return reverse('login')

    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'
    context_object_name = 'profile'

    def get_object(self):
        """Get the profile object for the logged-in user"""
        return self.request.user.profile_set.first()

class ShowNewsFeedView(LoginRequiredMixin, DetailView):
    """Define a view class to show the news feed"""

    def get_login_url(self):
        """Return the URL required for login"""
        return reverse('login')

    model = Profile
    template_name = 'mini_fb/news_feed.html'
    context_object_name = 'profile'

    def get_object(self):
        """Get the profile object for the logged-in user"""
        return self.request.user.profile_set.first()
    
class UserRegistrationView(CreateView):
    """Define a view class to register a new user"""

    template_name = 'mini_fb/register.html'
    form_class = UserCreationForm
    model = User