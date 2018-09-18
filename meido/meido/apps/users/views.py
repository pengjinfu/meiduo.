from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, GenericAPIView, CreateAPIView
from rest_framework.response import Response
from users.models import User

# Create your views here.
from users.serializers import UserSerializer


class UserNmaeView(GenericAPIView):
    def get(self, request, username):
        # 用户名数量查询
        count = User.objects.filter(username=username).count()

        # 返回数量
        return Response(
            {
                'username': username,
                'count': count
            }
        )


class MobileView(GenericAPIView):
    def get(self, request, mobile):

        # 手机号数量查询
        count = User.objects.filter(mobile=mobile).count()

        # 返回数量
        return Response(
            {
                'mobile': mobile,
                'count': count
            }
        )


class UserView(CreateAPIView):
    serializer_class = UserSerializer


    # def post(self, request, *args, **kwargs):




