
from django.contrib import admin
from django.urls import path

from djangoapp.views import TemperatureListSet, HumidityListSet, PressureListSet

from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'temperature', TemperatureListSet)
router.register(r'humidity', HumidityListSet)
router.register(r'pressure', PressureListSet)



urlpatterns = [
    path('', include(router.urls)),
]
