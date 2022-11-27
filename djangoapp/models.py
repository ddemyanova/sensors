from __future__ import unicode_literals
from django.db import models


class Temperature (models.Model):
    value = models.IntegerField()


class Humidity (models.Model):
    value = models.DecimalField(
        decimal_places=2, max_digits=6)


class Pressure (models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=7)


class PeriodicMeasurements (models.Model):
    temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
    humidity = models.ForeignKey(Humidity, on_delete=models.CASCADE)
    pressure = models.ForeignKey(Pressure, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True)


class Unit (models.Model):
    unit = models.CharField(max_length=50)
    measurement = models.CharField(unique=True, max_length=50)


def __unicode__(self):
    return self.value
