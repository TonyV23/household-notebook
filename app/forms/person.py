from django.forms import ModelForm
from django.forms import DateInput

from app.models import Person


class PersonForm (ModelForm):

    class Meta:
        model = Person
        exclude = ['created_at', 'created_by']
        widgets = {
            'annee_de_naissance': DateInput(attrs={'type': 'date'}),
            'date_depart': DateInput(attrs={'type': 'date'}),
        }
