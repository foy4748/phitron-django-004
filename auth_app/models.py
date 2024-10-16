from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)

    def __str__(self):
        return f"Current Balance {self.balance}"
