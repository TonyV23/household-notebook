# Generated by Django 4.2.5 on 2023-09-29 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_person_numero_telephone_alter_person_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='est_verifie_par_chef_de_route',
        ),
    ]
