from django.urls import path, include
from djangoapp.views import MeasuresListView
from django.contrib import admin

urlpatterns = [
    path('api/', include('djangoapp.urls')),
    path('measurements/', MeasuresListView.as_view(),  name='measurements-list'),
    path('admin/', admin.site.urls),
]
