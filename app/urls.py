# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us

* Taken as code base. Extended by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

"""

from django.urls import path, re_path
from app import views
from app.views import EditNoteView, ViewNoteView, AdvisorySummaryView, SingleProtocolView, CreateNoteView, \
    SearchResultsView, \
    SearchView, AdvisoryChangesView, SingleProtocolV2View

urlpatterns = [
    # The home page
    path('', views.index, name='home'),

    re_path(r'^notes$', views.notes, name='notes'),
    re_path(r'^protocols', views.protocols, name='protocols'),

    path('protocol-v2/<int:pk>/', SingleProtocolV2View.as_view(), name='protocol-v2'),
    path('protocol/<int:pk>/', SingleProtocolView.as_view(), name='protocol'),
    path('advisory-summary/<int:pk>/', AdvisorySummaryView.as_view(), name='advisory-summary'),
    path('advisory-changes/<int:pk>/', AdvisoryChangesView.as_view(), name='advisory-changes'),
    path('edit-note/<int:pk>/', EditNoteView.as_view(), name='edit-note'),
    path('view-note/<int:pk>/', ViewNoteView.as_view(), name='view-note'),
    path('create-note/', CreateNoteView.as_view(), name='create-note'),
    path('search-results/', SearchResultsView.as_view(), name='search-results'),
    path('search/', SearchView.as_view(), name='search'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
