from django.conf import settings

from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render
from cars.forms import NewCarForm, SearchForm,UploadFileForm
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files.storage import default_storage
from cars.forms import UploadFileForm
import time

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

                if car_id:
                    message = " car_id %d の情報を更新しました" % (car_id)
                    context = {
                        'message': message,
                        'car': car,
                    }
                else:
                    message = " car_id %d を新規に登録しました" % (car.id)
                    context = {
                        'message' : message,
                        'car' : car,
                    }
                return render(request,'success.html',context)
            except Car.DoesNotExist:
                raise Http404("maker does not exist")
        else:
            pass
    else:
        form = NewCarForm(instance=car)

    context = {
        'car_id':car_id,
        'form': form,

    }

    return render(request, 'edit.html', context)

def searchform(request):
    form=SearchForm()
    context = {'form':form,}
    return render(request,'search.html',context)


def mypage(request):
    return render(request,'my_page.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        ja = time.time()
        file_name = str(ja)+".jpg"
        img_path = settings.CAR_IMG_URL+file_name   # temporary
        img_url = settings.CAR_IMG_ROOT+file_name
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], img_path)
            #return HttpResponse('success/url/')
            context = {
                'img_path': img_path,
                'img_url': img_url,
            }
            return render(request,'uploaded.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html',{'form':form})

def handle_uploaded_file(f, img_path):
    with open(img_path, 'wb+') as destination: #合わない
        for chunk in f.chunks():
            destination.write(chunk)

