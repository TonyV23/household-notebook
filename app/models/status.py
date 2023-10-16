from django.db import models

class Status (models.Model):
    status = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.status