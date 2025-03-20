# File: urls.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025 modified 3/20/2025
# Description: URL patterns

from django.urls import path
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profile'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile'),
    path('profile/create', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/create_status', CreateStatusMessageView.as_view(), name='create_status'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('status/<int:pk>/delete', DeleteStatusMessageView.as_view(), name='delete_status'),
    path('status/<int:pk>/update', UpdateStatusMessageView.as_view(), name='update_status'),
    path('profile/<int:pk>/add_friend/<int:other_pk>', AddFriendView.as_view(), name='add_friend'),
    path('profile/<int:pk>/friend_suggestions', ShowFriendSuggestionsView.as_view(), name='friend_suggestions'),
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name='news_feed'),
]