# _*_ coding: utf-8 _*_
# @Time     : 17:31
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Product, Photo, Item


class ProductAdmin(object):
    # 显示的列
    list_display = ['name', 'image', 'description', 'nutrition', 'effect', 'created']


class PhotoAdmin(object):
    # 显示的列
    list_display = ['product', 'image']


class ItemAdmin(object):
    # 显示的列
    list_display = ['product', 'description', 'price', 'unit', 'stock']


xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(Photo, PhotoAdmin)
xadmin.site.register(Item, ItemAdmin)
