from django.forms import ModelForm

from app.models import Quartier

class QuartierForm (ModelForm) :

    class Meta :
        model = Quartier
        fields = '__all__'