from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')

    page_title = 'Se connecter'
    template = 'app/settings/auth/login.html'

    variable = {
        'page_title': page_title
    }

    return render(
        request,
        template_name=template,
        context=variable
    )

def logout_user(request):
    logout(request)

    return redirect('/login')