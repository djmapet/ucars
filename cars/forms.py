from django import forms
from cars.models import Car, Manufacturer, CarModel

class SearchForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = {'carmodel', 'body_type', 'gear', 'color', 'mileage', 'latest_inspection_date', 'price'}

    def clean_carmodel(self):
        carmodel = self.cleaned_data.get('carmodel')
        return carmodel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['carmodel'].required = False
        self.fields['latest_inspection_date'].required = False
        self.fields['mileage'].required = False
        self.fields['price'].required = False



class NewCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = {'carmodel', 'color', 'gear', 'body_type', 'drive', 'mileage', 'model_year', 'price'}

        labels = {
            'carmodel': '車の名前',
            'manufacturer': 'メーカー',
            'color': '車の色',
            'gear': 'ギア',
            'body_type': 'ボデイタイプ',
            'drive': '駆動方式',
            'mileage': '走行距離',
            'model_year': '年式',
            'price': '値段'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['carmodel'].initial = None
        self.fields['color'].initial = None
        self.fields['gear'].initial = None
        self.fields['body_type'].initial = None
        self.fields['drive'].initial = None
        self.fields['mileage'].initial = None
        self.fields['model_year'].initial = None
        self.fields['price'].initial = None
        BODY_TYPE_CHOICES = [
            ('----','None'),
            (Car.TYPE_SEDAN, 'SEDAN'),
            (Car.TYPE_COUPE, 'COUPE'),
            (Car.TYPE_WAGON, 'WAGON'),
        ]
        self.fields['body_type'].ChoiceField(
                                        choices = BODY_TYPE_CHOICES,
                                        required=False,
                                        widget=forms.widgets.Select,)

    def clean_car(self):
        car = self.cleaned_data.post('car')
        return car


