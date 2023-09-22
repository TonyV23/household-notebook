from django.forms import ModelForm

from app.models import Province

class ProvinceForm (ModelForm) :

    class Meta :
        model = Province
        fields = '__all__'