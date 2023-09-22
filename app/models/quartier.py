from django.db import models

from app.models import Province, Commune, Zone

class Quartier (models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    quartier = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.quartier