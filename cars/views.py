from django.shortcuts import render
from cars.models import Car
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index")

def detail(request, car_id=1):
    try:
        car = Car.objects.get(pk=car_id)
        color = car.get_color()
        #mileage = car.get_mileage()
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    return HttpResponse("car id = %d" % car_id)
    return HttpResponse("car mileage = %d" % mileage)

def testview(request):
    user = request.user
