from django.forms import ModelForm

from app.models import *

class QuartierForm (ModelForm) :

    class Meta :
        model = Quartier
        fields = ['province','commune','zone','quartier']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['province'].queryset = Province.objects.none()
        self.fields['commune'].queryset = Commune.objects.none()
        # self.fields['zone'].queryset = Zone.objects.none()
        

        if 'province' in self.data:
                try:
                    province_id = int(self.data.get('province'))
                    
                    self.fields['commune'].queryset = Commune.objects.filter(province_id=province_id).order_by('province')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
                self.fields['commune'].queryset = self.instance.province.commune_set.order_by('commune')
        if 'commune' in self.data:
            try:
                commune_id = int(self.data.get('commune'))
                print(commune_id,'dddd')
                self.fields['zone'].queryset = Zone.objects.filter(commune_id=commune_id).order_by('zone')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            # self.fields['zone'].queryset = self.instance.commune.zone_set.order_by('zone')
            pass

            # if 'zone' in self.data:
            #     try:
            #         zones_id = int(self.data.get('zone'))
                    
            #         self.fields['quartiers'].queryset = Quartier.objects.filter(zones_id=zones_id).order_by('designation')
            #     except (ValueError, TypeError):
            #         pass  # invalid input from the client; ignore and fallback to empty City queryset
            # elif self.instance.pk:
            #     # self.fields['quartiers'].queryset = self.instance.quartiers.city_set.order_by('designation')
            #     pass