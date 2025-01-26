from django.contrib.auth.models import User
from django.db import models
import random

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_pin = models.CharField(max_length=4, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def generate_verification_pin(self):
        self.verification_pin = f"{random.randint(1000, 9999)}"
        self.save()

    def __str__(self):
        return self.user.username

