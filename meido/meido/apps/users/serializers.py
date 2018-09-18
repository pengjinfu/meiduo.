import re
from rest_framework import serializers
from users.models import User
from django_redis import get_redis_connection
from rest_framework_jwt.settings import api_settings

'''
username	str	是	用户名
password	str	是	密码
password2	str	是	确认密码
sms_code	str	是	短信验证码
mobile	str	是	手机号
allow	str	是	是否同意用户协议

'''


class UserSerializer(serializers.ModelSerializer):
    # 额外到字段验证需要显示指明
    password2 = serializers.CharField(max_length=20, min_length=8, write_only=True)
    sms_code = serializers.CharField(max_length=6, min_length=6, write_only=True)
    allow = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'password', 'password2', 'sms_code', 'allow', 'token')
        # 对于模型类字段进行额外限制条件添加
        extra_kwargs = {
            'username': {
                'max_length': 20,
                'min_length': 5,
                'error_messages': {
                    'max_length': '名字过长',
                    'min_length': '名字过短'
                }
            },
            'password': {
                'write_only': True,
                'max_length': 20,
                'min_length': 8,
                'error_messages': {
                    'max_length': '密码过长',
                    'min_length': '密码过短'
                }
            }

        }

    # 手机号验证
    def validate_mobile(self, value):

        print(value)

        if not re.match(r'^1[3-9]\d{9}$', value):
            return serializers.ValidationError('手机号不正确')

        return value

    # 选中状态
    def validate_allow(self, value):

        if value != 'true':
            return serializers.ValidationError('状态未选中')

        return value

    def validate(self, attrs):

        # 密码判断
        if attrs['password'] != attrs['password2']:
            return serializers.ValidationError('密码不一致')

        # 短信验证
        # 从缓存中取出短息
        conn = get_redis_connection('verify')
        sms_code_real = conn.get('sms_code_%s' % attrs['mobile'])
        # 获取不到短信
        if not sms_code_real:
            return serializers.ValidationError('短信失效')

        if attrs['sms_code'] != sms_code_real.decode():
            return serializers.ValidationError('短信不一致')

        return attrs

    def create(self, validated_data):

        print(validated_data)
        # 删除不需要保存的字段数据
        del validated_data['password2']
        del validated_data['sms_code']
        del validated_data['allow']

        user = super().create(validated_data)
        # 对于明文密码加密
        user.set_password(validated_data['password'])
        user.save()

        # 生成jwt——token值返回
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # 对用户对象添加token属性
        user.token = token

        return user



