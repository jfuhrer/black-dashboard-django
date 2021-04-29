# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from app.views import EditNoteView, ViewNoteView, AdvisorySummaryView, ProtocolView, CreateNoteView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    re_path(r'^advisorySession.html$', views.advisorySessions, name='advisorySessions'),
    re_path(r'^notes.html$', views.notes, name='notes'),

    path('protocol/<int:pk>/', ProtocolView.as_view(), name='protocol'),
    path('advisory-summary/<int:pk>/', AdvisorySummaryView.as_view(), name='advisory-summary'),
    path('edit-note/<int:pk>/', EditNoteView.as_view(), name='edit-note'),
    path('view-note/<int:pk>/', ViewNoteView.as_view(), name='view-note'),
    path('create-note/', CreateNoteView.as_view(), name='create-note'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
