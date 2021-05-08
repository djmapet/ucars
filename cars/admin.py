from django.contrib import admin

# Register your models here.
from .models import Manufacturer, CarModel

admin.site.register(Manufacturer)
admin.site.register(CarModel)