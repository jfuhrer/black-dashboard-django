# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django import template
from django.urls import reverse_lazy
from django.views import generic

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
            Q(summary__icontains=query) |
            Q(title__icontains=query)
        ).distinct()

        for advisory in advisory_results:
            result_title = advisory.title
            result_text = advisory.summary
            result_date = advisory.date
            object_list.append({'type': 'Beratung', 'title': result_title,
                                'date': result_date, 'text':result_text})

        advisory_results = AdvisorySession.objects.filter(protocol__icontains=query).distinct()

        for advisory in advisory_results:
            result_title = advisory.title
            result_text = advisory.protocol
            result_date = advisory.date
            object_list.append({'type': 'Beratung Protokoll', 'title': result_title,
                                'date': result_date, 'text': result_text})

        notes_results = Notes.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)  # case insensitive
        ).distinct()

        for notes in notes_results:
            result_title = notes.title
            result_text = notes.text # ToDo: not only in summary but overall
            result_date = notes.evt_created
            object_list.append({'type': 'Notiz', 'title': result_title,
                                'date': result_date, 'text': result_text})

        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context


class CreateNoteView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    model = Notes
    template_name = 'create-note.html'
    form_class = CreateNoteForm

    def get_initial(self):
        initial = super(generic.CreateView, self).get_initial()
        # prefill person and if available advisory session
        initial.update({'person': self.request.user})
        if self.request.GET.get('next')[-2] is not None:
            initial.update({'advisory_session': self.request.GET.get('next')[-2]})
        return initial

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('notes')) #redirect to url stored in param 'a'

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


class EditNoteView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    model = Notes
    template_name = 'edit-note.html'
    form_class = CreateNoteForm
    success_url = reverse_lazy('notes')


class ViewNoteView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Notes
    template_name = 'view-note.html'
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = UserProfile.objects.get(user=self.request.user)
        advisor = BankEmployees.objects.get(pk=user.advisor_id)
        context['advisor'] = advisor
        context['notes'] = Notes.objects.filter(pk=self.kwargs.get('pk'))
        return context


class AdvisorySummaryView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
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


class AdvisoryChangesView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = AdvisorySession # ToDo maybe own model?
    template_name = 'advisory-changes.html'
    context_object_name = 'advisory-changes'

    def get_context_data(self, **kwargs):
        advisory = AdvisorySession.objects.filter(pk=self.kwargs.get('pk'))
        context = {'advisory': advisory}
        return context


class ProtocolView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
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

        #advisors = BankEmployees.objects.all() # if wanted get advisor name by this model
        advisories = AdvisorySession.objects.filter(person_id=userId).order_by('-date')

        context['segment'] = 'index'
        context['advisories'] = advisories
        #context['advisors'] = advisors

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
        load_template = load_template + '.html'

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
        context = {'notes': notesObjects, 'segment': 'notes'}
        print('notes')
        return render(request, "notes.html", context)

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
