from django.urls import path
from .views import car, shop

urlpatterns = [
    path('car/<int:car_id>', car.detail),
    path('maker/<int:manufacturer_id>', car.maker_cars),
    path('shop/cars/<int:shop_id>', shop.shop_cars),
    path('shop/<int:shop_id>', shop.shop_info),
    path('', car.maker_list),
]
