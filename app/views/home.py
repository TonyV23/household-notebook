from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from app.models import Household, Person, Visitor, Quartier, Profession


@login_required(login_url='login')
def index(request):
    page_title = 'Accueil'
    template = 'app/home/index.html'

    total_households = Household.objects.all().count()
    total_persons = Person.objects.all().count()

    masculine_gender_occurence = getMasculineOccurrence()
    feminine_gender_occurence = getFeminineOccurence()
    quarters_occurence = getQuarterOccurence()
    profession_occurence = getProfessionOccurence()
    
    person_registered_per_day = getPersonRegisteredPerDay()

    context = {
        'page_title': page_title,
        'template': template,
        'total_households': total_households,
        'total_persons': total_persons,
        'masculine_gender_occurence': masculine_gender_occurence,
        'feminine_gender_occurence': feminine_gender_occurence,
        'quarters_occurence': quarters_occurence,
        'profession_occurence': profession_occurence,
        'person_registered_per_day': person_registered_per_day,
    }

    return render(request, template_name=template, context=context)

def getFeminineOccurence() :
    feminine_gender_occurence = Person.objects.values('genre').filter(genre ='Female').annotate(feminine_gender = Count('genre'))
    feminine_gender_occurence_list = []
    for i in range(0,len(feminine_gender_occurence)) :
        feminine_gender_occurence_list.append(list(feminine_gender_occurence[i].values())[1])
    
    return feminine_gender_occurence_list

def getMasculineOccurrence():
    masculine_gender_occurence = Person.objects.values('genre').filter(genre ='Male').annotate(masculine_gender = Count('genre'))
    masculine_gender_occurence_list = []
    for i in range(0,len(masculine_gender_occurence)) :
        masculine_gender_occurence_list.append(list(masculine_gender_occurence[i].values())[1])
    
    return masculine_gender_occurence_list

def getQuarterOccurence() :
    get_all_quarters_id = Quartier.objects.values('id')
    get_all_quarters_id_list = []

    for i in range(0, len(get_all_quarters_id)) :
        get_all_quarters_id_list.append(list(get_all_quarters_id[i].values())[0]) 

    quarter_person_dict = {}

    for k in get_all_quarters_id_list :
        get_all_quarters_names = Quartier.objects.filter(pk = k).values('quartier')
        get_all_quarters_name = ""
        
        for i in range(0, len(get_all_quarters_names)) :
            get_all_quarters_name = list(get_all_quarters_names[i].values())[0]
            occurence_quarters = 0
            occurence_quarters = Person.objects.filter(quartier_de_residence_id = k).count()

            quarter_person_dict [get_all_quarters_name] = occurence_quarters

    return quarter_person_dict

def getProfessionOccurence():
    get_all_profession_ids =  Profession.objects.values('id')
    get_all_profession_ids_list = []
    
    for i in range(0, len(get_all_profession_ids)) :
        get_all_profession_ids_list.append(list(get_all_profession_ids[i].values())[0])

    profession_dict = {}

    for k in get_all_profession_ids_list :
        get_all_profession_names = Profession.objects.filter(pk = k).values('profession')
        get_all_profession_name = ""

        for i in range (0, len(get_all_profession_names)) :
            get_all_profession_name = list(get_all_profession_names[i].values())[0]
            occurence_level_studies = 0
            occurence_level_studies = Person.objects.filter(profession_id = k).count()

            profession_dict[get_all_profession_name] = occurence_level_studies

    return profession_dict

def getPersonRegisteredPerDay() :
    person_registered_per_day = Person.objects.extra(select={'day': 'date( created_at )'}).values('day').annotate(available=Count('created_at'))
    
    return person_registered_per_day
