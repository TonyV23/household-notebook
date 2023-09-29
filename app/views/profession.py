from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.models import Profession
from app.forms import ProfessionForm

@login_required(login_url ='login')
def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Liste des professions'
    template = 'app/settings/profession/index.html'
    professions_list = Profession.objects.all()
    context = {
        'page_title': page_title,
        'professions_list': professions_list
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def add_profession(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une profession'

    if request.method == 'GET':
        form = ProfessionForm()

    template = 'app/settings/profession/add.html'
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
def store_profession(request):
    if request.method == 'POST':
        form = ProfessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Profession enregistrée !")
        else:
            messages.error(request, form.errors)
        return redirect('/profession')

@login_required(login_url ='login')
def edit_profession(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la profession'
    if request.method == 'GET':
        if id == 0:
            form = ProfessionForm()
        else:
            profession = Profession.objects.get(pk=id)
            form = ProfessionForm(instance=profession)

        template = 'app/settings/profession/edit.html'
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
def update_profession(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ProfessionForm(request.POST)
        else:
            profession = Profession.objects.get(pk=id)
            form = ProfessionForm(request.POST, instance=profession)
        if form.is_valid():
            form.save()
        messages.success(request, "Profession modifiée ")
        return redirect('/profession')

@login_required(login_url ='login')
def delete_profession(request, id):
    profession = Profession.objects.get(pk=id)
    profession.delete()
    messages.success(request, "Profession supprimée")
    return redirect('/profession')
