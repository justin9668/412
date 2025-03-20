# File: admin.py
# Author: Justin Wang (justin1@bu.edu), 2/23/2025 modified 3/20/2025
# Description: Admin

from django.contrib import admin

# Register your models here.
from .models import Profile, StatusMessage, Image, StatusImage, Friend
admin.site.register(Profile)
admin.site.register(StatusMessage)
admin.site.register(Image)
admin.site.register(StatusImage)
admin.site.register(Friend)