from django.forms import ModelForm

from app.models import *

class ZoneForm (ModelForm) :

    class Meta :
        model = Zone
        fields = ['province','commune','zone'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['province'].queryset = Province.objects.none()
        self.fields['commune'].queryset = Commune.objects.none()
        if 'province' in self.data:
                print(self.data)
                try:
                    province_id = int(self.data.get('province'))
                    
                    self.fields['commune'].queryset = Commune.objects.filter(province_id=province_id).order_by('province')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
                self.fields['commune'].queryset = self.instance.province.commune_set.order_by('commune')
                
     