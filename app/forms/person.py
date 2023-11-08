from django.forms import ModelForm
from django.forms import DateInput

from app.models import Person
class PersonForm (ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.initial['annee_de_naissance'] = self.instance.annee_de_naissance
            self.initial['date_depart'] = self.instance.date_depart

    class Meta:
        model = Person
        exclude = ['created_at', 'created_by']
        widgets = {
            'annee_de_naissance': DateInput(attrs={'type': 'date'}),
            'date_depart': DateInput(attrs={'type': 'date'}),
        }
