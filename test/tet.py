#!/usr/bin/env python
# encoding: utf-8
'''
@Time: 2023/2/15 16:40
@Project: R_jyyx 
@File: tet.py
@Author: R_记忆犹新
@Software: pycharm
@Desc:
'''
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

token = ''
signature = ''
timestamp = ''
nonce = ''


try:
    check_signature(token, signature, timestamp, nonce)
except InvalidSignatureException:
    # 处理异常情况或忽略
	print('异常')