from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpRequest

from app.forms import UserForm, UserEditInfoForm


def account_type(request):
    page_title = 'Type de compte'
    template = 'app/settings/account/type.html'

    variable = {
        'page_title': page_title,
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

def index_chef_family(request):
    page_title = 'Comptes des chefs de famille'
    group = Group.objects.get(name="chef_family")
    users = User.objects.filter(groups=group).order_by('username')
    template = 'app/settings/account/index_chef_family.html'

    variable = {
        'page_title': page_title,
        'users': users,
        'group': group
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

def index_chef_quarter(request):
    page_title = 'Comptes des chefs de quartiers'
    group = Group.objects.get(name="chef_quarter")
    users = User.objects.filter(groups=group).order_by('username')
    template = 'app/settings/account/index_chef_quarter.html'

    variable = {
        'page_title': page_title,
        'users': users
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

def add_user_chef_family(request):
    page_title = 'Compte du chef de menage'
    template = 'app/settings/account/add_chef_family.html'
    form = UserForm()

    variable = {
        'page_title': page_title,
        'form': form
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

def add_user_chef_quarter(request):
    page_title = 'Compte du chef de quartier'
    template = 'app/settings/account/add_chef_quarter.html'
    form = UserForm()

    variable = {
        'page_title': page_title,
        'form': form
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

def store_user_chef_family(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='chef_family')
            user.groups.add(group)
            messages.success(request, 'Le compte de '+username+' a été ajouté')

        return redirect('/account/list_chef_family')

def store_user_chef_quarter(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='chef_quarter')
            user.groups.add(group)
            messages.success(request, 'Le compte de '+username+' a été ajouté')

        return redirect('/account/list_chef_family')

def edit_user(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier les données de l\'utilisateur'
    if request.method == 'GET':
        if id == 0:
            form = UserEditInfoForm()
        else:
            user = User.objects.get(pk=id)
            form = UserEditInfoForm(instance=user)

        template = "app/settings/account/edit.html"
        context = {
            'page_title': page_title,
            'form': form
        }
        return render(
            request,
            template_name=template,
            context=context
        )

def update_user(request, id):
    if request.method == 'POST':
        if id == 0:
            form = UserEditInfoForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserEditInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            groups = user.groups.all()
            if groups.filter(name='chef_family').exists():
                return redirect('/account/list_chef_family')
            elif groups.filter(name='chef_quarter').exists():
                return redirect('/account/list_chef_quarter')
        messages.success(request, "Les données ont été modifié !")
        return redirect('/type_account')

def delete_user(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    groups = user.groups.all()
    if groups.filter(name='chef_family').exists():
        return redirect('/account/list_chef_family')
    elif groups.filter(name='chef_quarter').exists():
        return redirect('/account/list_chef_quarter')
    messages.success(request, 'Le compte a été supprimé')
    return redirect('/type_account')

