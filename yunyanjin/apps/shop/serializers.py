# _*_ coding: utf-8 _*_
# @Time     : 19:00
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from .models import Product, Photo, Item


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPhotoSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(many=False)

    class Meta:
        model = Photo
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(many=False)

    class Meta:
        model = Item
        fields = '__all__'
