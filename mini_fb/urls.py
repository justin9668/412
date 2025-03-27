# File: urls.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025 modified 3/26/2025
# Description: URL patterns

from django.urls import path
from django.conf import settings
from . import views
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profile'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile'),
    path('profile/create', CreateProfileView.as_view(), name='create_profile'),
    path('status/create_status', CreateStatusMessageView.as_view(), name='create_status'),
    path('profile/update', UpdateProfileView.as_view(), name='update_profile'),
    path('status/<int:pk>/delete', DeleteStatusMessageView.as_view(), name='delete_status'),
    path('status/<int:pk>/update', UpdateStatusMessageView.as_view(), name='update_status'),
    path('profile/add_friend/<int:other_pk>', AddFriendView.as_view(), name='add_friend'),
    path('profile/friend_suggestions', ShowFriendSuggestionsView.as_view(), name='friend_suggestions'),
    path('profile/news_feed', ShowNewsFeedView.as_view(), name='news_feed'),
    path('login', auth_views.LoginView.as_view(template_name='mini_fb/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='mini_fb/logged_out.html'), name='logout'),
]