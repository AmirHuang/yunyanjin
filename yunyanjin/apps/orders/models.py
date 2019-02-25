from django.db import models
from django.contrib.auth.models import User
from shop.models import Item


class Order(models.Model):
    # Order status
    UNPAID = 'U'
    PAID = 'P'
    DISPATCHED = 'D'
    FINISHED = 'F'

    # Order status choices
    STATUS_CHOICES = (
        (UNPAID, '未支付'),
        (PAID, '已支付'),
        (DISPATCHED, '已发货'),
        (FINISHED, '已完成'),
    )

    order_id = models.UUIDField(primary_key=True, editable=False, verbose_name='订单编号')
    user = models.ForeignKey(User, related_name='orders', verbose_name='用户', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='状态')
    phone = models.CharField(max_length=11, verbose_name='电话号码')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '订单' + str(self.order_id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name='订单', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name='购买项目', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('数量')

    class Meta:
        verbose_name = '订单条目'
        verbose_name_plural = verbose_name
