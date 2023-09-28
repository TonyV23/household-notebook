from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from app.models import Household
@login_required(login_url ='login')
def index (request) :
    page_title = 'Accueil'
    template = 'app/home/index.html'

    total_households = Household.objects.all().count()


    context = {
        'page_title' : page_title,
        'template' : template,
        'total_households' : total_households,
    }
    
    return render(request, template_name=template, context=context)
