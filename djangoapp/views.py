import os
from django.views import generic
from django.conf import settings

from rest_framework.decorators import api_view
from django.shortcuts import render


from djangoapp.analytics.analytics import Analytics

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
            # humidity_file = self.openFile('humidity_test')
            # for hum in humidity_file:
            #   Humidity.objects.get_or_create(humidity=hum)
            context['humidity'] = Humidity.objects.all()

            # pressure_file = self.openFile('pressure_test')
            # for pr in pressure_file:
            #     Pressure.objects.get_or_create(pressure=pr)
            context['pressure'] = Pressure.objects.all()

            # temperature_file = self.openFile('temperature_test')
            # for temp in temperature_file:
            #     Temperature.objects.get_or_create(temperature=temp)
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


@api_view()
def analytics_view(request):
    analytics = Analytics()
    prediction_temperature, rmse_temperature = analytics.getTestDataTemp()
    prediction_humidity, rmse_humidity = analytics.getTestDataHum()
    prediction_pressure, rmse_pressure = analytics.getTestDataPr()
    contextDict={
        'humidity': analytics.get_humidityHtml,
        'pressure': analytics.get_pressureHtml,
        'temperature': analytics.get_temperatureHtml,
        'max_temperature': analytics.temperatureSeries.max,
        'min_temperature': analytics.temperatureSeries.min,
        'max_humidity': analytics.humiditySeries.max,
        'min_humidity': analytics.humiditySeries.min,
        'max_pressure': analytics.pressureSeries.max,
        'min_pressure': analytics.pressureSeries.min,
        'pressureLineGraph': analytics.get_pressureLineGraph,
        'humidityBarGraph': analytics.get_humidityBarGraph,
        'temperatureBarGraph': analytics.get_temperatureBarGraph,
        'correlationTemperaturePressureLineGraph': analytics.get_correlationTempPrLineGraph,
        'correlationHumidityTemperatureLineGraph': analytics.get_correlationHumTempLineGraph,
        'correlationPressureHumidityLineGraph': analytics.get_correlationPrHumLineGraph,
        'humidity_description': analytics.humiditySeries.describe(),
        'pressure_description': analytics.pressureSeries.describe(),
        'temperature_description': analytics.temperatureSeries.describe(),
        'prediction_temperature': prediction_temperature,
        'prediction_humidity': prediction_humidity,
        'prediction_pressure': prediction_pressure,
        'rmse_temperature': rmse_temperature,
        'rmse_humidity': rmse_humidity,
        'rmse_pressure': rmse_pressure
    }
    return render(request, 'analytics.html', contextDict)
