from django.urls import path, include
from djangoapp.views import MeasurementListView

urlpatterns = [
    path('api/', include('djangoapp.urls')),
    path('measurements/', MeasurementListView.as_view(),  name='measurement_list'),
]
