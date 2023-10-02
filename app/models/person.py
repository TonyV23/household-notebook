from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

from app.models import Household, Province, Commune, Zone, Profession, Quartier


class Person (models.Model):

    relationship_with_parents = (
        ('PARENT', 'PARENT'),
        ('ENFANT', 'ENFANT')
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

    est_chef_de_menage = models.BooleanField(default=False)
    est_verifie_par_chef_de_menage = models.BooleanField(default=False)
    est_verifie_par_chef_de_quartier = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created_by = kwargs.pop('request').user
    #     super().save(*args, **kwargs)

    # to make the save method working

    # def my_view(request):
    # if request.method == 'POST':
    #     form = MyForm(request.POST)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.save(request=request)  # Pass the request object to the save() method
    #         # Rest of the view logic
    # else:
    #     form = MyForm()

    # context = {
    #     'form': form
    # }
    # return render(request, 'my_template.html', context)
