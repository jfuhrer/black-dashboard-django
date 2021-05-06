# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class BankEmployees(models.Model):
    #might be needed to connect employees with user in the future
    #person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField('Vorname', max_length=150, blank=True)
    last_name = models.CharField('Nachname', max_length=150, blank=True)
    role = models.CharField('Rolle', max_length=150, blank=True,
                            choices=[('advisor_m', 'Kundenbetreuer'),
                                     ('advisor_f', 'Kundenbetreuerin'),
                                     ('bachoffice', 'Back-Office'),
                                     ('manager', 'Manager')])
    email = models.CharField('E-Mail', max_length=150, blank=True)
    telephone_no = models.CharField('Telefon', max_length=150, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    advisor = models.ForeignKey(BankEmployees, on_delete=models.DO_NOTHING, null=True, blank=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    notes = RichTextUploadingField(blank=True, null=True)
    type = models.CharField('Einstufung', max_length=150, blank=True,
                            choices=[('NW', 'Non Wealthy'),
                                     ('MAI', 'Mass Affluent Individual'),
                                     ('HNWI', 'High Net Worth Individual'),
                                     ('UHNWI', 'Ultra High Net Worth Individual')])


class AdvisorySession(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=150, choices=[('advisory', 'Beratung'),
                                                     ('next-advisory', 'Bevorstehende Beratung'),
                                                     ('event', 'Event')])
    title = models.CharField(max_length=150)
    date = models.DateTimeField('Datum')
    advisor_name = models.CharField(max_length=150, blank=True)
    advisor = models.ForeignKey(BankEmployees, on_delete=models.DO_NOTHING, null=True, blank=True)
    place = models.CharField(max_length=150, blank=True)
    overview = models.TextField(blank=True)
    hot_leads = models.TextField(blank=True)
    agenda = models.TextField(blank=True)
    investment_details = models.TextField(blank=True)
    summary = RichTextUploadingField(blank=True, null=True)
    protocol = RichTextUploadingField(blank=True, null=True)
    created_by = models.CharField(max_length=150) # should be an ID and automatically filled
    modified_by = models.CharField(max_length=150, blank=True) # should be an ID and automatically filled
    evt_created = models.DateTimeField('Erstellt am', auto_now_add=True) # Automatically set the field to now when the object is first created. blank = true, editable = false
    evt_modified = models.DateTimeField('Verändert am', auto_now=True) # Automatically set the field to now every time the object is saved.  blank = true, editable = false

    def __str__(self):
        return self.title


class Notes(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Titel', max_length=150)
    text = RichTextUploadingField(blank=True, null=True)
    due_date = models.DateField('Zu erledigen bis', null=True, blank=True)
    reminder = models.BooleanField(default=False)
    advisory_session = models.ForeignKey(AdvisorySession, on_delete=models.CASCADE, null=True, blank=True,)
    evt_created = models.DateTimeField('Erstellt am', auto_now_add=True)
    evt_modified = models.DateTimeField('Verändert am', auto_now=True)

    def __str__(self):
        return self.title




"""
class Documents(models.Model):
    file = models.FileField() # maybe add upload_to https://www.youtube.com/watch?v=1UYTZiMtxA4
    advisory_session = models.ForeignKey(AdvisorySession, on_delete=models.CASCADE, blank=True)
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=150)
    evt_uploaded = models.DateTimeField('Uploaded on', auto_now_add=True)

"""




