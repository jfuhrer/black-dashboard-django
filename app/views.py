# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us

* Taken as code base. Extended by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from django import template
from django.urls import reverse_lazy
from django.views import generic

# needed when data is loaded through REST API
from . import services
from .forms import CreateNoteForm, SearchForm
from .models import AdvisorySession, Notes, BankEmployees, UserProfile


class SearchView(LoginRequiredMixin, generic.FormView):
    login_url = '/login/'
    template_name = 'search.html'
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'search'
        return context


class SearchResultsView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'search-results.html'

    def get_queryset(self):
        object_list = []
        query = self.request.GET.get('q')

        advisory_results = AdvisorySession.objects.filter(
            Q(person=self.request.user) &
            (Q(summary__icontains=query) | Q(title__icontains=query))
        ).distinct()

        for advisory in advisory_results:
            result_title = advisory.title
            result_text = advisory.summary
            result_date = advisory.date
            result_id = advisory.id
            object_list.append({'type': 'Beratung', 'title': result_title,
                                'date': result_date, 'text':result_text, 'id':result_id})

        advisory_results = AdvisorySession.objects.filter(
            Q(person=self.request.user) & Q(protocol__icontains=query)
        ).distinct()

        for advisory in advisory_results:
            result_title = advisory.title
            result_text = advisory.protocol
            result_date = advisory.date
            result_id = advisory.id
            object_list.append({'type': 'Beratung Protokoll', 'title': result_title,
                                'date': result_date, 'text': result_text, 'id':result_id})

        notes_results = Notes.objects.filter(
            Q(person=self.request.user) &
            (Q(title__icontains=query) | Q(text__icontains=query))  # case insensitive
        ).distinct()

        for notes in notes_results:
            result_title = notes.title
            result_text = notes.text
            result_date = notes.evt_created
            result_id = notes.id
            object_list.append({'type': 'Notiz', 'title': result_title,
                                'date': result_date, 'text': result_text, 'id':result_id})

        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    # make semi colon after list element
    text = text.replace('</li>', ";")
    # clean other tags
    clean = re.compile('<.*?>')
    return re.sub(clean, ' ', text)


class CreateNoteView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    model = Notes
    template_name = 'create-note.html'
    form_class = CreateNoteForm

    def get_initial(self):
        initial = super(generic.CreateView, self).get_initial()
        # prefill person and if available advisory session
        initial.update({'person': self.request.user})
        eventId = self.request.GET.get('eventId')
        initial.update({'advisory_session': eventId})
        return initial

    def get_success_url(self):
        # redirect to url stored in param 'next'
        return self.request.GET.get('next', reverse_lazy('notes'))

    def form_valid(self, form):
        form.instance.person = self.request.user
        # add selected text to notes-textfield if existing
        selected_text = self.request.POST.get('selected-text')
        if selected_text is not None:
            selected_text = remove_html_tags(selected_text)
            form.instance.text = '<p> Notiz zu Abschnitt: <br> '+ selected_text +\
                                 '</p>' + \
                                 form.instance.text
        return super(CreateNoteView, self).form_valid(form)


class EditNoteView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    model = Notes
    template_name = 'edit-note.html'
    form_class = CreateNoteForm

    def get_initial(self):
        initial = super(generic.UpdateView, self).get_initial()
        initial.update({'person': self.request.user})
        return initial

    def get_object(self, *args, **kwargs):
        obj = super(EditNoteView, self).get_object(*args, **kwargs)
        if not obj.person == self.request.user:
            raise PermissionDenied("Du bist nicht berechtigt, diese Notiz zu bearbeiten.")
        return obj

    def get_success_url(self):
        # redirect to url stored in param 'next'
        return self.request.GET.get('next', reverse_lazy('notes'))


