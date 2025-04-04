# File: urls.py
# Author: Justin Wang (justin1@bu.edu), 4/3/2025
# Description: URL patterns

from django.urls import path
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    path(r'', VotersListView.as_view(), name='voters'),
    path('voter/<int:pk>/', VoterDetailView.as_view(), name='voter'),
    path('graphs/', GraphsView.as_view(), name='graphs'),
]