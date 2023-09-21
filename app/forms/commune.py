from django.forms import ModelForm

from app.models import Commune

class CommuneForm (ModelForm) :

    class Meta :
        model = Commune
        fields = '__all__'