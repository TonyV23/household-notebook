from django.shortcuts import render
from django.http import HttpResponse


def index (request) :
    page_title = 'Accueil'
    template = 'app/home/index.html'
    context = {
        'page_title' : page_title,
        'template' : template
    }
    
    return render(request, template_name=template, context=context)
