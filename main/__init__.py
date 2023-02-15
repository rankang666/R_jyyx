#!/usr/bin/env python
# encoding: utf-8
'''
@Time: 2023/2/15 11:36
@Project: R_jyyx 
@File: __init__.py.py
@Author: R_记忆犹新
@Software: pycharm
@Desc:
'''

from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from redis import Redis
from .plugins.queue import make_celery

app = Flask(__name__, instance_relative_config=True)
# 加载配置
app.config.from_object('config')
app.config.from_pyfile('config.py')

# 队列
celery = make_celery(app)

# 记录日志
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.WARNING)
app.logger.addHandler(handler)

# 初始第三方库
redis = Redis()


# 路由
from .routes import *
# 定时任务
from .plugins.cron import *