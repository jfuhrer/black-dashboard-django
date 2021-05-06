from django import forms
from django.urls import reverse_lazy
from django.forms import ModelForm

from app.models import Notes


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateNoteForm(ModelForm):
    def get_success_url(self):
        return self.request.GET.get('a', reverse_lazy('notes')) #redirect to url stored in param 'a'

    class Meta:
        model = Notes
        fields = ['title', 'text', 'due_date', 'reminder', 'advisory_session']
        widgets = {
            'due_date': DateInput(),
        }
