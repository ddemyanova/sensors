
from rest_framework import serializers

from djangoapp.models import PeriodicMeasurements


class PeriodicMeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicMeasurements
        fields = ('temperature', 'humidity', 'pressure', 'dateTime')
