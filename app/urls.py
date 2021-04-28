# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from app.views import EditNoteView, ViewNoteView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # ToDo: non-static path would be better
    re_path(r'^advisorySession.html$', views.advisorySessions, name='advisorySessions'),
    re_path(r'^advisorySessionDetail.html$', views.advisorySessionDetail, name='advisorySessionDetail'),
    re_path(r'^protocol.html$', views.protocol, name='protocol'),
    re_path(r'^notes.html$', views.notes, name='notes'),

    path('edit-note/<int:pk>/', EditNoteView.as_view(), name='edit-note'),
    path('view-note/<int:pk>/', ViewNoteView.as_view(), name='view-note'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
