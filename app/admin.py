from django.contrib import admin

from app.models import *

# Register your models here.
admin.site.register(Commune)
admin.site.register(Household)
admin.site.register(Person)
admin.site.register(Profession)
admin.site.register(Province)
admin.site.register(Quartier)
admin.site.register(Visitor)
admin.site.register(Zone)