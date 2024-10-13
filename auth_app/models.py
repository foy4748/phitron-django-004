from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
