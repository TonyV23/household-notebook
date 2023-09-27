from django.urls import path

from app.views import home, person, province, commune, zone, quartier, profession, household, user, auth, visitor

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

    path('household', household.index, name ='view_household'),
    path('household/add', household.add_household, name ='add_household'),
    path('household/store', household.store_household, name ='store_household'),
    path('household/edit/<int:id>', household.edit_household, name ='edit_household'),
    path('household/update/<int:id>', household.update_household, name ='update_household'),
    path('household/delete/<int:id>', household.delete_household, name ='delete_household'),

    path('type_account', user.account_type, name='type_account_overview'),
    path('account/list_chef_family', user.index_chef_family, name=' '),
    path('account/list_chef_quarter', user.index_chef_quarter, name='account_overview_chef_quarter'),
    path('type_account/new_chef_family', user.add_user_chef_family, name='new_account_chef_family'),
    path('type_account/new_chef_quarter', user.add_user_chef_quarter, name='new_account_chef_quarter'),
    path('type_account/store/chef_family', user.store_user_chef_family, name='store_user_chef_family'),
    path('type_account/store/chef_quarter', user.store_user_chef_quarter, name='store_user_chef_quarter'),
    path('type_account/edit/<int:id>', user.edit_user, name='edit_user'),
    path('type_account/update/<int:id>', user.update_user, name='update_user'),
    path('type_account/delete/<int:id>', user.delete_user, name='delete_user'),

    path('login', auth.login_user, name='login'),
    path('logout', auth.logout_user, name='logout'),

    path('family_or_visitor', person.person_type, name='family_visitor_overview'),
    path('family_members', person.index, name='family_members_overview'),
    path('family/add', person.add_family_member, name='add_family_member'),
    path('family/store', person.store_family_member, name='store_family_member'),
    path('family/edit/<int:id>', person.edit_family_member, name='edit_family_member'),
    path('family/update/<int:id>', person.update_family_member, name='update_family_member'),
    path('family/delete/<int:id>', person.delete_family_member, name='delete_family_member'),


    path('visitors', visitor.index, name='visitors_overview'),
    path('visitor/add', visitor.add_visitor, name='add_visitor'),
    path('visitor/store', visitor.store_visitor, name='store_visitor'),
    path('visitor/edit/<int:id>', visitor.edit_visitor, name='edit_visitor'),
    path('visitor/update/<int:id>', visitor.update_visitor, name='update_visitor'),
    path('visitor/delete/<int:id>', visitor.delete_visitor, name='delete_visitor'),

]