from rest_framework import viewsets

from .serializers import CarSerializer, CarPriceSerializer
from .models import Car, CarPrice


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('price')
    serializer_class = CarSerializer


class CarPriceViewSet(viewsets.ModelViewSet):
    queryset = CarPrice.objects.all().order_by('price')
    serializer_class = CarPriceSerializer
