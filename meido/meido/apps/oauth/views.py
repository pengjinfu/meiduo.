from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from QQLoginTool.QQtool import OAuthQQ
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from itsdangerous import TimedJSONWebSignatureSerializer as TJS

from oauth.models import OAuthQQModel


# Create your views here.
from oauth.serializers import OAuthQQSerializer


class QQLoginURLView(APIView):
    def get(self, request):
        # 获取前传递next
        next = request.query_params.get('next')

        if not next:
            next = '/'

        # 构建出引导用户跳转qq登录页面的url地址
        print(settings.SECRET_KEY)
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET,
                        redirect_uri=settings.QQ_REDIRECT_URI, state=next)

        # 获取qq登录地址
        login_url=oauth.get_qq_url()

        # 返回地址给前端

        return Response(
            {
                'login_url':login_url
            }
        )


class QQLoginView(APIView):

    def get(self,request):

        # 获取code值
        code=request.query_params.get('code')

        if not code:
            return Response({'message':'缺少code值'},status=401)

        # 获取access——token
        oauth=OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET,
                        redirect_uri=settings.QQ_REDIRECT_URI, state=next)
        access_token=oauth.get_access_token(code)

        # 获取openid数据
        openid=oauth.get_open_id(access_token)
        # 进行绑定
        #1\判断用户有没有绑定过
        try:
            qq_oauth=OAuthQQModel.objects.get(openid=openid)

        except:
            # 未绑定
            tjs=TJS(settings.SECRET_KEY,300)
            data={'openid':openid}
            access_token=tjs.dumps(data).decode()
            return Response({'access_token':access_token})

        # 绑定过跳转到登录成功页面
        # 获取user用户
        user=qq_oauth.user

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response(
            {
                'token':token,
                'username':user.username,
                'user_id':user.id
            }
        )

    def post(self,request):
        """
            处理绑定openid业务逻辑
        :param request:
        :return:
        """
        # 获取前端数据
        data=request.data

        # 验证数据
        ser=OAuthQQSerializer(data=data)

        ser.is_valid()

        # 绑定保存操作
        ser.save()

        # 结果返回

        return Response()

