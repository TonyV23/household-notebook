from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.models import Province, Commune, Zone, Quartier
from app.forms import QuartierForm

@login_required(login_url ='login')
def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Liste des quartiers'
    template = 'app/settings/quartier/index.html'
    quartiers_list = Quartier.objects.all()
    context = {
        'page_title': page_title,
        'quartiers_list': quartiers_list
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def add_quartier(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un quartier'
    template = 'app/settings/quartier/add.html'
    
    provinces_list = Province.objects.all()
    communes_list = Commune.objects.all()
    zones_list = Zone.objects.all()

    if request.method == 'GET':
        form = QuartierForm()

    context = {
        'page_title': page_title,
        'provinces_list': provinces_list,
        'communes_list': communes_list,
        'zones_list': zones_list,
        'form': form
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def store_quartier(request):
    if request.method == 'POST':
        form = QuartierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Quartier enregistré !")
        else:
            messages.error(request, form.errors)
        return redirect('/quartier')

@login_required(login_url ='login')
def edit_quartier(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le quartier'
    template = 'app/settings/quartier/edit.html'
    if request.method == 'GET':
        if id == 0:
            form = QuartierForm()
        else:
            quartier = Quartier.objects.get(pk=id)
            form = QuartierForm(instance=quartier)
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
def update_quartier(request, id):
    if request.method == 'POST':
        if id == 0:
            form = QuartierForm(request.POST)
        else:
            quartier = Quartier.objects.get(pk=id)
            form = QuartierForm(request.POST, instance=quartier)
        if form.is_valid():
            form.save()
        messages.success(request, "Quartier modifié")
        return redirect('/quartier')

@login_required(login_url ='login')
def delete_quartier(request, id):
    quartier = Quartier.objects.get(pk=id)
    quartier.delete()
    messages.success(request, "Quartier supprimé")
    return redirect('/quartier')
