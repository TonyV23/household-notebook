from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.models import Status
from app.forms import StatusForm

@login_required(login_url ='login')
def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Liste des statut'
    template = 'app/settings/status/index.html'
    status_list = Status.objects.all()
    context = {
        'page_title': page_title,
        'status_list': status_list
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def add_status(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un statut'

    if request.method == 'GET':
        form = StatusForm()

    template = 'app/settings/status/add.html'
    context = {
        'page_title': page_title,
        'form': form
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def store_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Statut enregistré !")
        else:
            messages.error(request, form.errors)
        return redirect('/status')

@login_required(login_url ='login')
def edit_status(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le Statut'
    if request.method == 'GET':
        if id == 0:
            form = StatusForm()
        else:
            status = Status.objects.get(pk=id)
            form = StatusForm(instance=status)

        template = 'app/settings/status/edit.html'
        context = {
            'page_title': page_title,
            'form': form
        }

        return render(
            request,
            template_name=template,
            context=context
        )

@login_required(login_url ='login')
def update_status(request, id):
    if request.method == 'POST':
        if id == 0:
            form = StatusForm(request.POST)
        else:
            status = Status.objects.get(pk=id)
            form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
        messages.success(request, "Statut modifié ")
        return redirect('/status')

@login_required(login_url ='login')
def delete_status(request, id):
    status = Status.objects.get(pk=id)
    status.delete()
    messages.success(request, "Statut supprimée")
    return redirect('/status')
