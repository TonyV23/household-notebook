from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.decorators import unauthenticated_user


@unauthenticated_user
def login_user(request):
    page_title = 'Se connecter'
    template = 'app/settings/auth/login.html'

    variable = {
        'page_title': page_title
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Identifiant incorrect')

    return render(
        request,
        template_name=template,
        context=variable
    )


def logout_user(request):
    logout(request)

    return redirect('/login')