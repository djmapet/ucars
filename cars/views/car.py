from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render
from cars.forms import EditForm


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
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('list')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = EditForm()
    return render(request, 'edit.html', params)

"""
def new_register_list(request):
    data = Member.objects.all()
    params = {'message': 'メンバーの一覧', 'data': data}
    return render(request, 'edit.html', params)    
"""