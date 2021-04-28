# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.urls import reverse_lazy
from django.views import generic

from .models import AdvisorySessionSummary, AdvisorySession, Notes


class EditNoteView(generic.UpdateView):
    model = Notes
    template_name = 'edit-note.html'
    fields = ['title', 'body', 'reminder_date', 'advisory_session']
    success_url = reverse_lazy('notes')


class ViewNoteView(generic.DetailView):
    model = Notes
    template_name = 'view-note.html'
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.filter(pk=self.kwargs.get('pk'))
        return context


@login_required(login_url="/login/")
def index(request):
    context = {}
    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)  # ToDo: throw better exception

        advisories = AdvisorySession.objects.filter(person_id=userId).filter(Q(type='advisory') | Q(type='next-advisory')).order_by('-date')

        context = {'advisories': advisories}
        context['segment'] = 'index'

        return render(request, "index.html", context)

    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    #html_template = loader.get_template( 'index.html' )
    #return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def advisorySessions(request):
    context = {}

    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)  # ToDo: throw better exception

        advisories = AdvisorySession.objects.filter(person_id=userId).order_by('-date')
        context = {'advisories': advisories}
        return render(request, "advisorySession.html", context)

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def advisorySessionDetail(request):
    context = {}

    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)  # ToDo: throw better exception

        notes = Notes.objects.filter(advisory_session=1)   # ToDo: wrong, how to get id
        summary = AdvisorySession.objects.filter(id=1) # ToDo: wrong, how to get id
        context = {'summary': summary, 'notes': notes}
        return render(request, "advisorySessionDetail.html", context)

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def protocol(request):
    context = {}

    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)  # ToDo: throw better exception

        summary = AdvisorySession.objects.filter(id=1) # ToDo: wrong, how to get id
        context = {'summary': summary}
        return render(request, "protocol.html", context)

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def notes(request):
    context = {}

    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)  # ToDo: throw better exception

        notesObjects = Notes.objects.filter(person_id=userId) # ToDo: wrong, how to get id
        context = {'notes': notesObjects}
        return render(request, "notes.html", context)

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
