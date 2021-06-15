from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render


def search(request):
    try:
        
