from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from random import randint
from django_redis import get_redis_connection
from meido.libs.yuntongxun.sms import CCP
from celery_tasks.sms.tasks import send_sms_code

# Create your views here.


class SMSCodeView(APIView):

    def get(self,request,mobile):

        # 判断60s
        conn = get_redis_connection('verify')
        flag=conn.get('sms_flag_%s'%mobile)
        if flag:
            return Response({'message':'errors'},status=401)

        # 生成短信验证码
        sms_code='%06d'%randint(0,999999)

        # 保存短信到redis缓存中
        pl=conn.pipeline()
        pl.setex('sms_code_%s'%mobile,300,sms_code)
        pl.setex('sms_flag_%s'%mobile,60,1)
        pl.execute()

        # 发送短信
        # ccp=CCP()
        # ccp.send_template_sms(mobile,[sms_code,'5'],1)
        send_sms_code.delay(mobile,sms_code)

        # 结果返回
        return Response({'message':'ok'})