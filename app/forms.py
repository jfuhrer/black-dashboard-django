"""
=========================================================
* FinCon v.1.0
=========================================================
* Coded by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

=========================================================

"""


from django import forms
from django.urls import reverse_lazy
from django.forms import ModelForm

from app.models import Notes


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateNoteForm(ModelForm):
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('notes')) #redirect to url stored in param 'a'

    class Meta:
        model = Notes
        fields = ['title', 'text', 'due_date', 'reminder', 'advisory_session']
        widgets = {
            'due_date': DateInput(),
        }


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)