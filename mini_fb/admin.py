# File: admin.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025
# Description: Admin

from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)