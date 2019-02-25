from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from .models import Cart
from .serializers import CartListSerializer, CartSerializer


class CartViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if self.action == 'list':
            return CartListSerializer
        else:
            return CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    # 库存 加
    def perform_destroy(self, instance):
        item = instance.item
        item.stock += instance.quantity
        item.save()
        instance.delete()

    # 库存 减
    def perform_create(self, serializer):
        cart = serializer.save()
        item = cart.item
        item.stock -= int(self.request.data.get('quantity'))
        item.save()

    # 更新库存 修改可能是增加 也可以能是减少
    def perform_update(self, serializer):
        # 首先先获取之前的的数量
        existed_record = Cart.objects.get(id=serializer.instance.id)
        existed_quantity = existed_record.quantity
        # 先保持之前的数据 existed_nums
        saved_record = serializer.save()
        # 变化量
        nums = saved_record.quantity - existed_quantity
        item = saved_record.item
        item.stock -= nums
        item.save()
