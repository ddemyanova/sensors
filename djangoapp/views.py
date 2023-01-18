import os
from django.views import generic
from django.conf import settings

from rest_framework import viewsets
from djangoapp.models import Temperature, Humidity, Pressure
from djangoapp.serializers import TemperatureSerializer, HumiditySerializer, PressureSerializer


class TemperatureListSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer


class HumidityListSet(viewsets.ModelViewSet):
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer


class PressureListSet(viewsets.ModelViewSet):

    queryset = Pressure.objects.all()
    serializer_class = PressureSerializer


class MeasuresListView(generic.ListView):
    model = Humidity
    context_object_name = 'measures'
    template_name = 'measurement_list.html'

    def openFile(self, fileName):
        return open(os.path.join(
            settings.BASE_DIR, fileName), 'r')

    def get_context_data(self):
        context = super(MeasuresListView, self).get_context_data()
        try:
            humidity_file = self.openFile('humidity_test')
            for hum in humidity_file:
                Humidity.objects.get_or_create(humidity=hum)
            context['humidity'] = Humidity.objects.all()

            pressure_file = self.openFile('pressure_test')
            for pr in pressure_file:
                Pressure.objects.get_or_create(pressure=pr)
            context['pressure'] = Pressure.objects.all()

            temperature_file = self.openFile('temperature_test')
            for temp in temperature_file:
                Temperature.objects.get_or_create(temperature=temp)
            context['temperature'] = Temperature.objects.all()
            return context
        except IOError:
            pass
        return context


# class HumidityListView(generic.ListView):
#     model = Humidity
#     context_object_name = 'humidity'
#     template_name = 'measurement_list.html'

#     def openFile(self, fileName):
#         return open(os.path.join(
#             settings.BASE_DIR, fileName), 'r')

#     def get(self, request, *args, **kwargs):
#         try:
#             humidity_file = self.openFile('humidity_test')
#             for hum in humidity_file:
#                 Humidity.objects.get_or_create(humidity=hum)

#         except IOError:
#             pass
#         return super(HumidityListView, self).get(request, *args, **kwargs)


# class PressureListView(generic.ListView):
#     model = Pressure
#     context_object_name = 'pressure'
#     template_name = 'measurement_list.html'

#     def openFile(self, fileName):
#         return open(os.path.join(
#             settings.BASE_DIR, fileName), 'r')

#     def get(self, request, *args, **kwargs):
#         try:
#             pressure_file = self.openFile('pressure_test')
#             for pr in pressure_file:
#                 print('here', pr)
#                 Pressure.objects.get_or_create(pressure=pr)

#         except IOError:
#             pass
#         return super(PressureListView, self).get(request, *args, **kwargs)


# class TemperatureListView(generic.ListView):
#     model = Temperature
#     context_object_name = 'temperature'
#     template_name = 'measurement_list.html'

#     def openFile(self, fileName):
#         return open(os.path.join(
#             settings.BASE_DIR, fileName), 'r')

#     def get(self, request, *args, **kwargs):
#         try:
#             temperature_file = self.openFile('temperature_test')
#             for temp in temperature_file:
#                 Temperature.objects.get_or_create(temperature=temp)

#         except IOError:
#             pass
#         return super(TemperatureListView, self).get(request, *args, **kwargs)
