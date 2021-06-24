from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404,render


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
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'results.html', {'car': car})
