from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Article(models.Model):
    title = models.CharField(max_length=250, null=True)
    text = models.CharField(max_length=10000, null=True)
    created_at = models.DateField(default=timezone.now)
    is_main = models.BooleanField(default=False)


class DictionaryTerm(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=5000, default="Описание временно отсутствует")


