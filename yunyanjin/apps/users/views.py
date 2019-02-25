from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from django.contrib.auth.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.permissions import IsAuthenticated


class UserViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        playload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(playload)
        re_dict['username'] = user.username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsAuthenticated()]
        elif self.action == 'create':
            return []
        return []

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserSerializer
        return UserDetailSerializer

    # 虽然继承了Retrievev 可以获取用户详情，但是并不知道用户的id，所以要重写get_object方法
    # 重写get_object方法就知道是哪个用户了
    def get_object(self):
        return self.request.user


