from django.urls import path
from .views import car, shop

urlpatterns = [
    path('car/<int:car_id>', car.detail),
    path('shop/<int:shop_id>', shop.shop_info),
    path('', car.index),
]
