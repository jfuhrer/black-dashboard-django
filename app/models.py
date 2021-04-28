# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField

class PersonTest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    body = RichTextField(blank=True, null=True)
    bodyUpload = RichTextUploadingField(blank=True, null=True)


class AdvisorySession(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=150, choices = [('advisory', 'advisory'),('next-advisory', 'next-advisory'), ('event', 'event')])
    title = models.CharField(max_length=150)
    date = models.DateTimeField('Date')
    advisor_name = models.CharField(max_length=150, blank=True)
    place = models.CharField(max_length=150, blank=True)
    overview = models.TextField(blank=True)
    hot_leads = models.TextField(blank=True)
    agenda = models.TextField(blank=True)
    investment_details = models.TextField(blank=True)
    summary = RichTextUploadingField(blank=True, null=True)
    protocol = RichTextUploadingField(blank=True, null=True)
    created_by = models.CharField(max_length=150) # should be an ID and automatically filled
    modified_by = models.CharField(max_length=150, blank=True) # should be an ID and automatically filled
    evt_created = models.DateTimeField('Created on', auto_now_add=True) # Automatically set the field to now when the object is first created. blank = true, editable = false
    evt_modified = models.DateTimeField('Modified on', auto_now=True) # Automatically set the field to now every time the object is saved.  blank = true, editable = false


    def __str__(self):
        return self.title

class AdvisorySessionSummary(models.Model):
    advisory_session = models.ForeignKey(AdvisorySession, on_delete=models.CASCADE)
    type = models.CharField(max_length=20) # type summary or protocol
    summary_text = models.TextField(blank=True)
    protocol_text = models.TextField(blank=True)
    created_by = models.CharField(max_length=150) # should be an ID and automatically filled
    modified_by = models.CharField(max_length=150, blank=True) # should be an ID and automatically filled
    evt_created = models.DateTimeField('Created on', auto_now_add=True) # Automatically set the field to now when the object is first created. blank = true, editable = false
    evt_modified = models.DateTimeField('Modified on', auto_now=True) # Automatically set the field to now every time the object is saved.  blank = true, editable = false

class Notes(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = RichTextUploadingField(blank=True, null=True)
    reminder_date = models.DateTimeField('Date', null=True)
    advisory_session = models.ForeignKey(AdvisorySession, on_delete=models.CASCADE, null=True)
    evt_created = models.DateTimeField('Created on', auto_now_add=True) # Automatically set the field to now when the object is first created. blank = true, editable = false
    evt_modified = models.DateTimeField('Modified on', auto_now=True) # Automatically set the field to now every time the object is saved.  blank = true, editable = false




"""
class Documents(models.Model):
    file = models.FileField() # maybe add upload_to https://www.youtube.com/watch?v=1UYTZiMtxA4
    advisory_session = models.ForeignKey(AdvisorySession, on_delete=models.CASCADE, blank=True)
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=150)
    evt_uploaded = models.DateTimeField('Uploaded on', auto_now_add=True)

"""




