from django.db import models

from app.models import Person

class Visitor(Person):
    date_arrive = models.DateField(auto_now_add=True)
    date_depart = models.DateField()

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom} (Visiteur)"