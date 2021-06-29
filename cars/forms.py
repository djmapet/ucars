from django import forms
from cars.models import Car, Manufacturer, CarModel

class SearchForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = {'carmodel', 'gear', 'color', 'mileage'}

    def clean_carmodel(self):
        carmodel = self.cleaned_data.get('carmodel')
        return carmodel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['carmodel'].required = False