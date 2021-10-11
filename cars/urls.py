from django.urls import path
from .views import car, shop , search

urlpatterns = [
    path('car/<int:car_id>', car.detail),
    path('maker/<int:manufacturer_id>', car.maker_cars,name='maker'),
    path('shop/cars/<int:shop_id>', shop.shop_cars),
    path('shop/<int:shop_id>', shop.shop_info),
    path('edit/<int:car_id>', car.edit, name="edit"),
    path('edit/', car.edit, name="edit_new"),
    path('', search.top, name='search'),
    path('results/<int:car_id>', search.results, name='result'),
    path('maker_list', car.maker_list),
    path('shop_list',shop.shop_list),
    path('shop_info/<int:shop_id>',shop.shop_info),
    path('my_page/',car.mypage, name='my_page'),
]