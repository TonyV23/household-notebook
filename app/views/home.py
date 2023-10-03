from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from app.models import Household, Person, Visitor
@login_required(login_url ='login')
def index (request) :
    page_title = 'Accueil'
    template = 'app/home/index.html'

    total_households = Household.objects.all().count()
    total_member_family = Person.objects.all().count()
    total_visitors = Visitor.objects.all().count()

    total_persons = total_member_family+total_visitors

    context = {
        'page_title' : page_title,
        'template' : template,
        'total_households' : total_households,
        'total_persons' : total_persons,
    }
    
    return render(request, template_name=template, context=context)
