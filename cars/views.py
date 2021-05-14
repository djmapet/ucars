from django.shortcuts import render
from cars.models import Car
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index")

def detail(request, car_id=1):
    return HttpResponse("car id = %d" % car_id)