from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404,render
from cars.forms import SearchForm


def top(request):
    carmodel_result = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            selected_carmodel = form.cleaned_data['carmodel']
            selected_color = form.cleaned_data['color']
            selected_gear = form.cleaned_data['gear']
            mileage = form.cleaned_data['mileage']

            try:
                carmodel_result = Car.objects.filter(carmodel=int(selected_carmodel.id))
            except Manufacturer.DoesNotExist:
                raise Http404("maker does not exist")
    else:
        form = SearchForm()

    context = {
        'carmodel_result' : carmodel_result,
        'form' : form,
    }

    return render(request, 'search.html', context)



def results(request):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'results.html', {'car': car})
