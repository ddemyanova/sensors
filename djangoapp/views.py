import os
from django.views import generic
from django.conf import settings

from djangoapp.models import PeriodicMeasurements


class MeasurementList(generic.ListView):
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
        return super(MeasurementList, self).get(request, *args, **kwargs)
