from django.db import models
from django.contrib.auth.models import User
from shop.models import Item


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name='购买项目', on_delete=models.CASCADE)
    quantity = models.IntegerField('数量')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ("user", "item")

    def __str__(self):
        return "%s(%d)".format(self.item.items.name, self.quantity)
