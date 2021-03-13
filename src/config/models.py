from django.db import models


class Config(models.Model):
    ip = models.CharField(max_length=15)

    port = models.IntegerField()

    hash = models.IntegerField()

    user = models.CharField(max_length=255)

    password = models.CharField(max_length=255)
