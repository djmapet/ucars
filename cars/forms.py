from django import forms
from cars.models import Car, Manufacturer, CarModel

class SearchForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = {'carmodel', 'body_type','gear', 'color', 'mileage','latest_inspection_date','price'}

    def clean_carmodel(self):
        carmodel = self.cleaned_data.get('carmodel')
        return carmodel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['carmodel'].required = False
        self.fields['latest_inspection_date'].required = False
