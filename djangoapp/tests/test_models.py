from django.test import TestCase
from djangoapp.models import Temperature, Humidity, Pressure
from decimal import Decimal
import datetime as DateTime

# models test


class ModelsTest(TestCase):
    TEMPERATURE = 15
    HUMIDITY = Decimal('70.0')
    PRESSURE = Decimal('450.0')

    def create_temperature(self, title="temperature model creation"):
        print(title)
        return Temperature.objects.create(temperature=self.TEMPERATURE)

    def create_pressure(self, title="pressure model creation"):
        print(title)
        return Pressure.objects.create(pressure=self.PRESSURE)

    def create_humidity(self, title="humidity model creation"):
        print(title)
        return Humidity.objects.create(humidity=self.HUMIDITY)

    def test_temperature(self, title="--temperature model test--"):  # Temperature
        print(title)
        temp = self.create_temperature()
        self.assertTrue(isinstance(temp, Temperature))
        self.assertTrue(isinstance(temp.dateTime, DateTime.datetime))
        self.assertTrue(isinstance(temp.temperature, int))
        self.assertEqual(temp.temperature, self.TEMPERATURE)

    def test_humidity_creation(self,  title="--humidity model test--"):  # Humidity
        print(title)
        hum = self.create_humidity()
        self.assertTrue(isinstance(hum, Humidity))
        self.assertTrue(isinstance(hum.dateTime, DateTime.datetime))
        self.assertTrue(isinstance(hum.humidity, Decimal))
        self.assertEqual(hum.humidity, self.HUMIDITY)

    def test_pressure_creation(self, title="--pressure model test--"):  # Preassure
        print(title)
        pres = self.create_pressure()
        self.assertTrue(isinstance(pres, Pressure))
        self.assertTrue(isinstance(pres.dateTime, DateTime.datetime))
        self.assertTrue(isinstance(pres.pressure, Decimal))
        self.assertEqual(pres.pressure, self.PRESSURE)
