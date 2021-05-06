# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import AdvisorySession, Notes, BankEmployees, UserProfile

admin.site.register(AdvisorySession)
admin.site.register(Notes)
admin.site.register(BankEmployees)
admin.site.register(UserProfile)

