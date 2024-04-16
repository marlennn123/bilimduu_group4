from  django.urls import path, include, re_path
# from product.views import carViews
from  django.urls import path
from .views import *
urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path(r'^auth/', include('djoser.urls')),

    path('car/', CarViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='car_list'),
    path('car/<int:pk>/', CarViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),


]