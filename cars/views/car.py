from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render
from cars.forms import NewCarForm
from django.shortcuts import redirect


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

def edit(request,car_id=None):
    car = None
    if car_id:
        try:
            car = Car.objects.get(pk=car_id)

        except Car.DoesNotExist:
            raise Http404("Car does not exist")

    if request.method == 'POST':
        form = NewCarForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required

            try:
                car = form.save(commit=False)
                car.save()
                status = 1


            except Car.DoesNotExist:
                raise Http404("maker does not exist")
        else:
            status = 2

            pass
    else:
        form = NewCarForm(instance=car)
        status = 2

    context = {
        'newcar': car,
        'car_id':car_id,
        'form': form,
        'status': status,


    }

    return render(request, 'edit.html', context)


