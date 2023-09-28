from django.db import models

from app.models import Province, Commune

class Zone (models.Model):
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT)
    zone = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.zone