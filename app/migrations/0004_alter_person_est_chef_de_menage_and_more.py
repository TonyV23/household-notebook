# Generated by Django 4.2.5 on 2023-10-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_person_date_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='est_chef_de_menage',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='est_verifie_par_chef_de_menage',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='est_verifie_par_chef_de_quartier',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
