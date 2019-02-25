# _*_ coding: utf-8 _*_
# @Time     : 17:41
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Cart


class CartAdmin(object):
    list_display = ['user', 'item', 'quantity']


xadmin.site.register(Cart, CartAdmin)

