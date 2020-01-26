# -*- coding: utf-8 -*-
"""
"""

from rest_framework import serializers

from .models import Car, CarPrice


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'company', 'model',
                  'product_year', 'price')


class CarPriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarPrice
        fields = ('id', 'price')
