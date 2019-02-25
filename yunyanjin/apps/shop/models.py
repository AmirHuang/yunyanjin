from datetime import datetime
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='名称')
    image = models.ImageField(upload_to='products/', verbose_name='照片')
    description = models.TextField('简介', null=True, blank=True)
    nutrition = models.TextField('营养成分', null=True, blank=True)
    effect = models.TextField('用途功效', null=True, blank=True)
    created = models.DateTimeField('上架时间', default=datetime.now)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Photo(models.Model):
    product = models.ForeignKey(Product, related_name='photos', verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', verbose_name='照片')

    class Meta:
        verbose_name = '商品照片'
        verbose_name_plural = verbose_name


class Item(models.Model):
    product = models.ForeignKey(Product, related_name='items', verbose_name='商品', on_delete=models.CASCADE)
    description = models.CharField(max_length=20, null=True, blank=True, verbose_name='项目描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    unit = models.CharField(max_length=10, verbose_name='单位')
    stock = models.PositiveIntegerField('库存')

    class Meta:
        ordering = ('price',)
        verbose_name = '购买项目'
        verbose_name_plural = verbose_name
