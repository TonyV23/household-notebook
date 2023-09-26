from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url ='login')
def index (request) :
    page_title = 'Accueil'
    template = 'app/home/index.html'
    context = {
        'page_title' : page_title,
        'template' : template
    }
    
    return render(request, template_name=template, context=context)
