from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Appuser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to="profilePIC/")

    def __str__(self) -> str:
        return self.user.username if self.user else "No user"

           