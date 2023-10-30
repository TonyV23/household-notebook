# Generated by Django 4.2.5 on 2023-10-30 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_zone_commune_alter_zone_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quartier',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_communes', to='app.commune'),
        ),
        migrations.AlterField(
            model_name='quartier',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_provinces', to='app.province'),
        ),
        migrations.AlterField(
            model_name='quartier',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_zones', to='app.zone'),
        ),
    ]
