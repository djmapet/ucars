from cars.models import Car, Shop
from django.http import HttpResponse, Http404
from django.shortcuts import render

def shop_info(request, shop_id):
    try:
        shop = Shop.objects.get(id=shop_id)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    context = {
        'name': shop.name,
        'tel': shop.tel,
        'email': shop.email,
        }
    return render(request, 'shop_info.html', context)

def shop_cars(request, shop_id):
    try:
        cars = Car.objects.filter(shop=shop_id)

    except Car.DoesNotExist:
        raise Http404("shop does not exist")

    context = {
        'cars': cars
    }
    return render(request, 'shop_cars.html', context)
