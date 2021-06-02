from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("index")

def detail(request, car_id=1):
    try:
        car = Car.objects.get(pk=car_id)
        color = car.get_color()
        mileage = car.mileage
        carmodel=car.carmodel
        model_name = carmodel.name
        manufacturer = carmodel.manufacturer
    except Car.DoesNotExist:
        raise Http404("Car does not exist")

    context = {
        'color': color,
        'mileage': mileage,
        'model_name': model_name,
        'manufacturer': manufacturer,
        }
    return render(request, 'car_detail.html', context)

def maker_list(request):
    try:
        makers = Manufacturer.objects.order_by('id')
    except Manufacturer.DoesNotExist:
        raise Http404("maker does not exist")

    context = {
        'makers': makers
    }
    return render(request, 'maker_list.html', context)


def maker_cars(request, manufacturer_id):
    try:
        models = CarModel.objects.filter(manufacturer=manufacturer_id)
        cars = Car.objects.filter(carmodel__in=models)
    except CarModel.DoesNotExist:
        raise Http404("cars does not exist")

    except Car.DoesNotExist:
        raise Http404("cars does not exist")

    context = {
        'cars': cars
    }
    return render(request, 'maker_cars.html', context)
