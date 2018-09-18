from rest_framework import serializers
from users.models import User


class OAuthQQSerializer(serializers.Serializer):
    mobile = serializers.RegexField(regex='1[3-8]\d{9}', max_length=11)
    password = serializers.CharField(max_length=20, min_length=8, write_only=True)
    sms_code = serializers.CharField(max_length=6, min_length=6, write_only=True)
    access_token = serializers.CharField(write_only=True)



    def validate(self, attrs):
        # 短信验证码验证

        # access——token解密验证


        # 用户验证
        # 1、用户查询不到
            # 创建用户

        # 用户查询到  校验密码

        pass

    def create(self, validated_data):
        # 绑定操作  创建出OAuthQQModel模型类对象


        pass


