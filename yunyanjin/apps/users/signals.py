# _*_ coding: utf-8 _*_
# @Time     : 11:01
# @Author   : Amir
# @Site     : 
# @File     : signals.py
# @Software : PyCharm

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# post_save: 接受信号的方式
# sender: 接收信号的model
@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    # 是否新建，因为update的时候也会进行post_save
    if created:
        password = instance.password
        # 这里的instance相当于User 这个model
        instance.set_password(password)
        instance.save()