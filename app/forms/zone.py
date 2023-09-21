from django.forms import ModelForm

from app.models import Zone

class ZoneForm (ModelForm) :

    class Meta :
        model = Zone
        fields = '__all__'