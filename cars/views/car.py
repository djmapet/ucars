from cars.models import Car, Shop
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
        'manufacturer': manufacturer
        }
    return render(request, 'car_detail.html', context)
