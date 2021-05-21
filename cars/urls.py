from django.urls import path
from . import views

urlpatterns = [
    path('<int:car_id>', views.detail),
    path('shop/<int:shop_id>', views.shop_info),
    path('', views.index),
]
