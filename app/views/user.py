from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
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
        'page_title' : page_title,
    }

    return render(
        request,
        template_name = template,
        context = variable
    )

def index(request) :
    page_title = 'Types de comptes'
    users = User.objects.all()
    template = 'app/settings/users/index.html'

    variable = {
        'page_title' : page_title,
        'users' : users
    }

    return render(
        request,
        template_name = template,
        context = variable
    )

def add_user(request) :
    page_title = 'Nouveau compte'
    template = 'app/settings/users/add.html'
    form = UserForm()

    variable = {
        'page_title' : page_title,
        'form': form
    }
    
    return render(
        request, 
        template_name = template,
        context = variable
    )

def store_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'students')
            user.groups.add(group)    
            messages.success(request, 'Le compte de '+username+' a été ajouté')
        
        return redirect('/accounts')

def login_user(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Nom d\'utilisateur ou mot de passe incorrect')

    page_title = 'Se connecter'
    template  = 'app/settings/users/login.html'
    
    variable = {
        'page_title' : page_title
    }

    return render(
        request,
        template_name = template,
        context = variable
    )

def edit_user(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier les informations de l\'étudiant'
    if request.method == 'GET':
        if id == 0:
            form = UserEditInfoForm()
        else:
            user = User.objects.get(pk=id)
            form = UserEditInfoForm(instance=user)

        template = "app/settings/users/edit.html"
        context = {
            'page_title' : page_title,
            'form' : form
        }
        return render(
            request,
            template_name = template,
            context= context
        )

def update_user(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = UserEditInfoForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserEditInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        messages.success(request, "Les informations de l'étudiant ont été modifié avec succès !")
        return redirect('/accounts') 

def logout_user(request) :
    logout(request)

    return redirect('/login')

def delete_user(request, id) :
    user = User.objects.get(pk = id)
    user.delete()
    messages.success(request, 'Le compte a été supprimé avec succès')
    return redirect('/accounts')