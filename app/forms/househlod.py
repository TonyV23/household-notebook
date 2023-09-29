from django.forms import ModelForm

from app.models import Household

class HouseholdForm (ModelForm) :

    class Meta :
        model = Household
        exclude = ['created_at', 'created_by']