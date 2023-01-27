from django.test import TestCase
from djangoapp.models import Temperature, Humidity, Pressure
from django.utils import timezone
from django.core.urlresolvers import reverse
from whatever.forms import WhateverForm

# models test
class ModelsTest(TestCase):

    def create_temperature(self, title="temperature model creation", body=""):
        return Temperature.objects.create(temperature = 15)
        
    def create_pressure(self, title="pressure model creation", body=""):
        return Pressure.objects.create(pressure = 450.0)

    def create_humidity(self, title="humidity model creation", body=""):
        return Humidity.objects.create(pressure = 70.0)

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, Whatever))
        self.assertEqual(w.__unicode__(), w.title)