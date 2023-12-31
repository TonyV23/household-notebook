from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest,JsonResponse
import json
from django.contrib.auth.decorators import login_required

from app.models import Province, Commune, Zone
from app.forms import ZoneForm

@login_required(login_url ='login')
def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Liste des zones'
    template = 'app/settings/zone/index.html'
    zones_list = Zone.objects.all()
    context = {
        'page_title': page_title,
        'zones_list': zones_list
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def add_zone(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une zone'
    template = 'app/settings/zone/add.html'
    provinces_list = Province.objects.all()
    communes_list = Commune.objects.all()

    if request.method == 'GET':
        form = ZoneForm()

    context = {
        'page_title': page_title,
        'provinces_list': provinces_list,
        'communes_list': communes_list,
        'form': form
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def store_zone(request):
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, "Zone enregistrée !")
        else:
            messages.error(request, form.errors)
        return redirect('/zone')

@login_required(login_url ='login')
def edit_zone(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la zone'
    template = 'app/settings/zone/edit.html'
    if request.method == 'GET':
        if id == 0:
            form = ZoneForm()
        else:
            zone = Zone.objects.get(pk=id)
            form = ZoneForm(instance=zone)
        context = {
            'form': form,
            'page_title': page_title
        }
        return render(
            request,
            template_name=template,
            context=context
        )

@login_required(login_url ='login')
def update_zone(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ZoneForm(request.POST)
        else:
            zone = Zone.objects.get(pk=id)
            form = ZoneForm(request.POST, instance=zone)
        if form.is_valid():
            form.save()
        messages.success(request, "Zone modifiée")
        return redirect('/zone')

@login_required(login_url ='login')
def delete_zone(request, id):
    zone = Zone.objects.get(pk=id)
    zone.delete()
    messages.success(request, "Zone supprimée")
    return redirect('/zone')

# def getProvince(request):
#     data = json.loads(request.body)
#     country_id=data['id']
#     provinces = Province.objects.filter(pays__id=country_id)
#     # print(provinces)
#     return JsonResponse(list(provinces.values("id", "designation")), safe=False)
#     # print(country_id)
#     # return JsonResponse("it is working",safe=False)
def getCommune(request):
    data = json.loads(request.body)
    province_id=data['id']
    communes = Commune.objects.filter(province__id=province_id)
    # print(communes)
    return JsonResponse(list(communes.values("id", "commune")), safe=False)
    # print(country_id)
    # return JsonResponse("it is working",safe=False)
def getZone(request):
    data = json.loads(request.body)
    commune_id=data['id']
    zones = Zone.objects.filter(commune__id=commune_id)
    # print(zones)
    return JsonResponse(list(zones.values("id", "zone")), safe=False)

def getQuarter(request):
    data = json.loads(request.body)
    zone_id=data['id']
    quartiers = Quartier.objects.filter(zones__id=zone_id)
    # print(quartiers)
    return JsonResponse(list(quartiers.values("id", "quartier")), safe=False)