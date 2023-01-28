
from django.contrib import admin
from django.urls import path

from djangoapp.views import temperatureApi, pressureApi, humidityApi

from django.urls import path



urlpatterns = [
    path('temperature', temperatureApi),
    path('humidity', humidityApi),
    path('pressure', pressureApi),
]
