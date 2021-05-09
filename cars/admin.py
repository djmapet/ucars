from django.contrib import admin

# Register your models here.
from import_export.resources import ModelResource
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from .models import Manufacturer, CarModel, Car

class CarResource(ModelResource):
    class Meta:
        model = Car

        import_order = ('car_model', 'shop', 'color', 'gear', 'drive', 'body_type', 'model_year', 'plate_category', 'mileage', 'inspection_date', 'price')
        import_id_fields = ['id']


class CarAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'shop']
    resource_class = CarResource
    formats = [base_formats.TSV]


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
admin.site.register(CarModel)