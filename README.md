# meiduo.
美多商城项目：
1. 项目准备
  1.1. 商业模式
    目的：知道美多商城项目属于B2C商业模式。
    商业模式介绍：
        1.B2B--企业对企业		    案例：阿里巴巴、慧聪网
        2.C2C--个人对个人		    案例：淘宝、易趣、瓜子二手车
        3.B2C--企业对个人		    案例：唯品会、乐蜂网
        4.C2B--个人对企业		    案例：海尔商城、 尚品宅配
        5.O2O--线上到线下		    案例：美团、饿了吗
        6.F2C--工厂到个人		    案例：戴尔
        7.B2B2C--企业--企业--个人	案例：京东商城、天猫商城
        
  1.2. 开发流程
    1. 架构设计
        分析可能用到的技术点
        前后端是否分离
        前端使用哪些框架
        后端使用哪些框架
        选择什么数据库
        如何实现缓存
        是否搭建分布式服务
        如何管理源代码
    2. 数据库设计
        数据库表的设计至关重要
        根据项目需求，设计合适的数据库表
        数据库表在前期如果设计不合理，后期随需求增加会变得难以维护
    3. 集成测试
        在测试阶段要留意测试反馈平台的bug报告

  1.3. 需求分析
    需求分析
    在需求分析阶段，我们可以借助产品原型图来分析。分析完后，前端按照产品原型图开发前端页面，后端开发响应业务处理。
    我们现在可以假借示例网站作为原型图来分析需求。

    1. 用户部分
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
    2. 商品部分
        首页
            商品分类
            广告控制
        商品列表
        商品详情
        商品搜索
    3. 购物车部分
        购物车管理 
    4. 订单部分
        提交订单
        我的订单
        订单评价
    5. 支付部分
        支付宝支付

  1.4. 项目架构
    项目架构
        项目采用前后端分离的应用模式
        前端使用Vue.js
        后端使用Django REST framework
    前端部分：用户页面、商品页面、购物车页面、订单页面、运营后台管理页面
    后端部分：用户模块、商品模块、购物车模块、订单模块、搜索模块
    其它技术栈：mysql(主从同步，双机热备）、 redis（session、缓存）、 celery（异步服务）、 FastDFS（分步式存储服务）
  1.5. 创建工程
  本部分属于架构师部分：
  本项目使用git管理项目代码，代码库放在github或gitee码云平台。（注意，公司中通常放在github私有服务器中）。
  1.在github或gitee码云平台上创建工程：
      1.1创建公有项目库
      1.2填写项目库信息

      本步骤属于后端人员所做之事。
      1.3克隆项目到本地
      git clone https://xxx
      ----------------------------------------------------------------------------------------
      前端人员和后端人员同时对应各自部分开发。这里假设前端部分已经完成。
  2.把前端文件添加到项目中
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
  3.创建Django REST framework工程
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

  1.6. 配置
       1.在meiduo包里创建一个apps的包：存放Django的应用
       2.在meiduo包里创建一个settings：存放配置文件的目录，分为开发dev和线上prod
            并把原settings.py名字更改为dev.py
       3.修改manage.py中项目settings的路径：os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo.settings.dev")
       4.创建数据库：为项目单独创建一个有权限的数据库
            create database meiduo default charset=utf8;
            create user meiduo identified by 'meiduo';
            grant all on meiduo.* to 'meiduo'@'%';
            flush privileges;
            说明：

            第一句：创建用户账号 meiduo, 密码 meiduo (由identified by 指明)
            第二句：授权meiduo数据库下的所有表（meiduo.*）的所有权限（all）给用户meiduo在以任何ip访问数据库的时候（'meiduo'@'%'）
            第三句：刷新生效用户权限
       5.在工程目录/meiduo_mall/apps目录下，创建一个应用users：
            cd meiduo/meiduo/apps
            django-admin startapp users
       6.修改settings/dev.py 文件中的路径信息
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

       7.修改settings/dev.py 文件中的INSTALLED_APPS
           INSTALLED_APPS = [
                ...
                'rest_framework',
            ]
       8.配置数据库
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '127.0.0.1',  # 数据库主机
                    'PORT': 3306,  # 数据库端口
                    'USER': 'meiduo',  # 数据库用户名
                    'PASSWORD': 'meiduo',  # 数据库用户密码
                    'NAME': 'meiduo_mall'  # 数据库名字
                }
            }
            在使用数据库前，一定安装驱动：
            meiduo/meiduo/__init__.py文件中添加
                import pymysql
                pymysql.install_as_MySQLdb()
       9.配置redis
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
       10.  本地化语言与时区
            LANGUAGE_CODE = 'zh-hans'
            TIME_ZONE = 'Asia/Shanghai'

       11.配置日志：并在根容器下创建logs文件
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
       12.7. 异常处理
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
        配置文件中添加

        REST_FRAMEWORK = {
            # 异常处理
            'EXCEPTION_HANDLER': 'meiduo_mall.utils.exceptions.exception_handler',
        }
2. 用户部分
  2.1. 用户模型类
  2.2. 注册业务接口分析
  2.3. 短信验证码
  2.4. 跨域CORS
  2.5. 使用Celery发送短信
  2.6. 判断帐号是否存在
  2.7. 注册
  2.8. JWT
  2.9. Django REST framework JWT
  2.10. 账号登录
  2.11. QQ登录
  2.12. 用户中心个人信息
  2.13. 邮件与验证
  2.14. 收货地址




