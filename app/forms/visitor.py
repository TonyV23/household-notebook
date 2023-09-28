from django.forms import ModelForm
from django import forms

from app.models import Visitor


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        exclude = ['created_at', 'created_by', 'est_chef_de_menage','date_arrive']
        widgets = {
            'annee_de_naissance': forms.DateInput(attrs={'type': 'date'}),
            'date_depart': forms.DateInput(attrs={'type': 'date'}),
        }
