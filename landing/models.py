from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class DictionaryTerm(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=5000, default="Описание временно отсутствует")

