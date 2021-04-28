# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # ToDo: non-static path would be better
    re_path(r'^advisorySession.html$', views.advisorySessions, name='advisorySessions'),
    re_path(r'^advisorySessionDetail.html$', views.advisorySessionDetail, name='advisorySessionDetail'),
    re_path(r'^protocol.html$', views.protocol, name='protocol'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
