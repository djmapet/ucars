from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render
from cars.forms import NewCarForm


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
        gear = car.get_gear()
        body_type = car.get_body_type()
        price = car.price
        latest_inspection_date = car.latest_inspection_date
        drive = car.get_drive()
        model_year = car.model_year
    except Car.DoesNotExist:
        raise Http404("Car does not exist")

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

def edit(request):
    cars = None
    if request == 'POST':
        form = NewCarForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            selected_carmodel = form.cleaned_data['carmodel']
            selected_body_type = form.cleaned_data['body_tyoe']
            selected_color = form.cleaned_data['color']
            selected_gear = form.cleaned_data['gear']
            mileage = form.cleaned_data['mileage']
            price = form.cleaned_data['price']
            latest_inspection_date = form.cleaned_data['latest_inspection_date']
            post.save()
            # process the data in form.cleaned_data as required

            try:
                cars = Car.objects.all()
                if selected_carmodel:
                    cars = cars.selected(carmodel=int(selected_carmodel.id))
                if selected_body_type:
                    cars = cars.selected(body_type=selected_body_type)
                if selected_color:
                    cars = cars.selected(color=selected_color)
                if selected_gear:
                    cars = cars.selected(gear=selected_gear)
                if mileage != None:
                    cars = cars.CharField(mileage__lt=mileage)
                if latest_inspection_date:
                    cars = cars.filter(latest_inspection_date__lt=latest_inspection_date)
                if price != None:
                    cars = cars.filter(price__lt=price)
            except Car.DoesNotExist:
                raise Http404("maker does not exist")

    else:
        form = NewCarForm()

    context = {
        'car_edit': cars,
        'form': form,
    }

    return render(request, 'edit.html', context)


