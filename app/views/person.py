from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.models import Person, Household, Province, Commune, Zone, Profession, Quartier
from app.forms import PersonForm

@login_required(login_url ='login')
def index(request):
    page_title = 'Membres de famille'
    template = 'app/settings/person/family/index.html'
    persons_list = Person.objects.filter(created_by=request.user)

    variable = {
        'page_title': page_title,
        'persons_list': persons_list,
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

@login_required(login_url ='login')
def person_type(request):
    page_title = 'Membre Famille / Visiteur'
    template = 'app/settings/person/type.html'

    variable = {
        'page_title': page_title,
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

@login_required(login_url ='login')
def add_family_member(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Nouveau membre de la famille'
    template = 'app/settings/person/family/add.html'
    provinces_list = Province.objects.all()
    communes_list = Commune.objects.all()
    zones_list = Zone.objects.all()
    quartiers_list = Quartier.objects.all()
    profession_list = Profession.objects.all()

    if request.method == 'GET':
        form = PersonForm()

    context = {
        'page_title': page_title,
        'provinces_list': provinces_list,
        'communes_list': communes_list,
        'zones_list': zones_list,
        'quartiers_list': quartiers_list,
        'profession_list': profession_list,
        'form': form
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def store_family_member(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.created_by = request.user  
            person.save()
            messages.success(request, "Données du membre enregistrées !")
        else:
            messages.error(request, form.errors)
        return redirect('/family_members')

@login_required(login_url ='login')
def edit_family_member(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier les données d\'un membre de la famille'
    template = 'app/settings/person/family/edit.html'
    if request.method == 'GET':
        if id == 0:
            form = PersonForm()
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(instance=person)
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
def update_family_member(request, id):
    if request.method == 'POST':
        if id == 0:
            form = PersonForm(request.POST)
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        messages.success(request, "Données du membre modifiées")
        return redirect('/family_members')

@login_required(login_url ='login')
def delete_family_member(request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    messages.success(request, "Données du membre supprimée")
    return redirect('/family_members')
