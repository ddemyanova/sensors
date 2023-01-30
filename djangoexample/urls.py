from django.urls import path, include
from djangoapp.views import MeasuresListView, analytics_view
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/', include('djangoapp.urls')),
    path('measurements/', MeasuresListView.as_view(),  name='measurements-list'),
    path('analytics/', analytics_view,  name='analytics'),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()

