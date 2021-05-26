from django.contrib import admin

# Register your models here.
from import_export.resources import ModelResource
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .models import Manufacturer, CarModel, Car, Shop

class CarResource(ModelResource):
    id = Field(attribute='id', column_name='id')
    carmodel = Field(attribute='carmodel', column_name='carmodel', widget=ForeignKeyWidget(CarModel, 'name'))
    shop = Field(attribute='shop', column_name='shop name', widget=ForeignKeyWidget(Shop, 'name'))
    color = Field(attribute='color', column_name='color')
    gear = Field(attribute='gear', column_name='gear')
    drive = Field(attribute='drive', column_name='drive')
    body_type = Field(attribute='body_type', column_name='body_type')
    model_year = Field(attribute='model_year', column_name='model_year')
    plate_category = Field(attribute='plate_category', column_name='plate_category')
    mileage = Field(attribute='mileage', column_name='mileage')
    inspection_date = Field(attribute='inspection_date', column_name='inspection_date')
    price = Field(attribute='price', column_name='price')

    class Meta:
        model = Car
        import_order = ('carmodel', 'shop', 'color', 'gear', 'drive', 'body_type', 'model_year', 'plate_category', 'mileage', 'inspection_date', 'price')
        import_id_fields = ['id']

    def before_import_row(self, row, row_number=None, **kwargs):
        for n in Car.COLOR_CHOICES:
            if n[1] == row['color']:
                row['color'] = n[0]
                break

        for n in Car.GEAR_CHOICES:
            if n[1] == row['gear']:
                row['gear'] = n[0]
                break

        for n in Car.DRIVE_CHOICES:
            if n[1] == row['drive']:
                row['drive'] = n[0]
                break

        for n in Car.BODY_TYPE_CHOICES:
            if n[1] == row['body_type']:
                row['body_type'] = n[0]
                break

class CarAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'shop']
    resource_class = CarResource
    formats = [base_formats.CSV]

#メーカー
class ManufacturerResource(ModelResource):
    id = Field(attribute='id', column_name='id')
    manufacturer = Field(attribute='manufacturer', column_name='manufacturer')
    class Meta:
        model =  Manufacturer
        import_order = ('manufacturer')

    def before_import_row(self, row, row_number=None, **kwargs):
        for n in Manufacturer.MANUFACTURER_CHOICES:
            if n[1] == row['manufacturer']:
                row['manufacturer'] = n[0]
                break

class ManufacturerAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'manufacturer']
    resource_class = ManufacturerResource
    formats = [base_formats.CSV]

#ショップ
class ShopResource(ModelResource):
    id = Field(attribute='id', column_name='id')
    name = Field(attribute='name', column_name='name')
    tel = Field(attribute='tel', column_name='tel')
    email = Field(attribute='email', column_name='email')
    pref = Field(attribute='pref', column_name='pref')
    city = Field(attribute='city', column_name='city')
    area = Field(attribute='area', column_name='area')

    class Meta:
        model =  Shop
        import_order = ('name','tel','email','pref','city','area')

    def before_import_row(self, row, row_number=None, **kwargs):
        for n in Shop.NAME_CHOICES:
            if n[1] == row[name]:
                row['name'] = n[0]
                break
class ShopAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'shop']
    resource_class = ShopResource
    formats = [base_formats.CSV]

#カーモデル
class CarModelResource(ModelResource):
    name = Field(attribute='name', column_name='name')
    manufacturer = Field(attribute='manufacturer', column_name='manufacturer', widget=ForeignKeyWidget(CarModel, 'manufacturer'))

    class Meta:
        model =  CarModel
        import_order = ('name','manufacturer')

    def before_import_row(self, row, row_number=None, **kwargs):
        for n in CarModel.NAME_CHOICES:
            if n[1] == row[name]:
                row['name'] = n[0]
                break

class CarModelAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['name', 'manufacturer']
    resource_class = CarModelResource
    formats = [base_formats.CSV]




admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
admin.site.register(CarModel)
admin.site.register(Shop)
