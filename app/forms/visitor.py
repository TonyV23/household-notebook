from django.forms import ModelForm
from django import forms

from app.models import Visitor


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        exclude = ['created_at', 'created_by', 'date_arrive']
        widgets = {
            'date_depart': forms.DateInput(attrs={'type': 'date'}),
        }
