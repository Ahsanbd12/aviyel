from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError

class User(AbstractBaseUser):
    RoleType = models.TextChoices('participant', 'speaker')
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=30)
    role = models.CharField(max_length=200, choices=RoleType.choices, default="participant")

    def __str__(self):
        return self.email
