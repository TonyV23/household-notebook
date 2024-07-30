# Generated by Django 4.2.5 on 2024-04-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='est_chef_de_menage',
            field=models.IntegerField(choices=[(1, 'Oui'), (0, 'Non')], max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='est_verifie_par_chef_de_menage',
            field=models.IntegerField(choices=[(1, 'Oui'), (0, 'Non')], max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='est_verifie_par_chef_de_quartier',
            field=models.IntegerField(choices=[(1, 'Oui'), (0, 'Non')], max_length=1),
        ),
    ]
