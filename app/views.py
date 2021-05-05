# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django import template
from django.urls import reverse_lazy
from django.views import generic
from django.forms import ModelForm

from .models import AdvisorySession, Notes


class CreateNoteForm(ModelForm):
    def get_success_url(self):
        return self.request.GET.get('a', reverse_lazy('notes')) #redirect to url stored in param 'a'

    class Meta:
        model = Notes
        fields = ['title', 'text', 'advisory_session']


class CreateNoteView(generic.CreateView):
    model = Notes
    template_name = 'create-note.html'
    fields = ['title', 'text', 'due_date', 'reminder', 'advisory_session']

    def get_initial(self):
        initial = super(generic.CreateView, self).get_initial()
        # prefill person and if available advisory session
        initial.update({'person': self.request.user})
        if self.request.GET.get('a')[-2] is not None:
            initial.update({'advisory_session': self.request.GET.get('a')[-2]})
        return initial

    def get_success_url(self):
        return self.request.GET.get('a', reverse_lazy('notes')) #redirect to url stored in param 'a'

    def form_valid(self, form):
        form.instance.person = self.request.user
        # add selected text to notes-textfield if existing
        selected_text = self.request.POST.get('selected-text')
        if selected_text is not None:
            form.instance.text = '<p> Notiz zu Abschnitt: <br> '+ selected_text +\
                                 '</p> <hr style="border-top: 2px solid rgba(0, 0, 0, 0.2);">' + \
                                 form.instance.text
        print('form valid')
        return super(CreateNoteView, self).form_valid(form)


class EditNoteView(generic.UpdateView):
    model = Notes
    template_name = 'edit-note.html'
    fields = ['title', 'advisory_session', 'due_date', 'reminder', 'text']
    success_url = reverse_lazy('notes')


class ViewNoteView(generic.DetailView):
    model = Notes
    template_name = 'view-note.html'
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.filter(pk=self.kwargs.get('pk'))
        return context


class AdvisorySummaryView(generic.DetailView):
    model = AdvisorySession
    template_name = 'advisory-summary.html'
    context_object_name = 'advisory-summary'
    form_class = CreateNoteForm

    def get_context_data(self, **kwargs):
        form = CreateNoteForm(initial={"advisory_session": self.kwargs.get('pk')})
        notesToAdvisory = Notes.objects.filter(advisory_session=self.kwargs.get('pk'))
        advisory = AdvisorySession.objects.filter(pk=self.kwargs.get('pk'))
        context = {'advisory': advisory, 'notes': notesToAdvisory, 'form': form}
        return context


class ProtocolView(generic.DetailView):
    model = AdvisorySession
    template_name = 'protocol.html'
    context_object_name = 'protocol'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advisory'] = AdvisorySession.objects.filter(pk=self.kwargs.get('pk'))
        return context


@login_required(login_url="/login/")
def index(request):
    context = {}
    try:
        userId = request.user
        if userId is None:
            print('user cannot be found', userId)  # ToDo: throw better exception

        advisories = AdvisorySession.objects.filter(person_id=userId).order_by('-date')

        context['segment'] = 'index'
        context['advisories'] = advisories

        return render(request, "index.html", context)

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    #html_template = loader.get_template( 'index.html' )
    #return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

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
