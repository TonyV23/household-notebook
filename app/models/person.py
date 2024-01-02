from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

from app.models import Household, Province, Commune, Zone, Profession, Quartier, Status


class Person (models.Model):

    gender = (
        ('Male', 'Male'), ('Female', 'Female')
    )
    menage = models.ForeignKey(Household, on_delete=models.CASCADE)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    genre = models.CharField(choices=gender, max_length=20)
    numero_carte_id = models.CharField(max_length=30, unique=True)
    lieu_de_delivrance = models.CharField(max_length=30)
    province_de_residence = models.ForeignKey(Province, on_delete=models.CASCADE)
    commune_de_residence = models.ForeignKey(Commune, on_delete=models.CASCADE)
    zone_de_residence = models.ForeignKey(Zone, on_delete=models.CASCADE)
    quartier_de_residence = models.ForeignKey(Quartier, on_delete=models.CASCADE)
    rue = models.CharField(max_length=30, null=True, blank=True)
    lieu_de_naissance = models.CharField(max_length=50)
    annee_de_naissance = models.DateField()
    nom_du_pere = models.CharField(max_length=30)
    nom_de_la_mere = models.CharField(max_length=30)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    numero_telephone = models.CharField(max_length=15, null=True, blank=True)
    relation_avec_chefs_de_menage = models.ForeignKey(Status, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    est_chef_de_menage = models.BooleanField(default=False)
    est_verifie_par_chef_de_menage = models.BooleanField(default=False)
    est_verifie_par_chef_de_quartier = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    date_depart = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"
