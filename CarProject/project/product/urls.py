from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path(r'^auth/', include('djoser.urls')),

    path('car/', CarViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='car_list'),
    path('car/<int:pk>/', CarViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),
    path('userprofile/', UserProfileSets.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/',
         UserProfileSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),
    path('accounth/', include('allauth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)