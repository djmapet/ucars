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
        self.fields['mileage'].required = False
        self.fields['price'].required = False

class EditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = {'color','gear','body_type','drive','mileage','model_year','price'} #,'__all__'

        labels = {
            'name': '車の名前',
            'manufacturer': 'メーカー',
            'color':'車の色',
            'gear':'ギア',
            'body_type':'ボデイタイプ',
            'drive':'駆動方式',
            'mileage':'駆動方式',
            'model_year':'年式',
            'price':'値段'
        }

        help_text = {
            'name': '車の名前を入力',
            'manufacturer': 'メーカーを選択',
            'color':'車の色を選択',
            'gear':'ギアを選択',
            'body_type':'ボデイタイプを選択',
            'drive':'駆動方式を選択',
            'mileage':'駆動方式を選択',
            'model_year':'年式を選択',
            'price':'値段を入力'
        }

