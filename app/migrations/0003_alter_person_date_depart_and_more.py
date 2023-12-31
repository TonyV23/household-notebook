# Generated by Django 4.2.5 on 2023-10-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_person_date_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_depart',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='numero_telephone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='rue',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
