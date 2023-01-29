import os
from django.http import HttpResponse
from django.views import generic
from django.conf import settings

from rest_framework import viewsets, status
from djangoapp.models import Temperature, Humidity, Pressure
from djangoapp.serializers import TemperatureSerializer, HumiditySerializer, PressureSerializer

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def makeApi(request,model, serializer):
    if request.method == 'GET':
        elements = model.objects.all()
        elements_serializer = serializer(elements, many=True)
        return JsonResponse(elements_serializer.data, safe=False)
    elif request.method == 'POST':
        element_data = JSONParser().parse(request)
        element_serializer = serializer(data=element_data)
        if element_serializer.is_valid():
            element_serializer.save()
            return JsonResponse(element_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(element_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("No Request")


@csrf_exempt
def temperatureApi(request): 
    return makeApi(request, Temperature, TemperatureSerializer)
    
@csrf_exempt
def humidityApi(request):
    return makeApi(request, Humidity, HumiditySerializer)
    
@csrf_exempt
def pressureApi(request):
    return makeApi(request, Pressure, PressureSerializer)
    
class MeasuresListView(generic.ListView):
    model = Humidity
    context_object_name = 'measures'
    template_name = 'measurement_list.html'

    def get_context_data(self):
        context = super(MeasuresListView, self).get_context_data()
        try:
            # for hum in humidity_file:
            #   Humidity.objects.get_or_create(humidity=hum)
            context['humidity'] = Humidity.objects.all()
            # for pr in pressure_file:
            #     Pressure.objects.get_or_create(pressure=pr)
            context['pressure'] = Pressure.objects.all()
            # for temp in temperature_file:
            #     model.objects.get_or_create(temperature=temp)
            context['temperature'] = Temperature.objects.all()
            return context
        except IOError:
            pass
        return context

