# _*_ coding: utf-8 _*_
# @Time     : 20:55
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    # 用户注册
    username = serializers.CharField(label='用户名', help_text='用户名',
                                     required=True, allow_blank=False,
                                     validators=[UniqueValidator(
                                         queryset=User.objects.all(),
                                         message='用户已经存在'
                                     )])
    # 输入密码的时候不显示明文
    password = serializers.CharField(style={'input_type': 'password'},
                                     label='密码', write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserDetailSerializer(serializers.ModelSerializer):
    # 用户详情
    class Meta:
        model = User
        fields = ('username', 'password')
