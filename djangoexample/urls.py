from django.urls import path, include
from djangoapp.views import MeasuresListView

urlpatterns = [
    path('api/', include('djangoapp.urls')),
    path('measurements/', MeasuresListView.as_view(),  name='measurement_list'),

]
