from django.forms import ModelForm

from app.models import Status

class StatusForm (ModelForm) :

    class Meta :
        model = Status
        fields = '__all__'