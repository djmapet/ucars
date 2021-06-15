from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render


def search(request):
    try:
        car = Car.objects.get(pk=car_id)
        color = car.get_color()
        mileage = car.mileage
        carmodel=car.carmodel
        model_name = carmodel.name
        manufacturer = carmodel.manufacturer
        gear = car.get_gear()
        body_type = car.get_body_type()
        price = car.price
        latest_inspection_date = car.latest_inspection_date
        drive = car.get_drive()
        model_year = car.model_year
    except Car.DoesNotExist:
        raise Http404("Seach does not exist")

    context = {
        'color': color,
        'mileage': mileage,
        'model_name': model_name,
        'manufacturer': manufacturer,
        'gear' : gear,
        'BodyType': body_type,
        'price': price,
        'LastInspectionDate': latest_inspection_date,
        'drive' : drive,
        'model_year' : model_year,
        }
    return render(request, 'search.html', context)
