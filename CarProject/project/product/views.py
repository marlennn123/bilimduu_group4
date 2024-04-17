from django.forms import model_to_dict
from rest_framework import viewsets
# from rest_framework import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import CarSerializer,BetSerializer,UserProfileSerializer


class CarViewSets(viewsets.ModelViewSet):
    queryset =Car.objects.all()
    serializer_class = CarSerializer

    # def get(self, request):
    #     lst = Car.objects.all().values()
    #     return Response({'title': list(lst)})



    # def post(self, request):
        # post_new = Car.objects.create(
        #     category=request.data['category'],
        #     marka=request.data['marka'],
        #     model=request.data['model'],
        #     price=request.data['price'],
        #     year=request.data['year'],
        #     mileage=request.data['mileage'],
        #     city=request.data['city'],
        #     country=request.data['country'],
        #     color=request.data['color'],
        #     volume=request.data['volume'],
        #     description=request.data['description'],
        # )
        #
        # return Response({'post': model_to_dict(post_new)})


class BetViewSets(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer


class UserProfileSets(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = UserProfileSerializer