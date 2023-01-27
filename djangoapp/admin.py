from django.contrib import admin

from djangoapp.models import Temperature, Humidity, Pressure

admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Pressure)
