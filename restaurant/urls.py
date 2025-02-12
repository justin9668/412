# File: urls.py
# Author: Justin Wang (justin1@bu.edu), 2/11/2025
# Description: URL patterns

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'', views.main, name='main'),
    path(r'main/', views.main, name='main'),
    path(r'order/', views.order, name='order'),
    path(r'confirmation/', views.confirmation, name='confirmation'),
    path(r'submit_order', views.submit_order, name='submit_order'),
]