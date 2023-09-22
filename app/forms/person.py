from django.forms import ModelForm

from app.models import Person

class PersonForm (ModelForm) :

    class Meta :
        model = Person
        fields = '__all__'