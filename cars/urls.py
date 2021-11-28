from django.urls import path

import views.car
from .views import car, shop , search
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('upload/',views.car.FileFieldFormView,name='upload'),
]

urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)