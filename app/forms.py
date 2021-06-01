"""
=========================================================
* FinCon v.1.0
=========================================================
* Coded by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

=========================================================

"""


from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import ModelForm, TextInput

from app.models import Notes, AdvisorySession


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateNoteForm(ModelForm):
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('notes')) #redirect to url stored in param 'next'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.pop('initial')
        person = initial.pop('person', None)
        if person is not None:
            advisory = initial.pop('advisory_session', None)
            self.fields['advisory_session'].queryset = AdvisorySession.objects.filter(person=person)

    class Meta:
        model = Notes
        fields = ['title', 'text', 'due_date', 'reminder', 'advisory_session', 'person']
        widgets = {
            'due_date': DateInput(),
            'title': TextInput(
                attrs={
                    "autocomplete": "off"
                }
            )
        }


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)