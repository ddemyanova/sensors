from __future__ import unicode_literals
from django.db import models


class Temperature (models.Model):
    temperature = models.IntegerField()
    dateTime = models.DateTimeField(auto_now_add=True)


class Humidity (models.Model):
    humidity = models.DecimalField(decimal_places=1, max_digits=6)
    dateTime = models.DateTimeField(auto_now_add=True)


class Pressure (models.Model):
    pressure = models.DecimalField(decimal_places=1, max_digits=7)
    dateTime = models.DateTimeField(auto_now_add=True)


def __unicode__(self):
    return self.value
