from django import forms
import copy
from datetime import datetime,timedelta
from cars.models import Car, Manufacturer, CarModel

class SearchForm(forms.Form):

    fields = {'carmodel', 'color', 'gear', 'body_type', 'latest_inspection_date', 'mileage', 'price'}
    labels = {
        'carmodel' : '車の名前',
        'color' :  '車の色',
        'gear' : '車のギア',
        'body_type' : '車種',
        'latest_inspection_date' : '車検日',
        'mileage' : '走行距離',
        'price' : '価格',
    }

    carmodel = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),
        choices=CarModel.get_carmodel_choices(),
        label='車の名前',
    )
    color = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Car.COLOR_CHOICES,
        label='車の色',
    )
    Car.GEAR_CHOICES.insert(0, (-1, '未設定'))
    gear = forms.ChoiceField(
        choices=Car.GEAR_CHOICES,
        required=False,
        label='車のギア',
    )
    Car.BODY_TYPE_CHOICES.insert(0, (0, '未設定'))
    body_type = forms.ChoiceField(
        choices=Car.BODY_TYPE_CHOICES,
        required=False,
        label='車種',
    )
    mileage = forms.IntegerField(required=False,label='走行距離')
    latest_inspection_date = forms.DateField(required=False,label='車検日')
    price = forms.IntegerField(required=False,label='価格')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NewCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = {'carmodel', 'color', 'gear', 'body_type', 'drive', 'mileage', 'model_year', 'price', 'plate_category', 'latest_inspection_date'}

        labels = {
            'carmodel': '車の名前',
            'manufacturer': 'メーカー',
            'color': '車の色',
            'gear': 'ギア',
            'body_type': 'ボデイタイプ',
            'drive': '駆動方式',
            'mileage': '走行距離',
            'model_year': '年式',
            'price': '値段',
            'plate_category': '車のサイズ',
            'latest_inspection_date': '車検日',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['carmodel'].initial = None

        color_list = copy.deepcopy(Car.COLOR_CHOICES)
        item = (None, 'カラーを選んで下さい')
        color_list.insert(0,item)
        self.fields['color'].choices = color_list
        self.fields['gear'].initial = None
        self.fields['body_type'].initial = None

        self.fields['drive'].initial = None
        self.fields['mileage'].initial = None
        self.fields['model_year'].initial = None
        self.fields['price'].initial = None
        self.fields['plate_category'].initial = None
        self.fields['latest_inspection_date'].initial = None


        body_type_list = copy.deepcopy(Car.BODY_TYPE_CHOICES)
        item = (None,'ボディタイプを選んで下さい')
        body_type_list.insert(0,item)
        self.fields['body_type'].choices = body_type_list

    def clean_car(self):
        car = self.cleaned_data.post('car')
        return car

    def clean_body_type(self):
        body_type = self.cleaned_data.get('body_type')
        if body_type not in [Car.TYPE_SEDAN,Car.TYPE_COUPE,Car.TYPE_WAGON]:
            raise forms.ValidationError('選択してください')
        return body_type

    def clean_latest_inspection_date(self):
        latest_inspection_date = self.cleaned_data.get('latest_inspection_date')
        today = datetime.today()
        years_ago = today - timedelta(days=365 * 5)
        years_late = today + timedelta(days=365 * 5)
        if latest_inspection_date < datetime.date(years_ago):
            raise forms.ValidationError('車検日を確認してください')
        if latest_inspection_date > datetime.date(years_late):
            raise forms.ValidationError('車検日を確認してください')
        return latest_inspection_date
