# -*- encoding: utf-8 -*-
"""
* Coded by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

************************

* This file is an implementation template for consuming REST APIs.
* It consumes the REST API provided by the Heinzelmännli Project.
* As this API hasn't existed yet as this code was written, several assumptions have been made.
* These assumptions and further details are documented in my Master Thesis.

* https://hzmEndpoint.ch is used as a placeholder for the Heinzelmännlis endpoint

"""

import requests
from django.shortcuts import render

# ****************************** GET ********************************


# get the list of all events of a client
def getEvents(request):
    clientId = request.user
    url = 'https://hzmEndpoint.ch/events/'

    # https://hzmplaceholder.ch/events/<clientId>/
    response = requests.get(url+clientId)

    events = response.json()

    # extract the events of the list object called "events" in the JSON file
    events_list = {'events': events['events']}
    return events_list


# get the client profile
def getProfile(request):
    clientId = request.user
    url = 'https://hzmEndpoint.ch/clients/'

    # https://hzmplaceholder.ch/clients/<clientId>/profile
    response = requests.get(url+clientId+'/profile')
    userProfile = response.json()
    return userProfile


# get the investment profile
def getInvestmentProfile(request):
    clientId = request.user
    url = 'https://hzmEndpoint.ch/clients/'

    # https://hzmplaceholder.ch/clients/<clientId>/investmentProfile
    response = requests.get(url+clientId+'/investmentProfile')

    invProfile = response.json()
    return invProfile


# get an event
def getEvent(request, eventId):
    url = 'https://hzmEndpoint.ch/events/'

    # https://hzmplaceholder.ch/events/<eventId>/
    response = requests.get(url+eventId)
    evt = response.json()
    return evt


# get the list of all notes of a client
def getNotes(request):
    clientId = request.user
    url = 'https://hzmEndpoint.ch/notes/'

    # https://hzmplaceholder.ch/notes/<clientId>/
    response = requests.get(url+clientId)

    ns = response.json()

    # extract the notes of the list object called "notes" in the JSON file
    notes_list = {'notes': ns['notes']}
    return notes_list

# get the list of all notes of an event
def getNotesByEvent(request, eventId):
    url = 'https://hzmEndpoint.ch/notes/'

    # https://hzmplaceholder.ch/notes/<eventId>/
    response = requests.get(url+eventId)
    ns = response.json()
    notes_list = {'notes': ns['notes']}
    return notes_list


# get a note
def getNote(request, noteId):
    url = 'https://hzmEndpoint.ch/notes/'

    # https://hzmplaceholder.ch/events/<eventId>/
    response = requests.get(url+noteId)
    nt = response.json()
    return nt


# get the list of all documents of a client
def getDocuments(request):
    clientId = request.user
    url = 'https://hzmEndpoint.ch/documents/'

    # https://hzmplaceholder.ch/documents/<clientId>/
    response = requests.get(url+clientId)

    docs = response.json()
    # extract the documents of the list object called "documents" in the JSON file
    docs_list = {'docs': docs['docs']}
    return docs_list


# get the list of all documents of an event
def getDocumentsByEvent(request, eventId):
    url = 'https://hzmEndpoint.ch/documents/'

    # https://hzmplaceholder.ch/documents/<eventId>/
    response = requests.get(url+eventId)
    docs = response.json()
    docs_list = {'docs': docs['docs']}
    return docs_list


# get a document
def getDocument(request, documentId):
    url = 'https://hzmEndpoint.ch/documents/'

    # https://hzmplaceholder.ch/documents/<documentId>/
    response = requests.get(url+documentId)
    doc = response.json()
    return doc


# ****************************** POST ********************************

def postNote(request, json):
    url = 'https://hzmEndpoint.ch/notes/'

    # json would be filled by form data
    """ 
    json = {'clientId': "123",
            "consultationId": "123-3456-3454-1",
            "title": "Neue Notiz",
            "evtCreated": "2021-01-17 10:00",
            "evtModified": "2021-01-21 10:00",
            "evtDue": "2021-05-17",
            "reminder": True,
            "textHtml": "Dies ist eine neue Notiz" } """

    response = requests.post(url, data=json)

    if response.status_code == 200:
        return print('POST successful, note stored', response.text)
    else:
        return print('something went wrong, check out the response code: %s and text %s'
                     % (response.status_code, response.text))


def postDocument(request, json):
    url = 'https://hzmEndpoint.ch/documents/'

    # json would filled by form data / upload
    """ 
    json = {"clientId": 012342223,
            "consultationId": "123-3456-3454-1",
            "title": "Risikoaufklärung 2.0",
            "evtCreated": "2021-01-17 10:00",
            "format": "pdf",
            "status": "Neu",
            "pdfResource":PDF resource } """

    response = requests.post(url, data=json)

    if response.status_code == 200:
        return print('POST successful, document stored', response.text)
    else:
        return print('something went wrong, check out the response code: %s and text %s'
                     % (response.status_code, response.text))


# ****************************** DELETE ********************************

def deleteNote(request, noteId):
    url = 'https://hzmEndpoint.ch/notes/' + noteId

    # delete should have some tokens to validate permission / security reasons
    # to be included here once known!
    response = requests.delete(url)

    if response.status_code == 200:
        return print('DELETE successful', response.text)
    else:
        return print('something went wrong, check out the response code: %s and text %s'
                     % (response.status_code, response.text))


def deleteDocument(request, documentId):
    url = 'https://hzmEndpoint.ch/documents/' + documentId

    # delete should have some tokens to validate permission / security reasons
    # to be included here once known!
    response = requests.delete(url)

    if response.status_code == 200:
        return print('DELETE successful', response.text)
    else:
        return print('something went wrong, check out the response code: %s and text %s'
                     % (response.status_code, response.text))

