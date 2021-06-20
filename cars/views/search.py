from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render


def top(request):
    try:
        makers = Manufacturer.objects.all()
    except Manufacturer.DoesNotExist:
        raise Http404("maker does not exist")

    try:
        car_models = CarModel.objects.all()
    except CarModel.DoesNotExist:
        raise Http404("car model does not exist")

    context = {
        'makers': makers,
        'car_models': car_models,
        'gears' : Car.GEAR_CHOICES,
        'color' : Car.COLOR_CHOICES,
    }

    return render(request, 'search.html', context)


def results(request):
    return render(request, 'results.html', {'makers': makers,'car_models': car_models,'gears' : Car.GEAR_CHOICES,'color' : Car.COLOR_CHOICES,})
