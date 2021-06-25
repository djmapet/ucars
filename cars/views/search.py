from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404,render
from cars.forms import SearchForm


def top(request):
    carmodel_result = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            #maker_id = form.cleaned_data['manufacturer']
            selected_carmodel = form.cleaned_data['carmodel']
            color_id = form.cleaned_data['color']
            gear_id = form.cleaned_data['gear']
            mileage = form.cleaned_data['mileage']

            try:
                #models = CarModel.objects.filter(pk=carmodel_id)
                carmodel_result = Car.objects.filter(carmodel=int(selected_carmodel.id))
            except Manufacturer.DoesNotExist:
                raise Http404("maker does not exist")
    else:
        form = SearchForm()

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
        'carmodel_result' : carmodel_result,
        'form' : form,
    }

    return render(request, 'search.html', context)


def results(request):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'results.html', {'car': car})
