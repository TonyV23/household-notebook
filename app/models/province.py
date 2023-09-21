from django.db import models

class Province (models.Model):
    province = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.province