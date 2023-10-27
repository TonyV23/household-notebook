from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.models import Household, Province, Commune, Zone, Quartier
from app.forms import HouseholdForm

@login_required(login_url ='login')
def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Liste des menages'
    template = 'app/settings/household/index.html'
    households_list = Household.objects.filter(created_by=request.user)
    context = {
        'page_title': page_title,
        'households_list': households_list,        
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def add_household(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une menage'
    template = 'app/settings/household/add.html'
    provinces_list = Province.objects.all()
    communes_list = Commune.objects.all()
    zones_list = Zone.objects.all()
    quartiers_list = Quartier.objects.all()

    if request.method == 'GET':
        form = HouseholdForm()

    context = {
        'page_title': page_title,
        'provinces_list': provinces_list,
        'communes_list': communes_list,
        'zones_list': zones_list,
        'quartiers_list': quartiers_list,
        'form': form
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def store_household(request):
    if request.method == 'POST':
        form = HouseholdForm(request.POST)
        if form.is_valid():
            household = form.save(commit=False)
            household.created_by = request.user
            household.save()
            messages.success(request, "Menage enregistrée !")
        else:
            messages.error(request, form.errors)
        return redirect('/household')

@login_required(login_url ='login')
def edit_household(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier une menage'
    template = 'app/settings/household/edit.html'
    if request.method == 'GET':
        if id == 0:
            form = HouseholdForm()
        else:
            household = Household.objects.get(pk=id)
            form = HouseholdForm(instance=household)
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
def update_household(request, id):
    if request.method == 'POST':
        if id == 0:
            form = HouseholdForm(request.POST)
        else:
            household = Household.objects.get(pk=id)
            form = HouseholdForm(request.POST, instance=household)
        if form.is_valid():
            form.save()
        messages.success(request, "Manage modifiée")
        return redirect('/household')

@login_required(login_url ='login')
def delete_household(request, id):
    household = Household.objects.get(pk=id)
    household.delete()
    messages.success(request, "Menage supprimée")
    return redirect('/household')

@login_required(login_url='login')
def preview(request) :
    page_title = 'Vu d\'ensemble des ménages'
    template = 'app/settings/household/preview.html'
    households_list = Household.objects.filter(created_by=request.user)

    context = {
        'page_title' :page_title,
        'households_list': households_list
    }

    return render(request, template_name=template, context=context)