from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Article(models.Model):
    text = models.CharField(max_length=10000, null=True)
    created_at = models.DateField(default=timezone.now)


class DictionaryTerm(models.Model):
    description = models.CharField(max_length=5000, default="Описание временно отсутствует")


