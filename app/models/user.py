from django.db import models
from django.contrib.auth.models import User
from app.models import Quartier

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username