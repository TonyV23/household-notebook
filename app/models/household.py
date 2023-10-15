from django.db import models
from django.contrib.auth.models import User

from app.models import Province, Commune, Zone, Quartier

class Household(models.Model):
    designation = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT)
    quartier = models.ForeignKey(Quartier, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
 
    def __str__(self):
        return self.designation