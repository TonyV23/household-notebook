# Generated by Django 4.2.5 on 2024-07-01 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_person_est_chef_de_menage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='genre',
            new_name='gender',
        ),
    ]