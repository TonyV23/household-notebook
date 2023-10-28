from django.db import models

from app.models import Province

class Commune (models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    commune = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.commune