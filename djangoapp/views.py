import os
from django.http import HttpResponse
from django.views import generic
from django.conf import settings

from rest_framework import viewsets
from djangoapp.models import Temperature, Humidity, Pressure
from djangoapp.serializers import TemperatureSerializer, HumiditySerializer, PressureSerializer

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.core.files.storage import default_storage

# Create your views here.

def makeApi(request,  model, serializer,id=0):
    if request.method=='GET':
        elements = model.objects.all()
        elements_serializer=serializer(elements,many=True)
        data = {
            
            "statusCode": 200,
            "version": "1.0"
        }
        return HttpResponse(data)
    elif request.method=='POST':
        element_data=JSONParser().parse(request)
        elements_serializer=serializer(data=element_data)
        if elements_serializer.is_valid():
            elements_serializer.save()
            return HttpResponse("Added Successfully")
        return HttpResponse("Failed to Add")
    elif request.method=='PUT':
        element_data=HttpResponse().parse(request)
        element=model.objects.get(TemperatureId=element_data['TemperatureId'])
        elements_serializer=serializer(element,data=element_data)
        if elements_serializer.is_valid():
            elements_serializer.save()
            return HttpResponse("Updated Successfully")
        return HttpResponse("Failed to Update")
    elif request.method=='DELETE':
        element=model.objects.get(TemperatureId=id)
        element.delete()
        return HttpResponse("Deleted Successfully")
    else:
        return HttpResponse("No Request")


@csrf_exempt
def temperatureApi(request,id=0):
    makeApi(request,Temperature, TemperatureSerializer)
    
@csrf_exempt
def humidityApi(request,  id=0):
    makeApi(request,Humidity, HumiditySerializer)
    
@csrf_exempt
def pressureApi(request,id=0):
    makeApi(request,Pressure, PressureSerializer)
    
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
            # for hum in humidity_file:
            #   Humidity.objects.get_or_create(humidity=hum)
            context['humidity'] = Humidity.objects.all()

            pressure_file = self.openFile('pressure_test')
            # for pr in pressure_file:
            #     Pressure.objects.get_or_create(pressure=pr)
            context['pressure'] = Pressure.objects.all()

            temperature_file = self.openFile('temperature_test')
            # for temp in temperature_file:
            #     model.objects.get_or_create(temperature=temp)
            context['temperature'] = Temperature.objects.all()
            return context
        except IOError:
            pass
        return context

