# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us

* Taken as code base. Extended by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('ckeditor/', include('ckeditor_uploader.urls')), # upload images in rich text field
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             # UI Kits Html files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
