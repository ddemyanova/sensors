import os
from django.views import generic
from django.conf import settings

from rest_framework import viewsets
from djangoapp.models import PeriodicMeasurements
from djangoapp.serializers import PeriodicMeasurementsSerializer


class MeasurementListSet(viewsets.ModelViewSet):
    queryset = PeriodicMeasurements.objects.all()
    serializer_class = PeriodicMeasurementsSerializer


class MeasurementListView(generic.ListView):
    model = PeriodicMeasurements
    context_object_name = 'measurements'
    template_name = 'measurement_list.html'

    def openFile(self, fileName):
        return open(os.path.join(
            settings.BASE_DIR, fileName), 'r')

    def get(self, request, *args, **kwargs):
        try:
            temperature_file = self.openFile('temperature_test')
            humidity_file = self.openFile('humidity_test')
            pressure_file = self.openFile('pressure_test')
            for temp, hum, pr in zip(temperature_file, humidity_file, pressure_file):
                PeriodicMeasurements.objects.get_or_create(
                    temperature=temp, humidity=hum, pressure=pr)

        except IOError:
            pass
        return super(MeasurementListView, self).get(request, *args, **kwargs)
