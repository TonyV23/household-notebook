from django.urls import path

from app.views import home, province, commune, zone, quartier, profession

urlpatterns = [
    path('', home.index, name ='dashboard'),

    path('profession', profession.index, name ='view_profession'),
    path('profession/add', profession.add_profession, name ='add_profession'),
    path('profession/store', profession.store_profession, name ='store_profession'),
    path('profession/edit/<int:id>', profession.edit_profession, name ='edit_profession'),
    path('profession/update/<int:id>', profession.update_profession, name ='update_profession'),
    path('profession/delete/<int:id>', profession.delete_profession, name ='delete_profession'),

    path('province', province.index, name ='view_province'),
    path('province/add', province.add_province, name ='add_province'),
    path('province/store', province.store_province, name ='store_province'),
    path('province/edit/<int:id>', province.edit_province, name ='edit_province'),
    path('province/update/<int:id>', province.update_province, name ='update_province'),
    path('province/delete/<int:id>', province.delete_province, name ='delete_province'),

    path('commune', commune.index, name ='view_commune'),
    path('commune/add', commune.add_commune, name ='add_commune'),
    path('commune/store', commune.store_commune, name ='store_commune'),
    path('commune/edit/<int:id>', commune.edit_commune, name ='edit_commune'),
    path('commune/update/<int:id>', commune.update_commune, name ='update_commune'),
    path('commune/delete/<int:id>', commune.delete_commune, name ='delete_commune'),

    path('zone', zone.index, name ='view_zone'),
    path('zone/add', zone.add_zone, name ='add_zone'),
    path('zone/store', zone.store_zone, name ='store_zone'),
    path('zone/edit/<int:id>', zone.edit_zone, name ='edit_zone'),
    path('zone/update/<int:id>', zone.update_zone, name ='update_zone'),
    path('zone/delete/<int:id>', zone.delete_zone, name ='delete_zone'),

    path('quartier', quartier.index, name ='view_quartier'),
    path('quartier/add', quartier.add_quartier, name ='add_quartier'),
    path('quartier/store', quartier.store_quartier, name ='store_quartier'),
    path('quartier/edit/<int:id>', quartier.edit_quartier, name ='edit_quartier'),
    path('quartier/update/<int:id>', quartier.update_quartier, name ='update_quartier'),
    path('quartier/delete/<int:id>', quartier.delete_quartier, name ='delete_quartier'),
]