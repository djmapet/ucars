from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404,render
from cars.forms import SearchForm


def top(request):
    cars = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # selected_carmodel = form.cleaned_data['carmodel']
            # selected_body_type = form.cleaned_data['body_type']
            selected_color = form.cleaned_data['color']
            # selected_gear = form.cleaned_data['gear']
            # mileage = form.cleaned_data['mileage']
            # price = form.cleaned_data['price']
            # latest_inspection_date = form.cleaned_data['latest_inspection_date']

            try:
                cars = Car.objects.all()
                # if selected_carmodel:
                #    cars = cars.filter(carmodel=int(selected_carmodel.id))
                # if selected_body_type:
                #    cars = cars.filter(body_type=selected_body_type)
                if selected_color:
                    cars = cars.filter(color__in=selected_color)
                # if selected_gear:
                #    cars = cars.filter(gear=selected_gear)
                # if mileage != None:
                #    cars = cars.filter(mileage__lt=mileage)
                # if latest_inspection_date:
                #    cars = cars.filter(latest_inspection_date__lt=latest_inspection_date)
                # if price != None:
                #    cars = cars.filter(price__lt=price)


            except Manufacturer.DoesNotExist:
                raise Http404("maker does not exist")
    else:
        form = SearchForm()

    context = {
        'carmodel_result' : cars,
        'form' : form,
    }


    return render(request, 'search.html', context)



def results(request):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'results.html', {'car': car})
