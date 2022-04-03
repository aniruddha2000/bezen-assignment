import imp
import django
from django.db import models
from datetime import datetime
from api.resize_mixings import ResizeImageMixin


class Record(models.Model, ResizeImageMixin):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    weight = models.PositiveIntegerField()
    lat = models.FloatField()
    log = models.FloatField()
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    photo = models.ImageField(upload_to="media/images", default="")

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.resize(self.photo, (140, 140))

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "{} - {} - {}".format(self.name, self.species, self.timestamp)
