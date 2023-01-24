
from rest_framework import serializers

from djangoapp.models import Temperature, Humidity, Pressure


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('temperature', 'dateTime')


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ('humidity', 'dateTime')


class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure
        fields = ('pressure', 'dateTime')
