# _*_ coding: utf-8 _*_
# @Time     : 14:34
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from shop.serializers import ItemSerializer
from shop.models import Item
from .models import Cart


class CartSerializer(serializers.Serializer):
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    item = serializers.PrimaryKeyRelatedField(required=True,
                                              queryset=Item.objects.all())
    quantity = serializers.IntegerField(required=True,
                                        label='数量',
                                        min_value=1,
                                        error_messages={
                                            'min_value': '商品数量不能少于一',
                                            'required': '请选择购买的数量'
                                        })

    # 继承的serializer 没有save功能, 必须写一个create方法
    def create(self, validated_data):
        # validated_data 表示已经处理过的数据
        # 获取当前的用户
        # view中, self.request.user;
        # 在serializer中, self.context['request'].user
        user = self.context['request'].user
        quantity = validated_data['quantity']
        item = validated_data['item']

        # 判断购物车里面是否有记录
        existed = Cart.objects.filter(user=user, item=item)
        # 如果购物车有记录 数量+添加数量
        # 如果购物车没有记录 创建记录
        if existed:
            existed = existed[0]
            existed.quantity += quantity
            existed.save()
        else:
            # 创建这条记录
            existed = Cart.objects.create(**validated_data)
        return existed

    def update(self, instance, validated_data):
        # 修改商品中的数量
        instance.quantity = validated_data['quantity']
        instance.save()
        return instance


class CartListSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False, read_only=True)

    class Meta:
        model = Cart
        fields = ('item', 'quantity',)
