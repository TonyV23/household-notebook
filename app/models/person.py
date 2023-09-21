from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from app.models import Commune, Zone, Profession, Quartier

class Person (models.Model):

    relationship_with_parents = (
        ('ENFANTS','ENFANTS'),
        ('FAMILLE', 'MEMBRE_FAMILLE'),
        ('AMIS', 'AMIS'),
        ('GROOM', 'GROOM'),
    )

    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    numero_carte_id = models.CharField(max_length=30, unique=True)
    lieu_de_delivrance = models.CharField(max_length=30)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
    rue = models.CharField(max_length=30)
    lieu_de_naissance = models.CharField(max_length=50)
    annee_de_naissance = models.DateField()
    nom_du_pere = models.CharField(max_length=30)
    nom_de_la_mere = models.CharField(max_length=30)
    profession = models.ForeignKey(Profession, on_delete = models.CASCADE)
    numero_telephone = PhoneNumberField(null=True)
    relation_avec_chefs_de_menage = models.CharField(choices=relationship_with_parents,max_length=20, null=True)
    photo = models.ImageField(upload_to='photos/')
    est_chef_de_manage = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"