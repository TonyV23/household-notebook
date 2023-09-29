from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.models import Visitor, Province, Commune, Zone, Profession, Quartier
from app.forms import VisitorForm

@login_required(login_url ='login')
def index(request):
    page_title = 'Les visiteurs'
    template = 'app/settings/person/visitor/index.html'
    visitors_list = Visitor.objects.all()

    variable = {
        'page_title': page_title,
        'visitors_list': visitors_list,
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

@login_required(login_url ='login')
def add_visitor(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Nouveau visiteur'
    template = 'app/settings/person/visitor/add.html'
    provinces_list = Province.objects.all()
    communes_list = Commune.objects.all()
    zones_list = Zone.objects.all()
    quartiers_list = Quartier.objects.all()
    profession_list = Profession.objects.all()

    if request.method == 'GET':
        form = VisitorForm()

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
def store_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            # instance = form.save(commit=False)
            # instance.save(request=request)
            messages.success(request, "Données du visiteur enregistrée !")
        else:
            messages.error(request, form.errors)
        return redirect('/visitors')


@login_required(login_url ='login')
def edit_visitor(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier les données d\'un visiteur'
    template = 'app/settings/person/visitor/edit.html'
    if request.method == 'GET':
        if id == 0:
            form = VisitorForm()
        else:
            visitor = Visitor.objects.get(pk=id)
            form = VisitorForm(instance=visitor)
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
def update_visitor(request, id):
    if request.method == 'POST':
        if id == 0:
            form = VisitorForm(request.POST)
        else:
            visitor = Visitor.objects.get(pk=id)
            form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
        messages.success(request, "Données du visiteur modifiées")
        return redirect('/visitors')

@login_required(login_url ='login')
def delete_visitor(request, id):
    visitor = Visitor.objects.get(pk=id)
    visitor.delete()
    messages.success(request, "Données du visiteur supprimée")
    return redirect('/visitors')

