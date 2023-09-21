from django.db import models

class Profession (models.Model):
    profession = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.profession