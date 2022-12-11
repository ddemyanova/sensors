from __future__ import unicode_literals
from django.db import models


class PeriodicMeasurements (models.Model):
    temperature = models.IntegerField()
    humidity = models.DecimalField(decimal_places=2, max_digits=6)
    pressure = models.DecimalField(decimal_places=2, max_digits=7)
    dateTime = models.DateTimeField(auto_now_add=True)


def __unicode__(self):
    return self.value
