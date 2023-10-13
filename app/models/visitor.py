from django.db import models

from app.models import Household, Province, Commune, Zone, Profession, Quartier

class Visitor(models.Model):
    relationship_with_parents = (
        ('MEMBRE_FAMILLE', 'MEMBRE_FAMILLE'),
        ('AMIS', 'AMIS'),
        ('GROOM', 'GROOM'),
    )

    gender = (
        ('Male', 'Male'), ('Female', 'Female')
    )

    menage = models.ForeignKey(Household, on_delete=models.PROTECT)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    genre = models.CharField(choices=gender, max_length=20)
    numero_carte_id = models.CharField(max_length=30, unique=True)
    lieu_de_delivrance = models.CharField(max_length=30)
    province_de_residence = models.ForeignKey(Province, on_delete=models.PROTECT)
    commune_de_residence = models.ForeignKey(Commune, on_delete=models.PROTECT)
    zone_de_residence = models.ForeignKey(Zone, on_delete=models.PROTECT)
    quartier_de_residence = models.ForeignKey(Quartier, on_delete=models.PROTECT)
    rue = models.CharField(max_length=30, blank=True)
    lieu_de_naissance = models.CharField(max_length=50)
    annee_de_naissance = models.DateField()
    nom_du_pere = models.CharField(max_length=30)
    nom_de_la_mere = models.CharField(max_length=30)
    profession = models.ForeignKey(Profession, on_delete=models.PROTECT)
    numero_telephone = models.CharField(max_length=15, null=True, blank=True)
    relation_avec_chefs_de_menage = models.CharField(choices=relationship_with_parents, max_length=20)
    photo = models.ImageField(upload_to='app/photos/', blank=True)

    est_verifie_par_chef_de_menage = models.BooleanField(default=False)
    est_verifie_par_chef_de_quartier = models.BooleanField(default=False)
    date_arrive = models.DateTimeField(auto_now_add=True)
    date_depart = models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom} (Visiteur)"