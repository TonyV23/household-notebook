from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.models import Province
from app.forms import ProvinceForm

@login_required(login_url ='login')
def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Liste des provinces'
    template = 'app/settings/province/index.html'
    provinces_list = Province.objects.all()
    context = {
        'page_title': page_title,
        'provinces_list': provinces_list
    }

    return render(
        request,
        template_name=template,
        context=context
    )

@login_required(login_url ='login')
def add_province(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une province'

    if request.method == 'GET':
        form = ProvinceForm()

    template = 'app/settings/province/add.html'
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
def store_province(request):
    if request.method == 'POST':
        form = ProvinceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Province enregistrée !")
        else:
            messages.error(request, form.errors)
        return redirect('/province')

@login_required(login_url ='login')
def edit_province(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la province'
    if request.method == 'GET':
        if id == 0:
            form = ProvinceForm()
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(instance=province)

        template = 'app/settings/province/edit.html'
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
def update_province(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ProvinceForm(request.POST)
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(request.POST, instance=province)
        if form.is_valid():
            form.save()
        messages.success(request, "Province modifiée ")
        return redirect('/province')

@login_required(login_url ='login')
def delete_province(request, id):
    province = Province.objects.get(pk=id)
    province.delete()
    messages.success(request, "Province supprimée")
    return redirect('/province')