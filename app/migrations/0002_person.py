# Generated by Django 4.2.5 on 2023-09-22 14:13

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=15)),
                ('numero_carte_id', models.CharField(max_length=30, unique=True)),
                ('lieu_de_delivrance', models.CharField(max_length=30)),
                ('rue', models.CharField(max_length=30)),
                ('lieu_de_naissance', models.CharField(max_length=50)),
                ('annee_de_naissance', models.DateField()),
                ('nom_du_pere', models.CharField(max_length=30)),
                ('nom_de_la_mere', models.CharField(max_length=30)),
                ('numero_telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('relation_avec_chefs_de_menage', models.CharField(choices=[('ENFANTS', 'ENFANTS'), ('MEMBRE_FAMILLE', 'MEMBRE_FAMILLE'), ('AMIS', 'AMIS'), ('GROOM', 'GROOM')], max_length=20, null=True)),
                ('photo', models.ImageField(upload_to='app/photos/')),
                ('est_chef_de_manage', models.BooleanField(default=False)),
                ('commune_de_residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commune')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profession')),
                ('province_de_residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.province')),
                ('quartier_de_residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quartier')),
                ('zone_de_residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.zone')),
            ],
        ),
    ]
