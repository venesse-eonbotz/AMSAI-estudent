# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from settings.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('amsai/prereg_settings/', preregSettings),
    path('amsai/prereg_settings/<int:nid>/delete/', preregSettingsDelete),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)