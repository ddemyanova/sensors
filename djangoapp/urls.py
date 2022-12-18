
from django.contrib import admin
from django.urls import path

from djangoapp.views import MeasurementListSet, MeasurementListView

from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'measurements', MeasurementListSet)


urlpatterns = [
    path('', include(router.urls)),
]
