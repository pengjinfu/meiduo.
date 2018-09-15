# meiduo.
#美多商城项目：
#1. 项目准备
  ##1.1. 商业模式
    ###目的：知道美多商城项目属于B2C商业模式。
    ###商业模式介绍：
        1.B2B--企业对企业		    案例：阿里巴巴、慧聪网
        2.C2C--个人对个人		    案例：淘宝、易趣、瓜子二手车
        3.B2C--企业对个人		    案例：唯品会、乐蜂网
        4.C2B--个人对企业		    案例：海尔商城、 尚品宅配
        5.O2O--线上到线下		    案例：美团、饿了吗
        6.F2C--工厂到个人		    案例：戴尔
        7.B2B2C--企业--企业--个人	案例：京东商城、天猫商城
        
  ##1.2. 开发流程
    ###1. 架构设计
        分析可能用到的技术点
        前后端是否分离
        前端使用哪些框架
        后端使用哪些框架
        选择什么数据库
        如何实现缓存
        是否搭建分布式服务
        如何管理源代码
    ###2. 数据库设计
        数据库表的设计至关重要
        根据项目需求，设计合适的数据库表
        数据库表在前期如果设计不合理，后期随需求增加会变得难以维护
    ###3. 集成测试
        在测试阶段要留意测试反馈平台的bug报告

  ##1.3. 需求分析
    需求分析
    在需求分析阶段，我们可以借助产品原型图来分析。分析完后，前端按照产品原型图开发前端页面，后端开发响应业务处理。
    我们现在可以假借示例网站作为原型图来分析需求。

    ###1. 用户部分
        注册
            短信验证码
        登录
        第三方登录
        个人信息
            邮箱填写与验证
            浏览历史记录
        地址管理
            省市区地址信息加载
            新增修改删除地址
            设置默认地址
       修改密码
    ###2. 商品部分
        首页
            商品分类
            广告控制
        商品列表
        商品详情
        商品搜索
    ###3. 购物车部分
        购物车管理 
    ###4. 订单部分
        提交订单
        我的订单
        订单评价
    ###5. 支付部分
        支付宝支付

  ##1.4. 项目架构
    ###项目架构
        项目采用前后端分离的应用模式
        前端使用Vue.js
        后端使用Django REST framework
    ###前端部分：用户页面、商品页面、购物车页面、订单页面、运营后台管理页面
    ###后端部分：用户模块、商品模块、购物车模块、订单模块、搜索模块
    ###其它技术栈：mysql(主从同步，双机热备）、 redis（session、缓存）、 celery（异步服务）、 FastDFS（分步式存储服务）
  ##1.5. 创建工程
  ###本部分属于架构师部分：
  ###本项目使用git管理项目代码，代码库放在github或gitee码云平台。（注意，公司中通常放在github私有服务器中）。
  ###1.在github或gitee码云平台上创建工程：
      1.1创建公有项目库
      1.2填写项目库信息

      本步骤属于后端人员所做之事。
      1.3克隆项目到本地
      git clone https://xxx
      ----------------------------------------------------------------------------------------
      前端人员和后端人员同时对应各自部分开发。这里假设前端部分已经完成。
  ###2.把前端文件添加到项目中
      2.1 添加文件
          git add 前端文件
          git status  # 查看状态
          git commit -m"描述所做的事“
          gitp push  # 把添加文件推送到远程仓库

      2.2 前端文件开发预览
            安装：
            curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

            重新进入终端，使用nvm安装最新版本的node.js
                nvm install node
           安装live-server
                npm install -g live-server
           使用
                # 在前端静态文件目录下执行
                live-server
  ###3.创建Django REST framework工程
       3.1 创建虚拟环境
            在终端下执行：
            创建虚拟环境： mkvirtualenv -p python3 py3_Django
            查看：workon
            使用虚拟环境：workon py3_Django
            查看安装的包：pip list
            指定安装Django版本:pip install Django==1.11.11
            安装其它的包：pip install djangorestframework及其它在开发中所需要的包均用此命令
            创建Django REST framework工程：django-admin startproject meiduo

       3.2 使用pycharm进行工程开发
            打开创建的meiduo项目
            选择虚拟环境：py3_Django
                            .
                ├── db.sqlite3
                ├── manage.py
                └── meiduo
                    ├── __init__.py
                    ├── settings.py
                    ├── urls.py
                    └── wsgi.py

  ##1.6. 配置
       ###1.在meiduo包里创建一个apps的包：存放Django的应用

       ###2.在meiduo包里创建一个settings：存放配置文件的目录，分为开发dev和线上prod
            并把原settings.py名字更改为dev.py

       ###3.修改manage.py中项目settings的路径：os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo.settings.dev")

       ###4.创建数据库：为项目单独创建一个有权限的数据库
            create database meiduo default charset=utf8;
            create user meiduo identified by 'meiduo';
            grant all on meiduo.* to 'meiduo'@'%';
            flush privileges;
            说明：
            第一句：创建用户账号 meiduo, 密码 meiduo (由identified by 指明)
            第二句：授权meiduo数据库下的所有表（meiduo.*）的所有权限（all）给用户meiduo在以任何ip访问数据库的时候（'meiduo'@'%'）
            第三句：刷新生效用户权限

       ###5.在工程目录/meiduo/apps目录下，创建一个应用users：
            cd meiduo/meiduo/apps
            django-admin startapp users

       ###6.修改settings/dev.py 文件中的路径信息
            INSTALLED_APPS = [
                ...
                'meiduo.apps.users.apps.UsersConfig',
            ]

            重要：
            为了还能像如下方式简便的注册引用，我们需要向Python解释器的导包路径中添加apps应用目录的路径。

            INSTALLED_APPS = [
                ...
                'users.apps.UsersConfig',
            ]
            我们将配置文件改为放在settings子目录下，所以 配置文件中的BASE_DIR指向的变为了meiduo/meiduo/meiduo。

            使用sys.path添加<BASE_DIR>/apps目录，即可添加apps应用的导包路径。

            代码：

            # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # 添加导包路径
            import sys
            sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

       ###7.修改settings/dev.py 文件中的INSTALLED_APPS
           INSTALLED_APPS = [
                ...
                'rest_framework',
            ]
       ###8.配置数据库
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '127.0.0.1',  # 数据库主机
                    'PORT': 3306,  # 数据库端口
                    'USER': 'meiduo',  # 数据库用户名
                    'PASSWORD': 'meiduo',  # 数据库用户密码
                    'NAME': 'meiduo'  # 数据库名字
                }
            }
            在使用数据库前，一定安装驱动：
            meiduo/meiduo/__init__.py文件中添加
                import pymysql
                pymysql.install_as_MySQLdb()

       ###9.配置redis
           CACHES = {
                "default": {
                    "BACKEND": "django_redis.cache.RedisCache",
                    "LOCATION": "redis://10.211.55.5:6379/0",
                    "OPTIONS": {
                        "CLIENT_CLASS": "django_redis.client.DefaultClient",
                    }
                },
                "session": {
                    "BACKEND": "django_redis.cache.RedisCache",
                    "LOCATION": "redis://10.211.55.5:6379/1",
                    "OPTIONS": {
                        "CLIENT_CLASS": "django_redis.client.DefaultClient",
                    }
                }
            }
            SESSION_ENGINE = "django.contrib.sessions.backends.cache"
            SESSION_CACHE_ALIAS = "session"
            除了名为default的redis配置外，还补充了名为session的redis配置，分别使用两个不同的redis库。

            同时修改了Django的Session机制使用redis保存，且使用名为'session'的redis配置。

            此处修改Django的Session机制存储主要是为了给Admin站点使用。

       ###10.  本地化语言与时区
            LANGUAGE_CODE = 'zh-hans'
            TIME_ZONE = 'Asia/Shanghai'

       ###11.配置日志：并在根容器下创建logs文件
            LOGGING = {
                'version': 1,
                'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
                'formatters': {  # 日志信息显示的格式
                    'verbose': {
                        'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
                    },
                    'simple': {
                        'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
                    },
                },
                'filters': {  # 对日志进行过滤
                    'require_debug_true': {  # django在debug模式下才输出日志
                        '()': 'django.utils.log.RequireDebugTrue',
                    },
                },
                'handlers': {  # 日志处理方法
                    'console': {  # 向终端中输出日志
                        'level': 'INFO',
                        'filters': ['require_debug_true'],
                        'class': 'logging.StreamHandler',
                        'formatter': 'simple'
                    },
                    'file': {  # 向文件中输出日志
                        'level': 'INFO',
                        'class': 'logging.handlers.RotatingFileHandler',
                        'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/meiduo.log"),  # 日志文件的位置
                        'maxBytes': 300 * 1024 * 1024,
                        'backupCount': 10,
                        'formatter': 'verbose'
                    },
                },
                'loggers': {  # 日志器
                    'django': {  # 定义了一个名为django的日志器
                        'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
                        'propagate': True,  # 是否继续传递日志信息
                        'level': 'INFO',  # 日志器接收的最低日志级别
                    },
                }
            }

       ###12. 异常处理
        修改Django REST framework的默认异常处理方法，补充处理数据库异常和Redis异常。
        新建utils/exceptions.py

        from rest_framework.views import exception_handler as drf_exception_handler
        import logging
        from django.db import DatabaseError
        from redis.exceptions import RedisError
        from rest_framework.response import Response
        from rest_framework import status

        # 获取在配置文件中定义的logger，用来记录日志
        logger = logging.getLogger('django')

        def exception_handler(exc, context):
            """
            自定义异常处理
            :param exc: 异常
            :param context: 抛出异常的上下文
            :return: Response响应对象
            """
            # 调用drf框架原生的异常处理方法
            response = drf_exception_handler(exc, context)

            if response is None:
                view = context['view']
                if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
                    # 数据库异常
                    logger.error('[%s] %s' % (view, exc))
                    response = Response({'message': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

            return response
        配置文件settings/dev.py 中添加
            REST_FRAMEWORK = {
                # 异常处理
                'EXCEPTION_HANDLER': 'meiduo.utils.exceptions.exception_handler',
            }


#2. 用户部分
  ##2.1. 用户模型类
    ###Django提供了认证系统，文档资料https://yiyibooks.cn/xx/Django_1.11.6/topics/auth/index.html
    ###Django认证系统同时处理认证和授权。

    ###Django的认证系统包含：
        用户
        权限：二元（是/否）标志指示一个用户是否可以做一个特定的任务。
        组：对多个用户运用标签和权限的一种通用的方式。
        一个可配置的密码哈希系统
        用户登录或内容显示的表单和视图
        一个可插拔的后台系统
    ###Django默认提供的认证系统中，用户的认证机制依赖Session机制，我们在本项目中将引入JWT认证机制，将用户的身份凭据存放在Token中，
    然后对接Django的认证系统，帮助我们来实现：
        用户的数据模型
        用户密码的加密与验证
        用户的权限系统
        Django用户模型类

    ###Django认证系统中提供了用户模型类User保存用户的数据，默认的User包含以下常见的基本字段：

        username：必选。 150个字符以内。 用户名可能包含字母数字，_，@，+ . 和-个字符。在Django更改1.10：max_length从30个字符增加到150个字符。

        主要英文名中使用：
            first_name：可选（blank=True）。 少于等于30个字符。
            last_name：可选（blank=True）。 少于等于30个字符。

        email： 可选（blank=True）。 邮箱地址。

        password： 必选。 密码的哈希及元数据。 （Django 不保存原始密码）。 原始密码可以无限长而且可以包含任意字符。

        groups：与Group 之间的多对多关系。

        user_permissions：与Permission 之间的多对多关系。

        is_staff：布尔值。 指示用户是否可以访问Admin 站点。

        is_active：
            布尔值。 指示用户的账号是否激活。 我们建议您将此标志设置为False而不是删除帐户；这样，如果您的应用程序对用户有任何外键，则外键不会中断
            。它不是用来控制用户是否能够登录。 在Django更改1.10：在旧版本中，默认is_active为False不能进行登录。

        is_superuser： 布尔值。 指定这个用户拥有所有的权限而不需要给他们分配明确的权限。

        last_login：用户最后一次登录的时间。

        date_joined：账户创建的时间。 当账号创建时，默认设置为当前的date/time。


    ###常用方法：
        set_password(raw_password)
            设置用户的密码为给定的原始字符串，并负责密码的。 不会保存User 对象。当None 为raw_password 时，密码将设置为一个不可用的密码。

        check_password(raw_password)
            如果给定的raw_password是用户的真实密码，则返回True，可以在校验用户密码时使用。

    ###管理器方法：
    管理器方法即可以通过User.objects. 进行调用的方法。
        create_user(username, email=None, password=None, *\extra_fields*)
        创建、保存并返回一个User对象。

        create_superuser(username, email, password, *\extra_fields*)
        与create_user() 相同，但是设置is_staff 和is_superuser 为True。

    ###创建自定义的用户模型类：
        Django认证系统中提供的用户模型类及方法很方便，我们可以使用这个模型类，但是字段有些无法满足项目需求，如本项目中需要保存用户的手机号
     ，需要给模型类添加额外的字段。

        Django提供了django.contrib.auth.models.AbstractUser用户抽象模型类允许我们继承，扩展字段来使用Django认证系统的用户模型类。

        我们现在在meiduo/meiduo/apps中创建Django应用users，并在配置文件中注册users应用。（已经在配置中完成）

        在创建好的应用models.py中定义用户的用户模型类。
        class User(AbstractUser):
            """用户模型类"""
            mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

            class Meta:
                db_table = 'tb_users'
                verbose_name = '用户'
                verbose_name_plural = verbose_name

        ###我们自定义的用户模型类还不能直接被Django的认证系统所识别，需要在配置文件中告知Django认证系统使用我们自定义的模型类。

        ###配置文件settings/dev.py 中添加
            AUTH_USER_MODEL = 'users.User'
            AUTH_USER_MODEL 参数的设置以点.来分隔，表示应用名.模型类名。

        ###注意（重要）：Django建议我们对于AUTH_USER_MODEL参数的设置一定要在第一次数据库迁移之前就设置好，否则后续使用可能出现未知错误。

        ###执行数据库迁移:在终端中输入以下命令：/meiduo./meiduo$
            python manage.py makemigrations
            python manage.py migrate


  ##2.2. 注册业务接口分析
    创建好用户模型类后，我们开始来实现第一个业务逻辑——用户注册。

    设计接口的思路
        分析要实现的业务逻辑，明确在这个业务中需要涉及到几个相关子业务，将每个子业务当做一个接口来设计。

    分析接口的功能任务，明确接口的访问方式与返回数据：
        接口的请求方式，如GET 、POST 、PUT等
        接口的URL路径定义
        需要前端传递的数据及数据格式（如路径参数、查询字符串、请求体表单、JSON等）
        返回给前端的数据及数据格式
        特别强调：在前后端分离的应用模式中，我们作为后端开发人员设计后端接口时，可以不用考虑返回给前端数据后，前端如何处理，这是前端开发人
    员的工作，我们只需明确我们要保存的或者要返回的是什么数据即可。

    明确上述每一点后，即可开始编写接口。

    注册业务接口分析
        在用户注册中，需要实现以下接口：
            短信验证码
            用户名判断是否存在
            手机号判断是否存在
            注册保存用户数据

        提示：
            短信验证码考虑到后续可能会在其他业务中也用到，因此我们将验证码独立
            创建一个新应用verifications，在此应用中实现短信验证码
        注：新建应用verifications是因为在后面的第三方登录中还要使用，所以为达到重用效果。


  ##2.3. 短信验证码
    ###1. 业务处理流程
        生成和发送短信验证码
        保存短信验证码
        redis pipeline的使用
        检查是否在60s内有发送记录
        Celery异步发送短信
    ###2. 后端接口设计：
        2.1访问方式： GET /sms_codes/(?P<mobile>1[3-9]\d{9})/

        2.2请求参数： 路径参数
        参数      类型	  是否必须	  说明
        mobile	  str	     是	     手机号

        2.3返回数据： JSON
        返回值	    类型	    是否必传	        说明
        message	     str	   否	      OK，发送成功


        2.4视图原型：

        # url('^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),
        class SMSCodeView(APIView):
            """
            发送短信验证码
            传入参数：
                mobile, image_code_id, text
            """
            pass

    ###3. 后端实现
        在verifications/views.py中定义实现视图：
        class SMSCodeView(APIView):
            """发送短信验证码"""

            def get(self, request, mobile):

                # 创建连接到redis的对象
                redis_conn = get_redis_connection('verify_codes')

                # 60秒内不允许重发发送短信
                send_flag = redis_conn.get('send_flag_%s' % mobile)
                if send_flag:
                    return Response({"message": "发送短信过于频繁"}, status=status.HTTP_400_BAD_REQUEST)

                # 生成和发送短信验证码
                sms_code = '%06d' % random.randint(0,999999)
                logger.debug(sms_code)

                CCP().send_template_sms(mobile,[sms_code, constants.SMS_CODE_REDIS_EXPIRES // 60], constants.SEND_SMS_TEMPLATE_ID)

                # 以下代码演示redis管道pipeline的使用
                pl = redis_conn.pipeline()
                pl.setex("sms_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
                pl.setex('send_flag_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
                # 执行
                pl.execute()

                # 响应发送短信验证码结果
                return Response({"message": "OK"})
    ##4. 设置域名
        4.1我们现在为前端和后端分别设置两个不同的域名
        位置	            域名
        前端	        www.meiduo.site
        后端	        api.meiduo.site


        4.2编辑/etc/hosts文件，可以设置本地域名
            sudo vim /etc/hosts
            在文件中增加两条信息
            127.0.0.1   api.meiduo.site
            127.0.0.1   www.meiduo.site

        4.3windows系统中若设置本地域名，hosts文件在如下目录：
            C:\Windows\System32\drivers\etc
            我们在前端front_end_pc/js目录中，创建host.js文件用以为前端保存后端域名

        4.4var host = 'http://api.meiduo.site:8000';
            在所有需要访问后端接口的前端页面中都引入host.js，使用host变量即可指代后端域名。

        修改settings配置中的ALLOWED_HOSTS
            一旦不再使用127.0.0.1访问Django后端，需要在配置文件中修改ALLOWED_HOSTS，增加可以访问后端的域名

            ALLOWED_HOSTS = ['api.meiduo.site', '127.0.0.1', 'localhost', 'www.meiduo.site']


  ##2.4. 跨域CORS
    ###1.我们为前端和后端分别设置了两个不同的域名
    位置	        域名
    前端  	www.meiduo.site
    后端	a   pi.meiduo.site

    ###2.现在，前端与后端分处不同的域名，我们需要为后端添加跨域访问的支持。
        我们使用CORS来解决后端对跨域访问的支持。
        使用django-cors-headers扩展
        参考文档https://github.com/ottoyiu/django-cors-headers/

        2.1安装
            pip install django-cors-headers

    ###3.添加应用
        INSTALLED_APPS = (
            ...
            'corsheaders',
            ...
        )
    ###4.中间层设置
        MIDDLEWARE = [
            'corsheaders.middleware.CorsMiddleware',
            ...
        ]
    ###5.添加白名单
        # CORS
        CORS_ORIGIN_WHITELIST = (
            '127.0.0.1:8080',
            'localhost:8080',
            'www.meiduo.site:8080',
            'api.meiduo.site:8000'
        )
        CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
        凡是出现在白名单中的域名，都可以访问后端接口
        CORS_ALLOW_CREDENTIALS 指明在跨域访问中，后端是否支持对cookie的操作。

  ###2.5. 使用Celery发送短信
    celery使用
    在meiduo/meidUo下创建celery_tasks用于保存celery异步任务。
    在celery_tasks目录下创建config.py文件，用于保存celery的配置信息
        broker_url = "redis://127.0.0.1/14"

    在celery_tasks目录下创建main.py文件，用于作为celery的启动文件

        from celery import Celery

        # 为celery使用django配置文件进行设置
        import os
        if not os.getenv('DJANGO_SETTINGS_MODULE'):
            os.environ['DJANGO_SETTINGS_MODULE'] = 'meidUo.settings.dev'

        # 创建celery应用
        app = Celery('meiduo')

        # 导入celery配置
        app.config_from_object('celery_tasks.config')

        # 自动注册celery任务
        app.autodiscover_tasks(['celery_tasks.sms'])


    在celery_tasks目录下创建sms目录，用于放置发送短信的异步任务相关代码。
    将提供的发送短信的云通讯SDK放到celery_tasks/sms/目录下。
    在celery_tasks/sms/目录下创建tasks.py文件，用于保存发送短信的异步任务

        import logging

        from celery_tasks.main import app
        from .yuntongxun.sms import CCP

        logger = logging.getLogger("django")

        # 验证码短信模板
        SMS_CODE_TEMP_ID = 1

        @app.task(name='send_sms_code')
        def send_sms_code(mobile, code, expires):
            """
            发送短信验证码
            :param mobile: 手机号
            :param code: 验证码
            :param expires: 有效期
            :return: None
            """

            try:
                ccp = CCP()
                result = ccp.send_template_sms(mobile, [code, expires], SMS_CODE_TEMP_ID)
            except Exception as e:
                logger.error("发送验证码短信[异常][ mobile: %s, message: %s ]" % (mobile, e))
            else:
                if result == 0:
                    logger.info("发送验证码短信[正常][ mobile: %s ]" % mobile)
                else:
                    logger.warning("发送验证码短信[失败][ mobile: %s ]" % mobile)
        在verifications/views.py中改写SMSCodeView视图，使用celery异步任务发送短信

        from celery_tasks.sms import tasks as sms_tasks

        class SMSCodeView(GenericAPIView):
            ...
                # 发送短信验证码
                sms_code_expires = str(constants.SMS_CODE_REDIS_EXPIRES // 60)
                sms_tasks.send_sms_code.delay(mobile, sms_code, sms_code_expires)

                return Response({"message": "OK"})


#2.6. 判断帐号是否存在
#2.7. 注册
#2.8. JWT
#2.9. Django REST framework JWT
#2.10. 账号登录
#2.11. QQ登录
#2.12. 用户中心个人信息
#2.13. 邮件与验证
#2.14. 收货地址




