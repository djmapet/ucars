from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render
from cars.forms import NewCarForm, SearchForm
from django.shortcuts import redirect
from urllib import parse
from django import template
from django.shortcuts import resolve_url

register = template.Library()


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

def get_return_link(request):
    top_page = resolve_url('search:top')  # 最新の日記一覧
    referer = request.environ.get('HTTP_REFERER')  # これが、前ページのURL

    # URL直接入力やお気に入りアクセスのときはリファラがないので、トップぺージに戻す
    if referer:

        # リファラがある場合、前回ページが自分のサイト内であれば、そこに戻す。
        parse_result = parse.urlparse(referer)
        if request.get_host() == parse_result.netloc:
            return referer

    return top_page

