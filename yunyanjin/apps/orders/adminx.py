# _*_ coding: utf-8 _*_
# @Time     : 17:37
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Order, OrderItem


class OrderAdmin(object):
    list_display = ['order_id', 'user', 'status', 'phone']


class OrderItemAdmin(object):
    list_display = ['order', 'item', 'quantity']


xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(OrderItem, OrderItemAdmin)