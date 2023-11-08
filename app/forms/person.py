from django.forms import ModelForm
from django import forms


from app.models import Person
class PersonForm (ModelForm):
     class Meta:
        model = Person
        exclude = ['created_at', 'created_by']
        widgets = {
            "annee_de_naissance": forms.TextInput(attrs={'type': 'date'}),
            "date_depart": forms.TextInput(attrs={'type': 'date'})
        }
