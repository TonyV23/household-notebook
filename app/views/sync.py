from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.models import *

@login_required(login_url ='login')
def synchronization_adresse(request):
    province_id = request.GET.get('id_province')
    commune_id = request.GET.get('id_commune')
    zone_id = request.GET.get('id_zone')

    communes_list = Commune.objects.filter(province_id = province_id)
    zones_list = Zone.objects.filter(commune_id = commune_id)
    quarters_list = Quartier.objects.filter(zone_id = zone_id)

    return render(
        request,
        'app/settings/synch.html',
        {
            'communes_list': communes_list,
            'zones_list': zones_list,
            'quarters_list': quarters_list,
        }
    )
