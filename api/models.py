import django
from django.db import models
from datetime import datetime


class Record(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    weight = models.PositiveIntegerField()
    lat = models.FloatField()
    log = models.FloatField()
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    photo = models.ImageField(upload_to="media/images", default="")