class ViewNoteView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Notes
    template_name = 'view-note.html'
    context_object_name = 'note'

    def get_object(self, *args, **kwargs):
        obj = super(ViewNoteView, self).get_object(*args, **kwargs)
        if not obj.person == self.request.user:
            raise PermissionDenied("Du bist nicht berechtigt, diese Notiz zu lesen.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            # or via API
            # user = services.getProfile(self.request)
            user = UserProfile.objects.get(user=self.request.user)
            try:
                advisor = BankEmployees.objects.get(pk=user.advisor_id)
                context['advisor'] = advisor

            except BankEmployees.DoesNotExist:
                advisor = None

        except UserProfile.DoesNotExist:
            user = None

        context['segment'] = 'notes'
        context['notes'] = Notes.objects.filter(pk=self.kwargs.get('pk'))
        return context


class AdvisorySummaryView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = AdvisorySession
    template_name = 'advisory-summary.html'
    context_object_name = 'advisory-summary'
    form_class = CreateNoteForm

    def get_object(self, *args, **kwargs):
        obj = super(AdvisorySummaryView, self).get_object(*args, **kwargs)
        if not obj.person == self.request.user:
            raise PermissionDenied("Du bist nicht berechtigt, diese Beratung anzuschauen.")
        return obj

    def get_context_data(self, **kwargs):
        person = self.request.user
        eventId = self.kwargs.get('pk')
        form = CreateNoteForm(initial={"advisory_session": eventId, "person": person})
        notesToAdvisory = Notes.objects.filter(advisory_session=eventId).order_by('-evt_created')
        advisory = AdvisorySession.objects.filter(pk=eventId)

        # or load data via REST API from Heinzelmännli endpoint
        # notesToAdvisory = services.getNotesByEvent(self.request, eventId)
        # advisory = services.getEvent(self.request, eventId)
        context = {'advisory': advisory, 'notes': notesToAdvisory, 'form': form, 'segment':'index'}
        return context


class AdvisoryChangesView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = AdvisorySession
    template_name = 'advisory-changes.html'
    context_object_name = 'advisory-changes'

    def get_context_data(self, **kwargs):
        advisory = AdvisorySession.objects.filter(pk=self.kwargs.get('pk'))
        # or via API
        # advisory = services.getEvent(self.request, self.kwargs.get('pk'))
        context = {'advisory': advisory, 'segment': 'index'}
        return context


class SingleProtocolView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = AdvisorySession
    template_name = 'protocol.html'
    context_object_name = 'protocol'
    form_class = CreateNoteForm

    def get_object(self, *args, **kwargs):
        obj = super(SingleProtocolView, self).get_object(*args, **kwargs)
        if not obj.person == self.request.user:
            raise PermissionDenied("Du bist nicht berechtigt, dieses Protokoll zu lesen.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CreateNoteForm(initial={"advisory_session": self.kwargs.get('pk'), "person": self.request.user})
        context['advisory'] = AdvisorySession.objects.filter(pk=self.kwargs.get('pk'))
        # or via API
        # context['advisory'] = services.getEvent(self.request, self.kwargs.get('pk'))
        context['form'] = form
        context['segment'] = 'protocols'
        return context


class SingleProtocolV2View(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = AdvisorySession
    template_name = 'protocol-v2.html'
    context_object_name = 'protocol-v2'
    form_class = CreateNoteForm

    # no permission needed because demonstration view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CreateNoteForm(initial={"advisory_session": self.kwargs.get('pk'), "person": self.request.user})
        context['advisory'] = AdvisorySession.objects.filter(pk=self.kwargs.get('pk'))
        # or via API
        # context['advisory'] = services.getEvent(self.request, self.kwargs.get('pk'))
        context['form'] = form
        context['segment'] = 'protocols'
        return context


@login_required(login_url="/login/")
def index(request):
    context = {}
    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)
            raise Http404

        try:
            # or via API
            # user = services.getProfile(self.request)
            user = UserProfile.objects.get(user=request.user)
            try:
                advisor = BankEmployees.objects.get(pk=user.advisor_id)
                context['advisor'] = advisor

            except BankEmployees.DoesNotExist:
                advisor = None

        except UserProfile.DoesNotExist:
            user = None

        advisories = AdvisorySession.objects.filter(person_id=userId).order_by('-date')

        # or via API
        # advisories = services.getEvents(self.request)
        # context['advisors'] = advisors

        context['segment'] = 'index'
        context['advisories'] = advisories

        return render(request, "index.html", context)

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('404.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html. --> for investor profile, user profile, login, register
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template
        load_template = load_template

        html_template = loader.get_template(load_template+'.html')
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def notes(request):
    context = {}

    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)
            raise Http404

        notesObjects = Notes.objects.filter(person_id=userId).order_by('-evt_created')
        # or via API
        # notesObjects = services.getNotes(self.request)

        context = {'notes': notesObjects, 'segment': 'notes'}
        return render(request, "notes.html", context)

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def protocols(request):
    context = {}

    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)
            raise Http404

        advisories = AdvisorySession.objects.filter(person=userId, type='advisory').order_by('-date')
        # or via API
        # advisories = services.getEvents(self.request)

        context = {'advisories': advisories, 'segment': 'protocols'}
        return render(request, "protocols.html", context)

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('500.html')
        return HttpResponse(html_template.render(context, request))

