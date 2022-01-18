from django.urls import path
from django.contrib import admin
from django.conf import settings

from .views import car, shop , search
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', search.top, name='search'),  # トップページ
#管理者用
    path('site_admin/', admin.site.urls),
    path('edit/<int:car_id>', car.edit, name="edit_car"),
    path('edit_new_car/', car.edit, name="edit_new_car"),  # 新規登録
    path('car/<int:car_id>', car.detail),  # 画像のアップロードを追加したい
    path('upload_car_pic/<int:car_id>', car.upload_file, name='upload'),
    path('upload_car_pic/file/name.txt', car.upload_file, name='upload_file'),
    path('success/url/', car.upload_file, name='success_file'),
#閲覧者用
    path('maker/<int:manufacturer_id>', car.maker_cars,name='maker'),
    path('shop/cars/<int:shop_id>', shop.shop_cars),
    path('shop/<int:shop_id>', shop.shop_info),
    path('results/<int:car_id>', search.results, name='result'),
    path('maker_list', car.maker_list),
    path('shop_list',shop.shop_list),
    path('shop_info/<int:shop_id>',shop.shop_info),
    path('my_page/',car.mypage, name='my_page'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)