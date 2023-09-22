from django.forms import ModelForm

from app.models import Visitor

class VisitorForm (ModelForm) :

    class Meta :
        model = Visitor
        fields = '__all__'