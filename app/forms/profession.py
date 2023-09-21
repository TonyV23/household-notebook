from django.forms import ModelForm

from app.models import Profession

class ProfessionForm (ModelForm) :

    class Meta :
        model = Profession
        fields = '__all__'