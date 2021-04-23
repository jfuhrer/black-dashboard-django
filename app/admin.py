# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import PersonTest, AdvisorySession, AdvisorySessionSummary

admin.site.register(PersonTest)
admin.site.register(AdvisorySession)
admin.site.register(AdvisorySessionSummary)

