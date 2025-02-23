# File: urls.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025
# Description: URL patterns

from django.urls import path
from django.conf import settings
from . import views
from .views import ShowAllProfilesView, ShowProfilePageView

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profile'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile'),
]