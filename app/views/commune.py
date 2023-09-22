from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from app.models import Province, Commune
from app.forms import CommuneForm


def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Liste des communes'
    template = 'app/settings/commune/index.html'
    communes_list = Commune.objects.all()
    context = {
        'page_title': page_title,
        'communes_list': communes_list
    }

    return render(
        request,
        template_name=template,
        context=context
    )


def add_commune(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une commune'
    template = 'app/settings/commune/add.html'
    provinces_list = Province.objects.all()

    if request.method == 'GET':
        form = CommuneForm()

    context = {
        'page_title': page_title,
        'provinces_list': provinces_list,
        'form': form
    }

    return render(
        request,
        template_name=template,
        context=context
    )


def store_commune(request):
    if request.method == 'POST':
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Commune enregistrée !")
        else:
            messages.error(request, form.errors)
        return redirect('/commune')


def edit_commune(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la commune'
    template = 'app/settings/commune/edit.html'
    if request.method == 'GET':
        if id == 0:
            form = CommuneForm()
        else:
            commune = Commune.objects.get(pk=id)
            form = CommuneForm(instance=commune)
        context = {
            'form': form,
            'page_title': page_title
        }
        return render(
            request,
            template_name=template,
            context=context
        )


def update_commune(request, id):
    if request.method == 'POST':
        if id == 0:
            form = CommuneForm(request.POST)
        else:
            commune = Commune.objects.get(pk=id)
            form = CommuneForm(request.POST, instance=commune)
        if form.is_valid():
            form.save()
        messages.success(request, "Commune modifiée")
        return redirect('/commune')

def delete_commune(request, id) :
    commune = Commune.objects.get(pk = id)
    commune.delete()
    messages.success(request,"Commune supprimée")
    return redirect('/commune')